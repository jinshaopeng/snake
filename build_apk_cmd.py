#!/usr/bin/env python3
"""
尝试使用命令行工具构建APK
"""

import os
import sys
import subprocess
from pathlib import Path

print("=" * 60)
print("尝试命令行构建APK")
print("=" * 60)

# 检查当前环境
print("\n[1] 检查环境...")

# 检查Java
java_ok = False
try:
    result = subprocess.run(["java", "-version"], capture_output=True, text=True)
    print(f"    Java: OK - {result.stderr.splitlines()[0]}")
    java_ok = True
except:
    print("    Java: 未找到")

# 检查Android SDK
android_home = os.environ.get("ANDROID_HOME", "")
android_sdk_root = os.environ.get("ANDROID_SDK_ROOT", "")

sdk_found = False
sdk_paths = [
    android_home,
    android_sdk_root,
    str(Path.home() / "AppData/Local/Android/Sdk"),
    str(Path.home() / "AppData/Local/Android/android-sdk"),
    "C:/Android/Sdk",
    "D:/Android/Sdk",
]

for sdk_path in sdk_paths:
    if sdk_path and Path(sdk_path).exists():
        print(f"    Android SDK: 找到 - {sdk_path}")
        sdk_found = True
        break

if not sdk_found:
    print("    Android SDK: 未找到")

print("\n[2] 检查可用方案...")

# 方案1: 如果有Android Studio项目
android_project = Path("android-project")
if android_project.exists():
    print("    Android Studio项目: 找到")
else:
    print("    Android Studio项目: 未找到")

# 输出总结
print("\n" + "=" * 60)
print("当前环境状态:")
print("=" * 60)

if not java_ok:
    print("\n❌ 需要安装 Java JDK")
    print("   下载: https://adoptium.net/")

if not sdk_found:
    print("\n❌ 需要安装 Android SDK")
    print("   方法1: 安装 Android Studio")
    print("          https://developer.android.com/studio")
    print("   方法2: 仅安装命令行工具")

print("\n" + "=" * 60)
print("可用的替代方案:")
print("=" * 60)
print("\n1. 使用在线工具（最简单，无需安装）")
print("   - https://webviewgold.com/")
print("   - https://www.appsgeyser.com/")

print("\n2. 使用 GitHub Actions")
print("   - 推送到GitHub后自动构建")

print("\n3. 安装 Android Studio")
print("   - 打开 android-project/ 目录")
print("   - Build -> Build APK(s)")

print("\n" + "=" * 60)

# 检查是否有Android Studio项目文件
if android_project.exists():
    print(f"\nAndroid项目位置: {android_project.absolute()}")
    print("\n你可以:")
    print("  1. 用 Android Studio 打开该目录")
    print("  2. 或者安装Android命令行工具后用Gradle构建")

# 先让用户可以玩游戏
index_html = Path("index.html")
if index_html.exists():
    print(f"\n✅ 游戏文件已就绪: {index_html.absolute()}")
    print("   双击它在浏览器里玩！")

print("\n" + "=" * 60)
