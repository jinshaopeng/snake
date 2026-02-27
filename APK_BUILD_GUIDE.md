# APK 打包完整指南

由于本地环境没有安装完整的Android构建工具链，这里提供三种方法来打包APK：

## 方法一：使用在线构建工具（最简单，推荐）

### 1. WebViewGold
访问：https://webviewgold.com/
- 上传 `index.html` 文件
- 填写应用名称：贪吃蛇
- 下载生成的APK

### 2. AppsGeyser
访问：https://www.appsgeyser.com/
- 选择 "Website" 模板
- 上传HTML文件或使用在线HTML编辑器
- 生成APK

### 3. Gonative.io
访问：https://gonative.io/
- 提供HTML文件
- 配置应用设置
- 下载APK

## 方法二：使用PhoneGap Build（Adobe）

1. 访问：https://build.phonegap.com/
2. 注册账号
3. 将项目打包成zip（包含index.html和config.xml）
4. 上传zip文件
5. 等待构建完成后下载APK

### 准备zip文件结构：
```
snake.zip/
├── config.xml
└── www/
    └── index.html
```

## 方法三：本地完整构建（需要安装工具）

### 前置要求

1. **安装 Node.js**
   - 下载：https://nodejs.org/
   - 安装LTS版本

2. **安装 Java JDK**
   - 下载：https://adoptium.net/
   - 安装JDK 11或17
   - 设置环境变量 `JAVA_HOME`

3. **安装 Android Studio**
   - 下载：https://developer.android.com/studio
   - 安装后打开SDK Manager
   - 安装 Android SDK Platform 30+
   - 安装 Android SDK Build-Tools
   - 安装 Android SDK Platform-Tools
   - 设置环境变量 `ANDROID_HOME`

### 使用 Cordova 构建步骤

```bash
# 1. 安装 Cordova
npm install -g cordova

# 2. 创建项目
cordova create snake-app com.example.snake SnakeGame
cd snake-app

# 3. 添加 Android 平台
cordova platform add android

# 4. 复制文件
# 将 cordova-template/www/index.html 复制到 snake-app/www/
# 将 cordova-template/config.xml 复制到 snake-app/

# 5. 构建 APK
cordova build android

# APK 位置：platforms/android/app/build/outputs/apk/debug/app-debug.apk
```

### 在 Windows 上使用我们的脚本

双击运行 `build-apk.bat`

## 方法四：使用 Capacitor

```bash
# 1. 初始化项目
npm init -y
npm install @capacitor/core @capacitor/cli @capacitor/android

# 2. 初始化 Capacitor
npx cap init SnakeGame com.example.snake

# 3. 添加 Android 平台
npx cap add android

# 4. 复制 www 文件
# 将 index.html 放到 www/ 目录

# 5. 同步并打开
npx cap sync
npx cap open android

# 6. 在 Android Studio 中构建 APK
# Build -> Build Bundle(s) / APK(s) -> Build APK(s)
```

## 测试APK

构建完成后，可以：
1. 将APK传输到Android手机安装
2. 使用Android模拟器测试
3. 使用在线APK安装器测试

## 常见问题

**Q: 构建提示SDK未找到？**
A: 确保安装了Android Studio并正确设置了ANDROID_HOME环境变量

**Q: Java版本不匹配？**
A: 使用JDK 11或17，不要使用太新的版本

**Q: 最简单的方法是什么？**
A: 使用WebViewGold或AppsGeyser等在线工具，无需安装任何东西
