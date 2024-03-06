# 1.简介
这是一个关于hololens2的项目，实现在hololens2上截图并把图片传输到PC服务器端的功能
# 2.代码介绍
## 2.1client.cs
hololens2客户端代码，作为脚本直接挂载到camera即可。在unity上按UWP平台进行`build`,输出的`.sln`文件用VS2022打开，生成解决方案，部署到hololesn2运行.
## 2.2server.py
PC服务器端代码，其中`ip`地址需要根据本机的`ip`进行改变。部署好`python`环境后直接运行，等待服务器连接。。。