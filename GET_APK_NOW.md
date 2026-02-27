# 立即获取APK！（三种方法）

## 🔥 方法一：在线一键生成（推荐，5分钟搞定）

### 步骤：

1. **访问这个网站：** https://webviewgold.com/
   - 或备用：https://www.appsgeyser.com/create-app/website/

2. **上传 index.html 文件**
   - 选择本目录下的 `index.html` 文件上传

3. **填写应用信息：**
   - 应用名称：`贪吃蛇`
   - 包名：`com.example.snake`
   - 图标：可以用默认的，或者自己上传一个图片

4. **点击生成/下载**
   - 等待几分钟，直接下载APK！

---

## 🚀 方法二：使用 GitHub Actions（需要GitHub账号）

### 步骤：

1. **在 GitHub 上创建一个新仓库**

2. **将这些文件推送到仓库：**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/你的用户名/你的仓库名.git
   git push -u origin main
   ```

3. **在 GitHub 上触发构建：**
   - 打开你的仓库
   - 点击 `Actions` 标签
   - 点击 `Build Snake Game APK` 工作流
   - 点击 `Run workflow` 按钮
   - 等待约5-10分钟

4. **下载APK：**
   - 构建完成后，在工作流页面底部找到 `Artifacts`
   - 下载 `SnakeGame-APK.zip`
   - 解压得到 APK 文件！

---

## 💻 方法三：我帮你用 Python 生成一个简单安装包

等等，其实我有个更简单的想法——让我创建一个可以在电脑上玩的版本，同时给你准备好APK构建文件！

**先试试 HTML 版本：**
直接双击 `index.html` 在浏览器里玩！

---

## 📱 测试APK

拿到APK后：
1. 传到手机
2. 安装（需要允许"未知来源"）
3. 开始玩！

---

## ⚡ 快速测试 - 先玩起来！

现在就可以打开 `index.html` 在浏览器里试玩游戏！
