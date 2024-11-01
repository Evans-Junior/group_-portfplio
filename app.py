<<<<<<< HEAD
# app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    print("Welcome to Our Portfolio")
    return "Welcome to Our Portfolio \nHome Page Find our Portfolio individualy here!"
=======
from flask import Flask, render_template

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('base.html')  # Link to the team’s landing page or index

# Godfred's page route
@app.route('/godfred')
def godfred():
    return render_template('godfred_page.html')
>>>>>>> 777e72dd48460b2e1d9e87c0a6fa60cf44711d38

if __name__ == '__main__':
    app.run(debug=True)
