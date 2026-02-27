# 贪吃蛇游戏

这是一个贪吃蛇游戏项目，包含两个版本：
1. Python + Pygame 版本（桌面版）
2. HTML5 + JavaScript 版本（可打包为APK）

## 文件说明

- `snake.py` - Python + Pygame 版本的贪吃蛇游戏
- `index.html` - HTML5 版本的贪吃蛇游戏（支持移动端触摸控制）
- `requirements.txt` - Python依赖
- `README.md` - 本说明文件

## 运行方法

### Python版本

```bash
# 安装依赖
pip install -r requirements.txt

# 运行游戏
python snake.py
```

控制：方向键控制移动

### HTML5版本

直接在浏览器中打开 `index.html` 即可

控制：
- 电脑：方向键 或 WASD
- 手机：点击屏幕下方的方向按钮

## 打包成APK的方法

### 方法一：使用Cordova（推荐）

#### 前置要求
1. 安装 Node.js: https://nodejs.org/
2. 安装 Java JDK 8 或更高版本
3. 安装 Android Studio 和 Android SDK
4. 设置环境变量：JAVA_HOME, ANDROID_HOME

#### 步骤

```bash
# 1. 安装 Cordova
npm install -g cordova

# 2. 创建 Cordova 项目
cordova create snake-app com.example.snake SnakeGame
cd snake-app

# 3. 添加 Android 平台
cordova platform add android

# 4. 将 index.html 复制到 www/ 目录下
# 替换 www/index.html 为我们的游戏文件

# 5. 配置 config.xml (可选，设置全屏、方向等)

# 6. 构建 APK
cordova build android

# APK 位置: platforms/android/app/build/outputs/apk/debug/app-debug.apk
```

### 方法二：使用 WebView Gold（在线工具）

1. 访问 https://webviewgold.com/
2. 上传 index.html 文件
3. 填写应用信息
4. 下载生成的 APK

### 方法三：使用 Python-for-android（Python版本）

```bash
# 安装 python-for-android
pip install python-for-android

# 创建 APK
p4a apk --package=com.example.snake \
        --name="贪吃蛇" \
        --version=1.0 \
        --bootstrap=sdl2 \
        --requirements=python3,pygame \
        --blacklist-requirements=android \
        --orientation=landscape \
        --window \
        --entry-point=snake.py
```

### 方法四：使用 Capacitor

```bash
npm install -g @capacitor/cli
npm init -y
npm install @capacitor/core @capacitor/cli @capacitor/android
npx cap init SnakeGame com.example.snake
npx cap add android
# 复制 index.html 到 www/ 目录
npx cap sync
npx cap open android
# 在 Android Studio 中构建 APK
```

## config.xml 配置示例

```xml
<?xml version='1.0' encoding='utf-8'?>
<widget id="com.example.snake" version="1.0.0" xmlns="http://www.w3.org/ns/widgets">
    <name>贪吃蛇</name>
    <description>经典贪吃蛇游戏</description>
    <author email="dev@example.com">Developer</author>
    <content src="index.html" />
    <preference name="Orientation" value="portrait" />
    <preference name="Fullscreen" value="true" />
    <preference name="KeepRunning" value="true" />
</widget>
```
