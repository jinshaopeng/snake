#!/usr/bin/env python3
"""
打开APK生成网站
"""

from playwright.sync_api import sync_playwright
import webbrowser
import sys
from pathlib import Path

print("=" * 60)
print("正在为你打开APK生成网站...")
print("=" * 60)

# 首先检查文件
index_html = Path("index.html").absolute()
print(f"\n游戏文件位置: {index_html}")
if index_html.exists():
    print("文件状态: OK")
else:
    print("文件状态: 未找到！")
    sys.exit(1)

print("\n" + "=" * 60)
print("\n请按以下步骤操作：")
print("\n【方法 A: 最简单 - 在线生成")
print("-" * 60)
print("1. 打开网站后:")
print("   - 选择上传 index.html 文件")
print("   - 应用名填: 贪吃蛇")
print("   - 点击生成/下载")
print("")
print("【方法 B】 GitHub Actions")
print("-" * 60)
print("1. 在 GitHub 创建仓库")
print("2. 推送所有文件")
print("3. Actions -> Run workflow")
print("")
print("=" * 60)

# 尝试打开网站
urls = [
    "https://webviewgold.com/",
    "https://www.appsgeyser.com/create-app/website/"
]

print("\n正在尝试打开浏览器...")
for url in urls:
    try:
        webbrowser.open(url)
        print(f"已打开: {url}")
        break
    except:
        continue

print("\n" + "=" * 60)
print("现在你可以:")
print("  1. 在打开的网站中上传 index.html")
print("  2. 或者先双击 index.html 玩游戏")
print("=" * 60)
