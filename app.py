from flask import Flask, render_template, request
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    # 1. Handle upload
    file = request.files['bill']
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)

    # 2. Extract + Analyze
    from utils.extract import extract_data
    from utils.analyze import analyze_data

    bill_data = extract_data(filepath)
    result, chart_path = analyze_data(bill_data)

    return render_template('result.html', result=result, chart=chart_path)

if __name__ == '__main__':
    app.run(debug=True)
