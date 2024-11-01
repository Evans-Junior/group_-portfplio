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

if __name__ == '__main__':
    app.run(debug=True)
