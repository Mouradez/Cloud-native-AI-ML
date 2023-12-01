from flask import Flask,jsonify,render_template,request
import numpy as np
import pickle
import pandas as pd

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

model = pickle.load(open("classifier_svm.pkl","rb"))

@app.route("/prediction",methods=["POST"])
def predict():
    float_features = [float(x) for x in request.form.values()]
    features = [np.array(float_features)]
    prediction = model.predict(features)
    if prediction[0] == 0:
        prediction = 'No, you dont have depression'
    else :
        prediction = 'Yes, you do have depression'
    return render_template("index.html",prediction_text = "Student Mental health prediction is :  {}".format(prediction))

if __name__ == "__main__":
    app.run(debug=True)