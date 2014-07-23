来源和原理来自于这个帖子 [http://testerhome.com/topics/1050](http://testerhome.com/topics/1050 "来源和原理")

### 工具的原理

1. 在手机端调用robotium框架获取当前界面的所有View，存入本地xml文件
2. PC运行界面程序，用adb拉取xml文件并分析，然后界面展示出来

### 目前存在的不足

1. 界面各种细节需要调整 （重构界面）
2. 获取的界面信息实际是一个list，很不利于查找 (获取成tree，同时展示成tree)
3. 只展示了截图，当点击具体一个view时，没有在截图上标明 (选择一个特定的view时，在截图上绘图)
4. 需要导入Robotium包，操作略麻烦 (直接对Instrumentation封装)
5. 界面程序是python写的，但是环境问题一直没有打包exe成功

### 优点

1. 不需要root
2. 开发如果使用的自定义的组件，可以显示出组件名（在uiautomatorviewer里边只会显示基类的类名，hierarchyviewer未尝试）
3. 几乎100%可以识别出id
4. 支持将界面信息存储在PC本地，并且离线直接读取本地文件
5. 手机端提供三个调用入口，方便实现通过脚本自动获取所有所需界面的信息

### 使用方法

1. 新建一个Android测试工程，填好各项配置
2. 导入robotium框架和getinfo.jar

#### robotium地址
[http://www.robotium.cn/download](http://www.robotium.cn/download "robotium地址")

**请保证该处打钩：**

![提示](imgs/step1.png "提示")

