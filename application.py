from flask import Flask,request,jsonify,render_template
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

application = Flask(__name__)
app = application

ridge_model = pickle.load(open('models/ridge.pkl','rb'))
Standard_Scaler = pickle.load(open('models/scaler.pkl','rb'))

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/hello")
def hello():
    return "Hello Soham"

@app.route("/test")
def test():
    return "Server working"

if __name__=="__main__":
    app.run(host="0.0.0.0")
