from flask import Flask

app = Flask('__name__')


@app.route('/')
def hello():
    return 'Hello World from Flask!'


app.run('127.0.0.1', 8080)
