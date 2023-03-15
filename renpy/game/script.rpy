define e = Character("派蒙")
define config.gl2 = True
image e = Live2D("paimeng", top=0.2, base=0.9, height=0.7, loop=True, seamless=True, _live2d_fade=True)
define u = Character("User")

label start:
    python:
        r = ""
    jump chat

label chat:
    scene 1
    show e 身体不太舒服
    python:
        import socket
        import threading
        i = 0
        status = 1
        global status
        if status == 1:
            your_text = renpy.input('',length=100)
        prompt = str(your_text)
        def send_txt():
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect(('127.0.0.1', 12345))
            s.send(prompt.encode())
            s.recv(1024).decode()
            status = 2
        thread = threading.Thread(target=send_txt())
        thread.start()
    if (status == 2):
        show e 派蒙一直支持着你哦
        python:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect(('127.0.0.1', 12345))
            s.send('发送空串用于占位'.encode())
            r = s.recv(1024).decode()
            status = 3
    if (status == 3):
        show e 知道你要说什么 吃到好吃的 陪你旅行到现在 这么说来你就是我的妹妹了 派蒙一直支持着你哦 难道你在外面还有其他的应急食品吗 嗯 知道你要说什么 吃到好吃的 咕嘟咕嘟 好无聊
        voice "audio/output.ogg"
        e "[r]"
        voice sustain
        jump chat