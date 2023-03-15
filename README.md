# <div align="center">DigitalLife</div>

<div align="center">

![派蒙](asset/paimon.jpg)

致力于给派蒙完整的一生


</div>


<div align="center">

<a href="https://github.com/zstar1003/Maze_Market"><img src="https://img.shields.io/badge/language-Python-orange.svg"></a>

</div>


# 项目演示

B站：[https://www.bilibili.com/video/BV1bY411z746](https://www.bilibili.com/video/BV1bY411z746)

# 项目使用
- 1.克隆项目
```c
git clone https://github.com/zstar1003/DigitalLife
```

- 2.安装依赖
```c
pip install -r requirements.txt
```

- 3.下载模型

下载派蒙的vits模型，放置在model文件夹下，重命名为`Paimon.pth`

下载连接：[https://pan.baidu.com/s/1aF6Q_rA5tBQv7YaU0jizuA?pwd=bya7](https://pan.baidu.com/s/1aF6Q_rA5tBQv7YaU0jizuA?pwd=bya7)

- 4.运行`test_gpt.py`，测试gpt3.5是否可用。

- 5.运行`main.py`，开启服务端，持续监听。

- 6.打开`renpy/Paimon.exe`，选择开始游戏，即可和派蒙对话了。

# 参考
本项目参考或使用了以下开源项目或模型：

[1] Vits派蒙模型：https://www.bilibili.com/video/BV16G4y1B7Ey

[2] live2d派蒙模型：https://www.bilibili.com/video/BV1pA411j78k

[3] live2d-chatgpt-vits：https://github.com/balmung08/live2d-chatgpt-vits

# 存在问题
目前仍存在的问题是在等待数据返回时，前端会出现卡顿，尽管使用了多线程方式，该方法仍未缓解。

预计可行的思路是借助Renpy的回滚机制，暂时懒得去维护了，有解决该问题的欢迎发起一个PR。

# 拓展
如果不需要前端显示，只需要GPT返回信息与音频，并嵌入到QQ群中，可以查看我的另一项目：[https://github.com/zstar1003/Qbot](https://github.com/zstar1003/Qbot)