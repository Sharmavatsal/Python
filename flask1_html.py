from flask import Flask, send_file #file content
import os

app = Flask(__name__)

file_path=r'F:\sem5\hlo.html'
@app.route('/')
def server_html():
    return send_file(file_path)


if __name__ == '__main__':
    app.run(debug=True,use_reloader=False,port=3000)

# type 127.0.0.1:3000 in url after running this code