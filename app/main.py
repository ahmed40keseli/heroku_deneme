from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "hello muslim..."
    # return "<hi>hello muslim...</hi>"
