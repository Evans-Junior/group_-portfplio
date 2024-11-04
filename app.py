from flask import Flask, render_template

app = Flask(__name__)

<<<<<<< HEAD
# Home page route
@app.route('/')
def godfred():
=======
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/evans')
def evans_page():
    return render_template('evans_page.html')

@app.route('/godfred')
def godfred_page():
>>>>>>> 307358e1ddb5ae70c1e22e259893c38e605e34e2
    return render_template('godfred_page.html')

@app.route('/elizabeth')
def elizabeth_page():
    return render_template('project4.html')

@app.route('/faith')
def faith_page():
    return render_template('FaithInusah-page.html')

if __name__ == "__main__":
    app.run()
