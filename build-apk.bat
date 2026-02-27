@echo off
echo ========================================
echo 贪吃蛇 APK 构建脚本
echo ========================================
echo.

where node >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo [错误] 未找到 Node.js
    echo 请先从 https://nodejs.org/ 下载并安装 Node.js
    pause
    exit /b 1
)

where cordova >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo [信息] 正在安装 Cordova...
    call npm install -g cordova
)

if not exist "snake-game" (
    echo [信息] 创建 Cordova 项目...
    call cordova create snake-game com.example.snake SnakeGame
    if %ERRORLEVEL% NEQ 0 (
        echo [错误] 创建项目失败
        pause
        exit /b 1
    )
)

cd snake-game

echo [信息] 复制游戏文件...
xcopy /Y /E ..\cordova-template\* .\ >nul

if not exist "platforms\android" (
    echo [信息] 添加 Android 平台...
    call cordova platform add android
)

echo [信息] 构建 APK...
call cordova build android

if %ERRORLEVEL% EQU 0 (
    echo.
    echo ========================================
    echo [成功] APK 构建完成!
    echo ========================================
    echo APK 位置: snake-game\platforms\android\app\build\outputs\apk\debug\app-debug.apk
) else (
    echo.
    echo [错误] 构建失败，请检查是否安装了 Android SDK 和 Java JDK
)

cd ..
pause
