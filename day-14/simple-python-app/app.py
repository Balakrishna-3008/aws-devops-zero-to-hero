from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, user!,my name is bala'

if __name__ == '__main__':
    app.run()

