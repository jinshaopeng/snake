#!/usr/bin/env python3
"""
贪吃蛇APK生成脚本
使用在线工具自动生成APK
"""

import os
import time
import zipfile
from pathlib import Path

print("=" * 50)
print("贪吃蛇 APK 生成方案")
print("=" * 50)
print()

# 检查当前目录
current_dir = Path(__file__).parent
index_html = current_dir / "index.html"

if not index_html.exists():
    print(f"[错误] 找不到 index.html")
    exit(1)

print(f"[OK] 找到游戏文件: {index_html}")
print()

# 方案1: 创建一个准备上传的ZIP包
print("方案1: 创建上传用的ZIP文件")
zip_path = current_dir / "snake_game_for_apk.zip"
with zipfile.ZipFile(zip_path, 'w') as zf:
    zf.write(index_html, "index.html")
print(f"[OK] 已创建: {zip_path}")
print()

# 方案2: 为GitHub Actions准备
print("方案2: GitHub Actions 自动构建")
print("请按以下步骤操作：")
print()
print("1. 在 GitHub 创建一个新仓库")
print("2. 在本地运行以下命令：")
print()
print("   git init")
print("   git add .")
print("   git commit -m 'Initial commit'")
print("   git branch -M main")
print("   git remote add origin https://github.com/你的用户名/仓库名.git")
print("   git push -u origin main")
print()
print("3. 在 GitHub 仓库页面:")
print("   - 点击 'Actions' 标签")
print("   - 选择 'Build Snake Game APK'")
print("   - 点击 'Run workflow'")
print("   - 等待 5-10 分钟")
print()
print("4. 构建完成后:")
print("   - 在工作流页面底部找到 'Artifacts'")
print("   - 下载 'SnakeGame-APK.zip'")
print("   - 解压得到 APK 文件！")
print()

# 方案3: 最简单的方法
print("=" * 50)
print("方案3: 最简单 - 使用在线工具（推荐）")
print("=" * 50)
print()
print("请访问以下任一网站，上传 index.html 文件：")
print()
print("1. https://webviewgold.com/")
print("2. https://www.appsgeyser.com/create-app/website/")
print("3. https://gonative.io/")
print()
print("步骤：")
print("  1. 打开网站")
print("  2. 上传 index.html 文件")
print("  3. 应用名填: 贪吃蛇")
print("  4. 点击生成/下载")
print("  5. 几分钟后就能得到 APK！")
print()

print("=" * 50)
print("另外：你现在就可以双击 index.html 在浏览器里玩游戏！")
print("=" * 50)
