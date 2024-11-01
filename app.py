import os
import yaml
from flask import Flask, render_template

app = Flask(__name__)

# Load configuration from YAML file
def load_config():
    with open("config.yaml", 'r') as file:
        config = yaml.safe_load(file)
    return config

config = load_config()
app.config.update(config['app'])

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
    return render_template('project4.html')

if __name__ == "__main__":
    app.run(debug=app.config['debug'])
