from pathlib import Path
import re
p = Path("services/workflow_store_service/app/storage.py")
s = p.read_text(encoding="utf-8")
# 确保 import os 存在
if "import json" not in s:
    s = s.replace("import json", "import json\nimport os")
resolver = r'''
def resolve_core_platform_dir() -> Path:
    env = os.environ.get("MAOMIAI_CORE_PLATFORM_DIR")
    if env:
        root = Path(env).expanduser().resolve()
        if root.exists():
            return root
    here = Path(__file__).resolve()
    for parent in [here, *here.parents]:
        if (
            (parent / "services").exists()
            and (parent / "apps").exists()
            and (parent / "scripts").exists()
        ):
            return parent
    cwd = Path.cwd().resolve()
    for parent in [cwd, *cwd.parents]:
        if (
            (parent / "services").exists()
            and (parent / "apps").exists()
            and (parent / "scripts").exists()
        ):
            return parent
    return cwd
'''
# 替换 BASE_DIR 定义
s = re.sub(
    r"BASE_DIR\s*=\s*Path\([^\n]+\)\n",
    resolver + "\nBASE_DIR = resolve_core_platform_dir()\n",
    s,
    count=1
)
# 防止 load_store 把临时空文件误判为 corrupt 一直备份
old = r'''def load_store\(\) -> StoreFile:
    ensure_data_dir\(\)
    with _LOCK:
        if not STORE_PATH\.exists\(\):
            store = StoreFile\(\)
            save_store\(store\)
            return store
        try:
            raw = json\.loads\(STORE_PATH\.read_text\(encoding="utf-8"\)\)\)
            return StoreFile\.model_validate\(raw\)
        except Exception:
            backup = STORE_PATH\.with_suffix\(f"\.corrupt\.\{int\(time\.time\(\)\)\}\.json"\)\)
            STORE_PATH\.rename\(backup\)
            store = StoreFile\(\)
            save_store\(store\)
            append_error\("load_store", "corrupt_store_recovered", \{"backup": str\(backup\)\}\)\)
            return store
'''
new = r'''def load_store\(\) -> StoreFile:
    ensure_data_dir\(\)
    with _LOCK:
        if not STORE_PATH\.exists\(\):
            store = StoreFile\(\)
            save_store\(store\)
            return store
        text = STORE_PATH\.read_text\(encoding="utf-8", errors="ignore"\)\.strip\(\)
        if not text:
            store = StoreFile\(\)
            save_store\(store\)
            append_error\("load_store", "empty_store_reinitialized", \{"path": str\(STORE_PATH\)\}\)\)
            return store
        try:
            raw = json\.loads\(text\)
            if not isinstance\(raw, dict\):
                raise ValueError\("store root must be object"\)\)
            raw\.setdefault\("store_version", "1\.0"\)
            raw\.setdefault\("items", \[\]\)
            return StoreFile\.model_validate\(raw\)
        except ValueError as e:
            backup = STORE_PATH\.with_suffix\(f"\.corrupt\.\{int\(time\.time\(\)\)\}\.json"\)\)
            try:
                STORE_PATH\.rename\(backup\)
            except Exception:
                pass
            store = StoreFile\(\)
            save_store\(store\)
            append_error\("load_store", "corrupt_store_recovered", \{
                "backup": str\(backup\),
                "error": str\(e\),
                "path": str\(STORE_PATH\),
            }\)\)
            return store
        except Exception as e:
            append_error\("load_store", f"io_error: {str\(e\)\)", \{"path": str\(STORE_PATH\)\}\)\)
            return StoreFile\(\)
'''
if old in s:
    s = s.replace(old, new)
else:
    print("WARN: exact load_store block not found, appending may be needed")
p.write_text(s, encoding="utf-8")
print("patched workflow storage path resolver")
