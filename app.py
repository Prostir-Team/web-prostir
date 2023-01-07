from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def main():
    return "<h1>Hello World</h1>"

if __name__ == "__main__":
    app.run(port=50000, debug=True)