from flask import Flask
app = Flask(__name__)
@app.route('/')
def home():
    return "<marquee><h1>Hello World!</h1></marquee>"
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
