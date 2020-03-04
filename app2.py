from flask import Flask, abort, jsonify, render_template,url_for, request,send_from_directory,redirect
import numpy as np
import pandas as pd
import requests
import joblib

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home1.html')


@app.route('/prediction', methods=['GET','POST'])
def predict():
    if request.method == 'POST':
        input = request.form
        area = input['hub']
        if area == "0":
            areastr = 'Jakarta'
        elif area == "1":
            areastr = 'Indonesia Timur'
        elif area == "2":
            areastr = "Sumatra"
        elif area == "3":
            areastr = "Jawa Tengah & Timur"
        else :
            areastr = "Jawa Barat" 
        SellableRoom = float(input['SRNs'])
        # Gross_Value = int(input['GMV'])
        Occ = float(input['OCC'])
        # OTA = input['OTA']
        # App = input['App']
        # Walk_In = input['Walk_In']
        # Web = input['Web']
        # MM = input['MM']
        # Direct = input['Direct']
        # Others = input['Rest']
        Arr = int(input['ARR'])
        # Revpar = int(input['Revpar'])
        # Cancellations = input['Cancellations']
        # No_Shows = input['No_Shows']
        # GTR = input['GTR']
        # NTR = input['NTR']
        # MGL = input['MGL']



        prediksi = [[Occ,Arr,SellableRoom]]
        results = round(model.predict(prediksi)[0],2)
        strResult = f"{(results)}""% is the minimum recommended Gross Take Rate"
        return render_template('pred.html',SellableRoom=SellableRoom,Occupancy=Occ,AvgRoomRate=Arr,area=areastr,results=strResult)
@app.route('/NotFound')
def notFound():
    return render_template('/error.html')
#--------------------------------------------------------
if __name__ == '__main__':
    model = joblib.load('model_linear')
    app.run(debug=True, port=5000)