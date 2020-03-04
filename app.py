from flask import Flask, abort, jsonify, render_template,url_for, request,send_from_directory,redirect
import numpy as np
import pandas as pd
import requests
import joblib

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


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
        # SellableRoom = input['SRNs']
        # Gross_Value = int(input['GMV'])
        # Occ = input['OCC']
        OTA = input['OTA']
        App = input['App']
        # Walk_In = input['Walk_In']
        # Web = input['Web']
        MM = input['MM']
        # Direct = input['Direct']
        # Others = input['Rest']
        # Arr = int(input['ARR'])
        # Revpar = int(input['Revpar'])
        Cancellations = input['Cancellations']
        No_Shows = input['No_Shows']
        GTR = input['GTR']
        # NTR = input['NTR']
        # MGL = input['MGL']

     


        prediksi = [[GTR,OTA,Cancellations,MM,No_Shows,App ]]
        results = model.predict(prediksi)[0]
        

        if results == 1:
            strResult = 'There are Property in this Hub might be not profitable'
            resultProba = round(model.predict_proba(prediksi)[0][1] * 100,2)
        elif results == 0:
            strResult = 'Property in this Hub is still Profitable'
            resultProba = round(model.predict_proba(prediksi)[0][0] * 100,2)
        # return render_template('prediction.html', SRN = SellableRoom, GMV = Gross_Value, Occupancy = Occ, OTABooking = OTA,
        # AppBooking = App, WalkIn = Walk_In, WebBooking = Web, DirectBooking = Direct, others = Others, AvgRoomRate = Arr,
        # RevenueperNight = Revpar, cancellations = Cancellations, no_shows = No_Shows, Gross_Rate = GTR, Net_Rate = NTR, result = strResult, area=areastr, probe=resultProba)
        return render_template('prediction.html', Gross_Rate=GTR, OTABooking=OTA,cancellations=Cancellations,MM=MM,No_Shows=No_Shows,AppBooking=App,area=areastr,result=strResult,probe=resultProba)

@app.route('/NotFound')
def notFound():
    return render_template('/error.html')
#--------------------------------------------------------
if __name__ == '__main__':
    model = joblib.load('model_tree')

    app.run(debug=True, port=5000)