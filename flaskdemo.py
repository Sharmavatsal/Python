from flask import Flask
app = Flask('My_app')
@app.route('/')

def hello_world():
    return 'Hello Guys'

if __name__ == '__main__':
    app.run(debug=True,use_reloader=False,port=5000)
    
# open chrome and write 127.0.0.1:5000 in url