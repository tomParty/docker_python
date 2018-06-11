from flask import Flask
from flask_restful import Api


try:
    print("Hello")
    import socket
    import ptvsd
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.close()
    ptvsd.enable_attach(secret=None,address=('0.0.0.0',5050))
    print('ptvsd is started')
except:
    print("NOT WORKING")
# ptvsd.wait_for_attach()
print('hello')
app = Flask(__name__)

@app.route("/")
def home():
    name = "Yama"
    return "Hello, " + name


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3000, debug=True)