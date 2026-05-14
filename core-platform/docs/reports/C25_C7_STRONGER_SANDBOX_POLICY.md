# C25-C7 Stronger Sandbox Policy

## 实现内容

✅ 外部 sandbox policy 配置
✅ Sandbox profile loader
✅ Command policy validator
✅ Environment allowlist
✅ Timeout policy
✅ stdout/stderr max output policy
✅ Policy snapshot per sandbox execution
✅ Sandbox policy APIs

## 新增文件

- `core-platform/data/sandbox_policy/sandbox_policy.json` - 外部 policy 配置
- `app/runtime/sandbox_policy.py` - Policy loader 和 validator
- `app/runtime/sandbox_executor.py` - 外部 policy 驱动的执行器

## 新增 API

- `GET /agent/sandbox/policy` - 返回完整 policy 配置
- `GET /agent/sandbox/profile/{profile_name}` - 返回指定 profile

## Sandbox Policy 结构

```json
{
  "version": "0.1.0-c25-c7",
  "default_profile": "local_restricted",
  "profiles": {
    "local_restricted": {
      "allowed_binaries": ["python", "python3", "node", "bash", "sh"],
      "blocked_binaries": ["rm", "sudo", "curl", "wget", "ssh", "scp", "nc", "netcat", "powershell", "pwsh", "cmd", "reg", "diskutil", "launchctl"],
      "timeout_seconds": 20,
      "max_stdout_bytes": 200000,
      "max_stderr_bytes": 200000,
      "network": "disabled_by_policy",
      "filesystem": "sandbox_only",
      "env_allowlist": ["PATH", "PYTHONPATH", "NODE_PATH", "HOME", "TMPDIR"],
      "env_overrides": {"MAOMIAI_SANDBOX": "1"}
    }
  }
}
```

## 验证结果

✅ py_compile 通过
✅ hardcode guard 通过
✅ `python3 -c "print(123)"` 允许执行 (ok=True, stdout 包含 "123")
✅ `rm -rf /tmp/not-allowed` 被阻断 (ok=False, message="binary blocked by sandbox policy: rm")
✅ Sandbox 执行结果包含 policy snapshot
✅ /agent/sandbox/policy 返回外部 policy

## Runtime 效果

- Sandbox 规则不再内嵌在 executor 代码中
- Binary allow/block 规则由外部 policy 控制
- 执行记录包含 sandbox policy snapshot
- Output 由 policy 限制大小
- Environment 由 allowlist 缩小

## 注意事项

这仍然是本地进程 sandbox，不是 VM/container 级隔离。

## 下一步

C25-C8: Multi-Agent Runtime (协作模式、消息传递、状态隔离)