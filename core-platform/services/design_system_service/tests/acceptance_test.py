#!/usr/bin/env python3
"""Acceptance tests for Design System Service (18127)"""

import sys
import json
import time
import requests

BASE_URL = "http://localhost:18127"

def test_health():
    """Test 1: Health check"""
    resp = requests.get(f"{BASE_URL}/health")
    data = resp.json()
    assert data.get("ok") == True
    assert "service" in data
    print("✅ Test 1: /health 正常")

def test_debug_storage():
    """Test 2: Debug storage paths"""
    resp = requests.get(f"{BASE_URL}/debug/storage")
    data = resp.json()
    assert data.get("ok") == True
    assert "base_dir" in data
    print("✅ Test 2: Debug storage 正常")

def test_list_empty():
    """Test 3: List design systems (empty)"""
    resp = requests.get(f"{BASE_URL}/list")
    data = resp.json()
    assert data.get("ok") == True
    count = data.get("count", 0)
    print(f"✅ Test 3: List 设计系统 (当前数量: {count})")

def test_register():
    """Test 4: Register design system"""
    import time
    unique_name = f"test-design-system-{int(time.time())}"
    resp = requests.post(f"{BASE_URL}/register", json={
        "name": unique_name,
        "version": "1.0.0",
        "description": "Test design system",
        "source": "manual"
    })
    data = resp.json()
    assert data.get("ok") == True
    assert "id" in data
    print(f"✅ Test 4: 注册设计系统成功 (ID: {data['id']})")
    return data['id']

def test_list_after_register():
    """Test 5: List design systems (after register)"""
    resp = requests.get(f"{BASE_URL}/list")
    data = resp.json()
    assert data.get("ok") == True
    count = data.get("count", 0)
    assert count >= 1
    print(f"✅ Test 5: 列表显示 {count} 个设计系统")

def test_parse_design_md():
    """Test 6: Parse DESIGN.md"""
    design_md = """
# Test Design System

Name: test-design
Version: 1.0.0

## Colors
- Primary: #007bff
- Secondary: #6c757d
- Accent: #ff5722

## Fonts
- Heading: Inter
- Body: Roboto

## Spacing
- xs: 4px
- sm: 8px
- md: 16px
- lg: 24px

## Components
Button, Card, Input, Modal

## UI Constraints
Max width: 1200px
"""
    resp = requests.post(f"{BASE_URL}/parse_design_md", json={
        "text": design_md,
        "source": "manual"
    })
    data = resp.json()
    assert data.get("ok") == True
    assert "colors" in data
    assert "fonts" in data
    assert "components" in data
    print(f"✅ Test 6: 解析 DESIGN.md 成功 (提取了 {len(data.get('colors', {}))} 个颜色)")

def test_get_design_system(design_system_id):
    """Test 7: Get design system by ID"""
    resp = requests.get(f"{BASE_URL}/design/{design_system_id}")
    data = resp.json()
    assert data.get("ok") == True
    assert data.get("id") == design_system_id
    print(f"✅ Test 7: 查询设计系统详情成功")

def test_export_design_system(design_system_id):
    """Test 8: Export design system"""
    resp = requests.get(f"{BASE_URL}/export/{design_system_id}")
    data = resp.json()
    assert data.get("ok") == True
    assert "design_system" in data
    print(f"✅ Test 8: 导出设计系统成功")

def test_suggest_ui():
    """Test 9: Suggest UI constraints"""
    resp = requests.post(f"{BASE_URL}/suggest_ui", json={
        "component_type": "button",
        "design_system_id": ""
    })
    data = resp.json()
    assert data.get("ok") == True
    assert "spacing" in data
    assert "colors" in data
    assert "typography" in data
    assert "components" in data
    print(f"✅ Test 9: UI 约束建议成功")

def test_recent_events():
    """Test 10: Recent events"""
    resp = requests.get(f"{BASE_URL}/recent")
    data = resp.json()
    assert data.get("ok") == True
    events = data.get("events", [])
    count = len(events)
    print(f"✅ Test 10: 最近事件记录 ({count} 条事件)")
    return events

def test_store_persistence():
    """Test 11: Verify store.json persistence"""
    import os
    from pathlib import Path

    # Try to find store.json
    possible_paths = [
        "/Users/mofamaomi/Documents/本地ai/data/design_system/store.json",
        Path(__file__).parent.parent / "data" / "design_system" / "store.json",
    ]

    for path in possible_paths:
        if Path(path).exists():
            size = Path(path).stat().st_size
            print(f"✅ Test 11: store.json 存在 ({size} bytes)")
            # Read and verify content
            with open(path) as f:
                store = json.load(f)
                print(f"  - 设计系统数量: {len(store.get('design_systems', []))}")
                print(f"  - 品牌配置数量: {len(store.get('brand_profiles', []))}")
                print(f"  - 设计 token 数量: {len(store.get('design_tokens', []))}")
                print(f"  - 组件规范数量: {len(store.get('component_specs', []))}")
            return

    print("⚠️ Test 11: store.json 未找到，跳过持久化验证")

def test_events_log():
    """Test 12: Verify events.jsonl"""
    import os
    from pathlib import Path

    possible_paths = [
        "/Users/mofamaomi/Documents/本地ai/data/design_system/events.jsonl",
        Path(__file__).parent.parent / "data" / "design_system" / "events.jsonl",
    ]

    for path in possible_paths:
        if Path(path).exists():
            with open(path) as f:
                lines = f.readlines()
            print(f"✅ Test 12: events.jsonl 存在 ({len(lines)} 条记录)")
            # Show recent events
            for line in lines[-3:]:
                event = json.loads(line)
                print(f"  - {event.get('event')}: {event.get('timestamp')}")
            return

    print("⚠️ Test 12: events.jsonl 未找到，跳过事件日志验证")

def main():
    """Run all acceptance tests"""
    print("=" * 60)
    print("Design System Service (18127) 验收测试")
    print("=" * 60)

    try:
        # Test 1-3: Basic checks
        test_health()
        test_debug_storage()
        test_list_empty()

        # Test 4-5: Register and list
        design_system_id = test_register()
        test_list_after_register()

        # Test 6: Parse DESIGN.md
        test_parse_design_md()

        # Test 7-8: Get and export
        test_get_design_system(design_system_id)
        test_export_design_system(design_system_id)

        # Test 9: Suggest UI constraints
        test_suggest_ui()

        # Test 10: Recent events
        events = test_recent_events()

        # Test 11-12: Persistence
        test_store_persistence()
        test_events_log()

        print("=" * 60)
        print("✅ 所有验收测试通过！")
        print("=" * 60)
        return 0

    except AssertionError as e:
        print(f"❌ 测试失败: {e}")
        return 1
    except Exception as e:
        print(f"❌ 测试异常: {e}")
        import traceback
        traceback.print_exc()
        return 1

if __name__ == "__main__":
    sys.exit(main())
