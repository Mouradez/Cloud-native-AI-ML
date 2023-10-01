from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

with open('C:/Users/21261/Desktop/Master 2/Devops and MLops/Project/model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():


    features = request.form.to_dict()
    features = list(features.values())
    features = list(map(float, features))
    print(features)
    final_features = np.array(features).reshape(1,13)
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)

    return render_template('index.html', prediction=' $ {}'.format(output))

if __name__ == "__main__":
    app.run(debug=True)

