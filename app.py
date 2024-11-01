# app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    print("Welcome to Our Portfolio")
    return "Welcome to Our Portfolio \nHome Page Find our Portfolio individualy here!"

if __name__ == '__main__':
    app.run(debug=True)
