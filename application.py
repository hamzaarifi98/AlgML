from flask import Flask,jsonify, render_template,request
import pandas as pd
import numpy as np  
from sklearn.preprocessing import StandardScaler
import pickle


application = Flask(__name__)
app = application


## import ridge regressor and standard scaler pickle
with open('models/ridge.pkl','rb') as f:
    ridge = pickle.load(f)

with open('models/scaler.pkl','rb') as f:
    scaler = pickle.load(f) 




@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["GET","POST"])
def predict_datapoint():
    if request.method == "POST":
        Weather = float(request.form.get('Weather'))
        RH = float(request.form.get('RH'))
        WS = float(request.form.get('WS'))  
        Rain = float(request.form.get('Rain'))
        FFMC = float(request.form.get('FFMC'))
        DMC = float(request.form.get('DMC'))    
        ISI = float(request.form.get('ISI'))
        Classes = float(request.form.get('Classes'))
        Region = float(request.form.get('Region'))

         ## scale the data
         ## reshape the data and predict
         ## return the results to the home page
         ## return the results to the home page
         ## return the results to the home page

        new_data_scaled = scaler.transform([[Weather,RH,WS,Rain,FFMC,DMC,ISI,Classes,Region]])
        prediction = ridge.predict(new_data_scaled)
        return render_template("home.html", results=prediction[0])

    else:
        return render_template("home.html")


if __name__ == "__main__":
    app.run(debug=True)



