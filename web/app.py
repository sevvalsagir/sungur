from flask import Flask, render_template, request
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.extractor import ThreatExtractor

app = Flask(__name__)

extractor = ThreatExtractor()

@app.route('/', methods=['GET', 'POST'])
def index():
    threats = None
    if request.method == 'POST':
        text = request.form.get('text')
        if text:
            threats = extractor.extract_threats(text)
    return render_template('index.html', threats=threats)

if __name__ == '__main__':
    app.run(debug=True)
