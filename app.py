from flask import Flask, request, render_template, jsonify
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'
    if file and file.filename.endswith('.csv'):
        df = pd.read_csv(file)
        # Assuming the CSV has the format suitable for analysis
        # Here we are simulating a basic model training and evaluation
        # This part should be replaced with your actual model and analysis
        
        # Example with Iris dataset for demonstration
        iris = load_iris()
        X = iris.data
        y = iris.target
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
        clf = RandomForestClassifier(n_estimators=10)
        clf.fit(X_train, y_train)
        y_pred = clf.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        
        return jsonify({'accuracy': accuracy})

    return 'Invalid file format. Please upload a CSV file.'

if __name__ == '__main__':
    app.run(debug=True)
