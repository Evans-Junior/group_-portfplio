from flask import Flask, render_template

app = Flask(__name__)

# Home page route
@app.route('/')
def godfred():
    return render_template('godfred_page.html')

if __name__ == '__main__':
    app.run(debug=True)
