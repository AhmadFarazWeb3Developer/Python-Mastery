import numpy as np
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('saved_models/linearRegression.pkl', 'rb'))

print(model)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    sat_score = float(request.form['sat'])
    prediction = model.predict([[sat_score]])
    output = prediction[0]
    return render_template('index.html', prediction_text=f'Predicted GPA is {output:.2f}')


if __name__ == "__main__":
    app.run(debug=True)
