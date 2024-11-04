from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/evans')
def evans_page():
    return render_template('evans_page.html')

@app.route('/godfred')
def godfred_page():
    return render_template('godfred_page.html')

@app.route('/elizabeth')
def elizabeth_page():
    return render_template('elizabeth.html')

if __name__ == "__main__":
    app.run()
