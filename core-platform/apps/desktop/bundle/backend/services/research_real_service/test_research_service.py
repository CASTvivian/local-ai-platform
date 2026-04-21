#!/usr/bin/env python3
"""
Research Real Service 测试脚本
"""
import requests
import json
import time

SERVICE_URL = "http://127.0.0.1:18098"

def test_health():
    """测试健康检查端点"""
    print("\n[1/4] 测试健康检查...")
    try:
        r = requests.get(f"{SERVICE_URL}/health", timeout=5)
        print(f"状态码: {r.status_code}")
        print(f"响应: {r.json()}")
        return True
    except Exception as e:
        print(f"❌ 失败: {e}")
        return False

def test_search():
    """测试搜索功能"""
    print("\n[2/4] 测试搜索功能...")
    try:
        payload = {
            "query": "人工智能最新进展",
            "limit": 3
        }
        r = requests.post(f"{SERVICE_URL}/search", json=payload, timeout=60)
        print(f"状态码: {r.status_code}")
        result = r.json()
        print(f"找到 {len(result.get('results', []))} 条结果")
        if result.get('results'):
            print(f"示例结果: {result['results'][0].get('title', 'N/A')}")
        return True
    except Exception as e:
        print(f"❌ 失败: {e}")
        return False

def test_news_summary():
    """测试新闻摘要功能"""
    print("\n[3/4] 测试新闻摘要功能...")
    try:
        # 使用一个常见的新闻网站URL
        payload = {
            "url": "https://news.sina.com.cn/",
            "limit": 5
        }
        r = requests.post(f"{SERVICE_URL}/news_summary", json=payload, timeout=120)
        print(f"状态码: {r.status_code}")
        result = r.json()
        print(f"摘要文件: {result.get('summary_file', 'N/A')}")
        print(f"新闻条数: {result.get('news_count', 0)}")
        return True
    except Exception as e:
        print(f"❌ 失败: {e}")
        return False

def test_stock_report():
    """测试股票研报功能"""
    print("\n[4/4] 测试股票研报功能...")
    try:
        payload = {
            "query": "茅台集团 2024年业绩分析",
            "limit": 3
        }
        r = requests.post(f"{SERVICE_URL}/stock_report", json=payload, timeout=120)
        print(f"状态码: {r.status_code}")
        result = r.json()
        print(f"研报文件: {result.get('report_file', 'N/A')}")
        print(f"搜索结果数: {result.get('search_count', 0)}")
        return True
    except Exception as e:
        print(f"❌ 失败: {e}")
        return False

def main():
    print("=" * 60)
    print("Research Real Service 测试")
    print("=" * 60)
    
    results = []
    
    # 等待服务启动
    print("\n等待服务启动...")
    time.sleep(3)
    
    results.append(("健康检查", test_health()))
    results.append(("搜索功能", test_search()))
    results.append(("新闻摘要", test_news_summary()))
    results.append(("股票研报", test_stock_report()))
    
    # 总结
    print("\n" + "=" * 60)
    print("测试总结")
    print("=" * 60)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for name, result in results:
        status = "✓ 通过" if result else "✗ 失败"
        print(f"{name}: {status}")
    
    print(f"\n总计: {passed}/{total} 通过")
    
    if passed == total:
        print("\n🎉 所有测试通过！")
        return 0
    else:
        print(f"\n⚠️  {total - passed} 个测试失败")
        return 1

if __name__ == "__main__":
    exit(main())
