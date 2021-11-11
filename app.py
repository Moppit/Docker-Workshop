from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1>CUWIC Docker Workshop</h1><p>Hi, my name is [...]</p>'

if __name__ == "__main__":
    app.run(debug=True)