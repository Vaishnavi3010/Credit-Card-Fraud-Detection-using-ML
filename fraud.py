from flask import Flask, request, render_template
import numpy as np
import pickle

app = Flask(__name__)

# Load the logistic regression model
with open('logistic_regression_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    input_features = [float(x) for x in request.form.values()]
    features = np.array(input_features).reshape(1, -1)
    prediction = model.predict(features)
    
    if prediction[0] == 0:
        result = "legitimate transaction"
    else:
        result = "fraudulent transaction"
    
    return render_template('index.html', prediction_text=f'The transaction is predicted to be a {result}')

if __name__ == "__main__":
    app.run(debug=True)
