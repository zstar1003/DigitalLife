import json
import socket
import openai
from VITS import vits_infer


def ask_gpt(msg):
    openai.api_key = '自己的key'
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": msg}
        ]
    )
    result = json.loads(str(completion.choices[0].message))
    return result['content']


if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('127.0.0.1', 12345))
    s.listen(5)
    print("已启动，等待连接中")

    epoch = 0
    respond_data = ""
    while True:
        sock, addr = s.accept()
        client_data = sock.recv(400000).decode()
        print(client_data)
        if epoch % 2 == 0:
            respond_data = ask_gpt(client_data)
            vits_infer.infer(respond_data)
        sock.send(respond_data.encode())
        epoch += 1