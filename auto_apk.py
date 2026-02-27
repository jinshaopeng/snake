#!/usr/bin/env python3
"""
尝试自动生成APK
"""

import sys
import time
from pathlib import Path

print("检查Playwright浏览器...")
try:
    from playwright.sync_api import sync_playwright
    print("Playwright已导入")
except ImportError:
    print("需要先安装Playwright浏览器")
    print("运行: playwright install chromium")
    sys.exit(1)

# 先让用户知道最简单的方案
print("\n" + "="*60)
print("由于APK生成需要复杂的在线验证，")
print("推荐使用以下最简单的方法：")
print("="*60)
print("\n方法1: 使用 WebViewGold (最简单)")
print("  1. 打开: https://webviewgold.com/")
print("  2. 上传 index.html")
print("  3. 应用名: 贪吃蛇")
print("  4. 下载APK！\n")

print("方法2: 使用 AppsGeyser")
print("  1. 打开: https://www.appsgeyser.com/create-app/website/")
print("  2. 选择 'HTML' 模式")
print("  3. 上传 index.html")
print("  4. 生成并下载APK\n")

print("="*60)
print("或者使用 GitHub Actions 自动构建:")
print("="*60)
print("\n1. 在 GitHub 创建新仓库")
print("2. 推送所有文件")
print("3. 点击 Actions -> Run workflow")
print("4. 等待5-10分钟下载APK\n")

# 检查文件
index_html = Path("index.html")
if index_html.exists():
    print(f"\n[OK] 游戏文件已准备: {index_html.absolute()}")
    print("你可以先双击它在浏览器里玩！\n")

print("="*60)

# 让我创建一个简单的APK项目说明
with open("APK快速获取.txt", "w", encoding="utf-8") as f:
    f.write("""
╔══════════════════════════════════════════════════════════════╗
║                    贪吃蛇 APK 快速获取指南                      ║
╠══════════════════════════════════════════════════════════════╣
║                                                                  ║
║  方案 A: 在线一键生成 (5分钟，推荐！)                          ║
║  ────────────────────────────────────────────────────────────  ║
║                                                                  ║
║  1. 打开网站: https://webviewgold.com/                         ║
║  2. 点击 "Select your website file"                             ║
║  3. 选择本目录下的 index.html 文件                              ║
║  4. App Name 填写: 贪吃蛇                                       ║
║  5. Package Name 填写: com.example.snake                        ║
║  6. 点击下载，稍等几分钟即可得到APK！                           ║
║                                                                  ║
║  备用网站:                                                       ║
║    - https://www.appsgeyser.com/create-app/website/            ║
║    - https://gonative.io/                                       ║
║                                                                  ║
╠══════════════════════════════════════════════════════════════╣
║                                                                  ║
║  方案 B: GitHub Actions 自动构建                                ║
║  ────────────────────────────────────────────────────────────  ║
║                                                                  ║
║  1. 在 GitHub.com 创建新仓库                                     ║
║  2. 在本地运行:                                                  ║
║     git init                                                    ║
║     git add .                                                    ║
║     git commit -m "Initial"                                     ║
║     git branch -M main                                          ║
║     git remote add origin https://github.com/你的用户名/仓库名   ║
║     git push -u origin main                                     ║
║  3. 打开 GitHub 仓库页面                                         ║
║  4. 点击 Actions → Build Snake Game APK → Run workflow         ║
║  5. 等待5-10分钟，下载 Artifacts 中的 APK                       ║
║                                                                  ║
╠══════════════════════════════════════════════════════════════╣
║                                                                  ║
║  先玩一下！                                                      ║
║  双击 index.html 在浏览器里直接玩游戏！                          ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════╝
    """.strip())

print("\n已创建 'APK快速获取.txt'，里面有详细步骤！")
print("\n现在你可以:")
print("  1. 先双击 index.html 玩游戏")
print("  2. 查看 'APK快速获取.txt' 获取APK")
