import pandas as pd
from pymongo import MongoClient , errors, ReturnDocument
from math import floor
from os import getcwd
from os.path import join
from json import loads, dumps, dump
from datetime import timedelta, datetime, timezone         
from urllib import parse
from urllib.request import  urlopen 
from bson.objectid import ObjectId  

# Connect to the MongoDB cluster
client = MongoClient("mongodb://localhost:27017")  # Replace with your MongoDB connection string

# Access the database and collection
db = client["COMP3901"]  # Replace with your database name
collection = db["crops"]           # Access the "crops" collection

rice = []
maize = []
chickpea = []
kidneybeans = []
pigeonpeas = []
mothbeans = []
mungbean = []
blackgram = []
lentil = [] 
pomegranate = []
banana = []
mango = []
grapes = []
watermelon = []
muskmelon = []
apple = []
orange = []
papaya = []
coconut = []
cotton = []
jute = []
coffee = []
crops = []

# Replace with the actual filename
df = pd.read_csv("Crop_recommendation.csv")  # Corrected to use read_csv
#print(df)

data_list = df.to_dict(orient="records")  # Convert each row to a dictionary

data_list = sorted(data_list, key=lambda x: x['label'])
#print(data_list)

for i in data_list:
    if i['label'] == 'rice':
        rice.append(i)
    elif i['label'] == 'maize':
        maize.append(i)
    elif i['label'] == 'chickpea':
        chickpea.append(i)
    elif i['label'] == 'kidneybeans':
        kidneybeans.append(i)
    elif i['label'] == 'pigeonpeas':
        pigeonpeas.append(i)
    elif i['label'] == 'mothbeans':
        mothbeans.append(i)
    elif i['label'] == 'mungbean':
        mungbean.append(i)
    elif i['label'] == 'blackgram':
        blackgram.append(i)
    elif i['label'] == 'lentil':
        lentil.append(i)
    elif i['label'] == 'pomegranate':
        pomegranate.append(i)
    elif i['label'] == 'banana':
        banana.append(i)
    elif i['label'] == 'mango':
        mango.append(i)
    elif i['label'] == 'grapes':
        grapes.append(i)
    elif i['label'] == 'watermelon':
        watermelon.append(i)
    elif i['label'] == 'muskmelon':
        muskmelon.append(i)
    elif i['label'] == 'apple':
        apple.append(i)
    elif i['label'] == 'orange':
        orange.append(i)
    elif i['label'] == 'papaya':
        papaya.append(i)
    elif i['label'] == 'coconut':
        coconut.append(i)
    elif i['label'] == 'cotton':
        cotton.append(i)
    elif i['label'] == 'jute':
        jute.append(i)
    elif i['label'] == 'coffee':
        coffee.append(i)

count = len(rice)
sumN, avgN, minN, maxN = 0, 0, 1000, 0
sumP, avgP, minP, maxP = 0, 0, 1000, 0
sumK, avgK, minK, maxK = 0, 0, 1000, 0
sumTemp, avgTemp, minTemp, maxTemp = 0, 0, 1000, 0
sumHum, avgHum, minHum, maxHum = 0, 0, 1000, 0
sumPH, avgPH, minPH, maxPH = 0, 0, 1000, 0
sumSM, avgSM, minSM, maxSM = 0, 0, 1000, 0
for i in rice:
        sumN += i['Nitrogen']
        if i['Nitrogen'] == 0:
             minN = minN
        else:
             minN = min(minN, i['Nitrogen'])
        maxN = max(maxN, i['Nitrogen'])
        sumP += i['phosphorus']
        if i['phosphorus'] == 0:
             minP = minP
        else:
             minP = min(minP, i['phosphorus'])
        maxP = max(maxP, i['phosphorus'])
        sumK += i['potassium']
        if i['potassium'] == 0:
             minK = minK
        else:
             minK = min(minK, i['potassium'])
        maxK = max(maxK, i['potassium'])
        sumTemp += i['temperature']
        if i['temperature'] == 0:
             minTemp = minTemp
        else:
             minTemp = min(minTemp, i['temperature'])
        maxTemp = max(maxTemp, i['temperature'])
        sumHum += i['humidity']
        if i['humidity'] == 0:
             minHum = minHum
        else:
             minHum = min(minHum, i['humidity'])
        maxHum = max(maxHum, i['humidity'])
        sumPH += i['ph']
        if i['ph'] == 0:
             minPH = minPH
        else:
             minPH = min(minPH, i['ph'])
        maxPH = max(maxPH, i['ph'])
        sumSM += i['rainfall']
        if i['rainfall'] == 0:
             minSM = minSM
        else:
             minSM = min(minSM, i['rainfall'])
        maxSM = max(maxSM, i['rainfall'])
        avgN =  sumN/count 
        avgP = sumP/count 
        avgK = sumK/count 
        avgTemp = sumTemp/count 
        avgHum = sumHum/count 
        avgPH = sumPH/count 
        avgSM = sumSM/count 
rice = [{"name":"rice", "Nitrogen":avgN, "Min Nitrogen":minN, "Max Nitrogen":maxN, 
        "phosphorus":avgP, "Min phosphorus":minP, "Max phosphorus":maxP, 
        "potassium":avgK, "Min potassium":minK, "Max potassium":maxK, 
        "temperature":avgTemp, "Min temperature":minTemp, "Max temperature":maxTemp, 
        "humidity":avgHum, "Min humidity":minHum, "Max humidity":maxHum, 
        "pH":avgPH, "Min pH":minPH, "Max pH":maxPH, "soil moisture":avgSM, 
        "Min soil moisture":minSM, "Max soil moisture":maxSM, "selected":False}]


count = len(maize)
sumN, avgN, minN, maxN = 0, 0, 1000, 0
sumP, avgP, minP, maxP = 0, 0, 1000, 0
sumK, avgK, minK, maxK = 0, 0, 1000, 0
sumTemp, avgTemp, minTemp, maxTemp = 0, 0, 1000, 0
sumHum, avgHum, minHum, maxHum = 0, 0, 1000, 0
sumPH, avgPH, minPH, maxPH = 0, 0, 1000, 0
sumSM, avgSM, minSM, maxSM = 0, 0, 1000, 0
for i in maize:
        sumN += i['Nitrogen']
        if i['Nitrogen'] == 0:
             minN = minN
        else:
             minN = min(minN, i['Nitrogen'])
        maxN = max(maxN, i['Nitrogen'])
        sumP += i['phosphorus']
        if i['phosphorus'] == 0:
             minP = minP
        else:
             minP = min(minP, i['phosphorus'])
        maxP = max(maxP, i['phosphorus'])
        sumK += i['potassium']
        if i['potassium'] == 0:
             minK = minK
        else:
             minK = min(minK, i['potassium'])
        maxK = max(maxK, i['potassium'])
        sumTemp += i['temperature']
        if i['temperature'] == 0:
             minTemp = minTemp
        else:
             minTemp = min(minTemp, i['temperature'])
        maxTemp = max(maxTemp, i['temperature'])
        sumHum += i['humidity']
        if i['humidity'] == 0:
             minHum = minHum
        else:
             minHum = min(minHum, i['humidity'])
        maxHum = max(maxHum, i['humidity'])
        sumPH += i['ph']
        if i['ph'] == 0:
             minPH = minPH
        else:
             minPH = min(minPH, i['ph'])
        maxPH = max(maxPH, i['ph'])
        sumSM += i['rainfall']
        if i['rainfall'] == 0:
             minSM = minSM
        else:
             minSM = min(minSM, i['rainfall'])
        maxSM = max(maxSM, i['rainfall'])
        avgN =  sumN/count 
        avgP = sumP/count 
        avgK = sumK/count 
        avgTemp = sumTemp/count 
        avgHum = sumHum/count 
        avgPH = sumPH/count 
        avgSM = sumSM/count 
maize = [{"name":"maize", "Nitrogen":avgN, "Min Nitrogen":minN, "Max Nitrogen":maxN, 
        "phosphorus":avgP, "Min phosphorus":minP, "Max phosphorus":maxP, 
        "potassium":avgK, "Min potassium":minK, "Max potassium":maxK, 
        "temperature":avgTemp, "Min temperature":minTemp, "Max temperature":maxTemp, 
        "humidity":avgHum, "Min humidity":minHum, "Max humidity":maxHum, 
        "pH":avgPH, "Min pH":minPH, "Max pH":maxPH, "soil moisture":avgSM, 
        "Min soil moisture":minSM, "Max soil moisture":maxSM, "selected":False}]


count = len(chickpea)
sumN, avgN, minN, maxN = 0, 0, 1000, 0
sumP, avgP, minP, maxP = 0, 0, 1000, 0
sumK, avgK, minK, maxK = 0, 0, 1000, 0
sumTemp, avgTemp, minTemp, maxTemp = 0, 0, 1000, 0
sumHum, avgHum, minHum, maxHum = 0, 0, 1000, 0
sumPH, avgPH, minPH, maxPH = 0, 0, 1000, 0
sumSM, avgSM, minSM, maxSM = 0, 0, 1000, 0
for i in chickpea:
        sumN += i['Nitrogen']
        if i['Nitrogen'] == 0:
             minN = minN
        else:
             minN = min(minN, i['Nitrogen'])
        maxN = max(maxN, i['Nitrogen'])
        sumP += i['phosphorus']
        if i['phosphorus'] == 0:
             minP = minP
        else:
             minP = min(minP, i['phosphorus'])
        maxP = max(maxP, i['phosphorus'])
        sumK += i['potassium']
        if i['potassium'] == 0:
             minK = minK
        else:
             minK = min(minK, i['potassium'])
        maxK = max(maxK, i['potassium'])
        sumTemp += i['temperature']
        if i['temperature'] == 0:
             minTemp = minTemp
        else:
             minTemp = min(minTemp, i['temperature'])
        maxTemp = max(maxTemp, i['temperature'])
        sumHum += i['humidity']
        if i['humidity'] == 0:
             minHum = minHum
        else:
             minHum = min(minHum, i['humidity'])
        maxHum = max(maxHum, i['humidity'])
        sumPH += i['ph']
        if i['ph'] == 0:
             minPH = minPH
        else:
             minPH = min(minPH, i['ph'])
        maxPH = max(maxPH, i['ph'])
        sumSM += i['rainfall']
        if i['rainfall'] == 0:
             minSM = minSM
        else:
             minSM = min(minSM, i['rainfall'])
        maxSM = max(maxSM, i['rainfall'])
        avgN =  sumN/count 
        avgP = sumP/count 
        avgK = sumK/count 
        avgTemp = sumTemp/count 
        avgHum = sumHum/count 
        avgPH = sumPH/count 
        avgSM = sumSM/count 
chickpea = [{"name":"chickpea", "Nitrogen":avgN, "Min Nitrogen":minN, "Max Nitrogen":maxN, 
        "phosphorus":avgP, "Min phosphorus":minP, "Max phosphorus":maxP, 
        "potassium":avgK, "Min potassium":minK, "Max potassium":maxK, 
        "temperature":avgTemp, "Min temperature":minTemp, "Max temperature":maxTemp, 
        "humidity":avgHum, "Min humidity":minHum, "Max humidity":maxHum, 
        "pH":avgPH, "Min pH":minPH, "Max pH":maxPH, "soil moisture":avgSM, 
        "Min soil moisture":minSM, "Max soil moisture":maxSM, "selected":False}]


count = len(kidneybeans)
sumN, avgN, minN, maxN = 0, 0, 1000, 0
sumP, avgP, minP, maxP = 0, 0, 1000, 0
sumK, avgK, minK, maxK = 0, 0, 1000, 0
sumTemp, avgTemp, minTemp, maxTemp = 0, 0, 1000, 0
sumHum, avgHum, minHum, maxHum = 0, 0, 1000, 0
sumPH, avgPH, minPH, maxPH = 0, 0, 1000, 0
sumSM, avgSM, minSM, maxSM = 0, 0, 1000, 0
for i in kidneybeans:
        sumN += i['Nitrogen']
        if i['Nitrogen'] == 0:
             minN = minN
        else:
             minN = min(minN, i['Nitrogen'])
        maxN = max(maxN, i['Nitrogen'])
        sumP += i['phosphorus']
        if i['phosphorus'] == 0:
             minP = minP
        else:
             minP = min(minP, i['phosphorus'])
        maxP = max(maxP, i['phosphorus'])
        sumK += i['potassium']
        if i['potassium'] == 0:
             minK = minK
        else:
             minK = min(minK, i['potassium'])
        maxK = max(maxK, i['potassium'])
        sumTemp += i['temperature']
        if i['temperature'] == 0:
             minTemp = minTemp
        else:
             minTemp = min(minTemp, i['temperature'])
        maxTemp = max(maxTemp, i['temperature'])
        sumHum += i['humidity']
        if i['humidity'] == 0:
             minHum = minHum
        else:
             minHum = min(minHum, i['humidity'])
        maxHum = max(maxHum, i['humidity'])
        sumPH += i['ph']
        if i['ph'] == 0:
             minPH = minPH
        else:
             minPH = min(minPH, i['ph'])
        maxPH = max(maxPH, i['ph'])
        sumSM += i['rainfall']
        if i['rainfall'] == 0:
             minSM = minSM
        else:
             minSM = min(minSM, i['rainfall'])
        maxSM = max(maxSM, i['rainfall'])
        avgN =  sumN/count 
        avgP = sumP/count 
        avgK = sumK/count 
        avgTemp = sumTemp/count 
        avgHum = sumHum/count 
        avgPH = sumPH/count 
        avgSM = sumSM/count 
kidneybeans = [{"name":"kidneybeans", "Nitrogen":avgN, "Min Nitrogen":minN, "Max Nitrogen":maxN, 
        "phosphorus":avgP, "Min phosphorus":minP, "Max phosphorus":maxP, 
        "potassium":avgK, "Min potassium":minK, "Max potassium":maxK, 
        "temperature":avgTemp, "Min temperature":minTemp, "Max temperature":maxTemp, 
        "humidity":avgHum, "Min humidity":minHum, "Max humidity":maxHum, 
        "pH":avgPH, "Min pH":minPH, "Max pH":maxPH, "soil moisture":avgSM, 
        "Min soil moisture":minSM, "Max soil moisture":maxSM, "selected":False}]


count = len(pigeonpeas)
sumN, avgN, minN, maxN = 0, 0, 1000, 0
sumP, avgP, minP, maxP = 0, 0, 1000, 0
sumK, avgK, minK, maxK = 0, 0, 1000, 0
sumTemp, avgTemp, minTemp, maxTemp = 0, 0, 1000, 0
sumHum, avgHum, minHum, maxHum = 0, 0, 1000, 0
sumPH, avgPH, minPH, maxPH = 0, 0, 1000, 0
sumSM, avgSM, minSM, maxSM = 0, 0, 1000, 0
for i in pigeonpeas:
        sumN += i['Nitrogen']
        if i['Nitrogen'] == 0:
             minN = minN
        else:
             minN = min(minN, i['Nitrogen'])
        maxN = max(maxN, i['Nitrogen'])
        sumP += i['phosphorus']
        if i['phosphorus'] == 0:
             minP = minP
        else:
             minP = min(minP, i['phosphorus'])
        maxP = max(maxP, i['phosphorus'])
        sumK += i['potassium']
        if i['potassium'] == 0:
             minK = minK
        else:
             minK = min(minK, i['potassium'])
        maxK = max(maxK, i['potassium'])
        sumTemp += i['temperature']
        if i['temperature'] == 0:
             minTemp = minTemp
        else:
             minTemp = min(minTemp, i['temperature'])
        maxTemp = max(maxTemp, i['temperature'])
        sumHum += i['humidity']
        if i['humidity'] == 0:
             minHum = minHum
        else:
             minHum = min(minHum, i['humidity'])
        maxHum = max(maxHum, i['humidity'])
        sumPH += i['ph']
        if i['ph'] == 0:
             minPH = minPH
        else:
             minPH = min(minPH, i['ph'])
        maxPH = max(maxPH, i['ph'])
        sumSM += i['rainfall']
        if i['rainfall'] == 0:
             minSM = minSM
        else:
             minSM = min(minSM, i['rainfall'])
        maxSM = max(maxSM, i['rainfall'])
        avgN =  sumN/count 
        avgP = sumP/count 
        avgK = sumK/count 
        avgTemp = sumTemp/count 
        avgHum = sumHum/count 
        avgPH = sumPH/count 
        avgSM = sumSM/count 
pigeonpeas = [{"name":"pigeonpeas", "Nitrogen":avgN, "Min Nitrogen":minN, "Max Nitrogen":maxN, 
        "phosphorus":avgP, "Min phosphorus":minP, "Max phosphorus":maxP, 
        "potassium":avgK, "Min potassium":minK, "Max potassium":maxK, 
        "temperature":avgTemp, "Min temperature":minTemp, "Max temperature":maxTemp, 
        "humidity":avgHum, "Min humidity":minHum, "Max humidity":maxHum, 
        "pH":avgPH, "Min pH":minPH, "Max pH":maxPH, "soil moisture":avgSM, 
        "Min soil moisture":minSM, "Max soil moisture":maxSM, "selected":False}]


count = len(mothbeans)
sumN, avgN, minN, maxN = 0, 0, 1000, 0
sumP, avgP, minP, maxP = 0, 0, 1000, 0
sumK, avgK, minK, maxK = 0, 0, 1000, 0
sumTemp, avgTemp, minTemp, maxTemp = 0, 0, 1000, 0
sumHum, avgHum, minHum, maxHum = 0, 0, 1000, 0
sumPH, avgPH, minPH, maxPH = 0, 0, 1000, 0
sumSM, avgSM, minSM, maxSM = 0, 0, 1000, 0
for i in mothbeans:
        sumN += i['Nitrogen']
        if i['Nitrogen'] == 0:
             minN = minN
        else:
             minN = min(minN, i['Nitrogen'])
        maxN = max(maxN, i['Nitrogen'])
        sumP += i['phosphorus']
        if i['phosphorus'] == 0:
             minP = minP
        else:
             minP = min(minP, i['phosphorus'])
        maxP = max(maxP, i['phosphorus'])
        sumK += i['potassium']
        if i['potassium'] == 0:
             minK = minK
        else:
             minK = min(minK, i['potassium'])
        maxK = max(maxK, i['potassium'])
        sumTemp += i['temperature']
        if i['temperature'] == 0:
             minTemp = minTemp
        else:
             minTemp = min(minTemp, i['temperature'])
        maxTemp = max(maxTemp, i['temperature'])
        sumHum += i['humidity']
        if i['humidity'] == 0:
             minHum = minHum
        else:
             minHum = min(minHum, i['humidity'])
        maxHum = max(maxHum, i['humidity'])
        sumPH += i['ph']
        if i['ph'] == 0:
             minPH = minPH
        else:
             minPH = min(minPH, i['ph'])
        maxPH = max(maxPH, i['ph'])
        sumSM += i['rainfall']
        if i['rainfall'] == 0:
             minSM = minSM
        else:
             minSM = min(minSM, i['rainfall'])
        maxSM = max(maxSM, i['rainfall'])
        avgN =  sumN/count 
        avgP = sumP/count 
        avgK = sumK/count 
        avgTemp = sumTemp/count 
        avgHum = sumHum/count 
        avgPH = sumPH/count 
        avgSM = sumSM/count 
mothbeans = [{"name":"mothbeans", "Nitrogen":avgN, "Min Nitrogen":minN, "Max Nitrogen":maxN, 
        "phosphorus":avgP, "Min phosphorus":minP, "Max phosphorus":maxP, 
        "potassium":avgK, "Min potassium":minK, "Max potassium":maxK, 
        "temperature":avgTemp, "Min temperature":minTemp, "Max temperature":maxTemp, 
        "humidity":avgHum, "Min humidity":minHum, "Max humidity":maxHum, 
        "pH":avgPH, "Min pH":minPH, "Max pH":maxPH, "soil moisture":avgSM, 
        "Min soil moisture":minSM, "Max soil moisture":maxSM, "selected":False}]


count = len(mungbean)
sumN, avgN, minN, maxN = 0, 0, 1000, 0
sumP, avgP, minP, maxP = 0, 0, 1000, 0
sumK, avgK, minK, maxK = 0, 0, 1000, 0
sumTemp, avgTemp, minTemp, maxTemp = 0, 0, 1000, 0
sumHum, avgHum, minHum, maxHum = 0, 0, 1000, 0
sumPH, avgPH, minPH, maxPH = 0, 0, 1000, 0
sumSM, avgSM, minSM, maxSM = 0, 0, 1000, 0
for i in mungbean:
        sumN += i['Nitrogen']
        if i['Nitrogen'] == 0:
             minN = minN
        else:
             minN = min(minN, i['Nitrogen'])
        maxN = max(maxN, i['Nitrogen'])
        sumP += i['phosphorus']
        if i['phosphorus'] == 0:
             minP = minP
        else:
             minP = min(minP, i['phosphorus'])
        maxP = max(maxP, i['phosphorus'])
        sumK += i['potassium']
        if i['potassium'] == 0:
             minK = minK
        else:
             minK = min(minK, i['potassium'])
        maxK = max(maxK, i['potassium'])
        sumTemp += i['temperature']
        if i['temperature'] == 0:
             minTemp = minTemp
        else:
             minTemp = min(minTemp, i['temperature'])
        maxTemp = max(maxTemp, i['temperature'])
        sumHum += i['humidity']
        if i['humidity'] == 0:
             minHum = minHum
        else:
             minHum = min(minHum, i['humidity'])
        maxHum = max(maxHum, i['humidity'])
        sumPH += i['ph']
        if i['ph'] == 0:
             minPH = minPH
        else:
             minPH = min(minPH, i['ph'])
        maxPH = max(maxPH, i['ph'])
        sumSM += i['rainfall']
        if i['rainfall'] == 0:
             minSM = minSM
        else:
             minSM = min(minSM, i['rainfall'])
        maxSM = max(maxSM, i['rainfall'])
        avgN =  sumN/count 
        avgP = sumP/count 
        avgK = sumK/count 
        avgTemp = sumTemp/count 
        avgHum = sumHum/count 
        avgPH = sumPH/count 
        avgSM = sumSM/count 
mungbean = [{"name":"mungbean", "Nitrogen":avgN, "Min Nitrogen":minN, "Max Nitrogen":maxN, 
        "phosphorus":avgP, "Min phosphorus":minP, "Max phosphorus":maxP, 
        "potassium":avgK, "Min potassium":minK, "Max potassium":maxK, 
        "temperature":avgTemp, "Min temperature":minTemp, "Max temperature":maxTemp, 
        "humidity":avgHum, "Min humidity":minHum, "Max humidity":maxHum, 
        "pH":avgPH, "Min pH":minPH, "Max pH":maxPH, "soil moisture":avgSM, 
        "Min soil moisture":minSM, "Max soil moisture":maxSM, "selected":False}]


count = len(blackgram)
sumN, avgN, minN, maxN = 0, 0, 1000, 0
sumP, avgP, minP, maxP = 0, 0, 1000, 0
sumK, avgK, minK, maxK = 0, 0, 1000, 0
sumTemp, avgTemp, minTemp, maxTemp = 0, 0, 1000, 0
sumHum, avgHum, minHum, maxHum = 0, 0, 1000, 0
sumPH, avgPH, minPH, maxPH = 0, 0, 1000, 0
sumSM, avgSM, minSM, maxSM = 0, 0, 1000, 0
for i in blackgram:
        sumN += i['Nitrogen']
        if i['Nitrogen'] == 0:
             minN = minN
        else:
             minN = min(minN, i['Nitrogen'])
        maxN = max(maxN, i['Nitrogen'])
        sumP += i['phosphorus']
        if i['phosphorus'] == 0:
             minP = minP
        else:
             minP = min(minP, i['phosphorus'])
        maxP = max(maxP, i['phosphorus'])
        sumK += i['potassium']
        if i['potassium'] == 0:
             minK = minK
        else:
             minK = min(minK, i['potassium'])
        maxK = max(maxK, i['potassium'])
        sumTemp += i['temperature']
        if i['temperature'] == 0:
             minTemp = minTemp
        else:
             minTemp = min(minTemp, i['temperature'])
        maxTemp = max(maxTemp, i['temperature'])
        sumHum += i['humidity']
        if i['humidity'] == 0:
             minHum = minHum
        else:
             minHum = min(minHum, i['humidity'])
        maxHum = max(maxHum, i['humidity'])
        sumPH += i['ph']
        if i['ph'] == 0:
             minPH = minPH
        else:
             minPH = min(minPH, i['ph'])
        maxPH = max(maxPH, i['ph'])
        sumSM += i['rainfall']
        if i['rainfall'] == 0:
             minSM = minSM
        else:
             minSM = min(minSM, i['rainfall'])
        maxSM = max(maxSM, i['rainfall'])
        avgN =  sumN/count 
        avgP = sumP/count 
        avgK = sumK/count 
        avgTemp = sumTemp/count 
        avgHum = sumHum/count 
        avgPH = sumPH/count 
        avgSM = sumSM/count 
blackgram = [{"name":"blackgram", "Nitrogen":avgN, "Min Nitrogen":minN, "Max Nitrogen":maxN, 
        "phosphorus":avgP, "Min phosphorus":minP, "Max phosphorus":maxP, 
        "potassium":avgK, "Min potassium":minK, "Max potassium":maxK, 
        "temperature":avgTemp, "Min temperature":minTemp, "Max temperature":maxTemp, 
        "humidity":avgHum, "Min humidity":minHum, "Max humidity":maxHum, 
        "pH":avgPH, "Min pH":minPH, "Max pH":maxPH, "soil moisture":avgSM, 
        "Min soil moisture":minSM, "Max soil moisture":maxSM, "selected":False}]


count = len(lentil)
sumN, avgN, minN, maxN = 0, 0, 1000, 0
sumP, avgP, minP, maxP = 0, 0, 1000, 0
sumK, avgK, minK, maxK = 0, 0, 1000, 0
sumTemp, avgTemp, minTemp, maxTemp = 0, 0, 1000, 0
sumHum, avgHum, minHum, maxHum = 0, 0, 1000, 0
sumPH, avgPH, minPH, maxPH = 0, 0, 1000, 0
sumSM, avgSM, minSM, maxSM = 0, 0, 1000, 0
for i in lentil:
        sumN += i['Nitrogen']
        if i['Nitrogen'] == 0:
             minN = minN
        else:
             minN = min(minN, i['Nitrogen'])
        maxN = max(maxN, i['Nitrogen'])
        sumP += i['phosphorus']
        if i['phosphorus'] == 0:
             minP = minP
        else:
             minP = min(minP, i['phosphorus'])
        maxP = max(maxP, i['phosphorus'])
        sumK += i['potassium']
        if i['potassium'] == 0:
             minK = minK
        else:
             minK = min(minK, i['potassium'])
        maxK = max(maxK, i['potassium'])
        sumTemp += i['temperature']
        if i['temperature'] == 0:
             minTemp = minTemp
        else:
             minTemp = min(minTemp, i['temperature'])
        maxTemp = max(maxTemp, i['temperature'])
        sumHum += i['humidity']
        if i['humidity'] == 0:
             minHum = minHum
        else:
             minHum = min(minHum, i['humidity'])
        maxHum = max(maxHum, i['humidity'])
        sumPH += i['ph']
        if i['ph'] == 0:
             minPH = minPH
        else:
             minPH = min(minPH, i['ph'])
        maxPH = max(maxPH, i['ph'])
        sumSM += i['rainfall']
        if i['rainfall'] == 0:
             minSM = minSM
        else:
             minSM = min(minSM, i['rainfall'])
        maxSM = max(maxSM, i['rainfall'])
        avgN =  sumN/count 
        avgP = sumP/count 
        avgK = sumK/count 
        avgTemp = sumTemp/count 
        avgHum = sumHum/count 
        avgPH = sumPH/count 
        avgSM = sumSM/count 
lentil = [{"name":"lentil", "Nitrogen":avgN, "Min Nitrogen":minN, "Max Nitrogen":maxN, 
        "phosphorus":avgP, "Min phosphorus":minP, "Max phosphorus":maxP, 
        "potassium":avgK, "Min potassium":minK, "Max potassium":maxK, 
        "temperature":avgTemp, "Min temperature":minTemp, "Max temperature":maxTemp, 
        "humidity":avgHum, "Min humidity":minHum, "Max humidity":maxHum, 
        "pH":avgPH, "Min pH":minPH, "Max pH":maxPH, "soil moisture":avgSM, 
        "Min soil moisture":minSM, "Max soil moisture":maxSM, "selected":False}]


count = len(pomegranate)
sumN, avgN, minN, maxN = 0, 0, 1000, 0
sumP, avgP, minP, maxP = 0, 0, 1000, 0
sumK, avgK, minK, maxK = 0, 0, 1000, 0
sumTemp, avgTemp, minTemp, maxTemp = 0, 0, 1000, 0
sumHum, avgHum, minHum, maxHum = 0, 0, 1000, 0
sumPH, avgPH, minPH, maxPH = 0, 0, 1000, 0
sumSM, avgSM, minSM, maxSM = 0, 0, 1000, 0
for i in pomegranate:
        sumN += i['Nitrogen']
        if i['Nitrogen'] == 0:
             minN = minN
        else:
             minN = min(minN, i['Nitrogen'])
        maxN = max(maxN, i['Nitrogen'])
        sumP += i['phosphorus']
        if i['phosphorus'] == 0:
             minP = minP
        else:
             minP = min(minP, i['phosphorus'])
        maxP = max(maxP, i['phosphorus'])
        sumK += i['potassium']
        if i['potassium'] == 0:
             minK = minK
        else:
             minK = min(minK, i['potassium'])
        maxK = max(maxK, i['potassium'])
        sumTemp += i['temperature']
        if i['temperature'] == 0:
             minTemp = minTemp
        else:
             minTemp = min(minTemp, i['temperature'])
        maxTemp = max(maxTemp, i['temperature'])
        sumHum += i['humidity']
        if i['humidity'] == 0:
             minHum = minHum
        else:
             minHum = min(minHum, i['humidity'])
        maxHum = max(maxHum, i['humidity'])
        sumPH += i['ph']
        if i['ph'] == 0:
             minPH = minPH
        else:
             minPH = min(minPH, i['ph'])
        maxPH = max(maxPH, i['ph'])
        sumSM += i['rainfall']
        if i['rainfall'] == 0:
             minSM = minSM
        else:
             minSM = min(minSM, i['rainfall'])
        maxSM = max(maxSM, i['rainfall'])
        avgN =  sumN/count 
        avgP = sumP/count 
        avgK = sumK/count 
        avgTemp = sumTemp/count 
        avgHum = sumHum/count 
        avgPH = sumPH/count 
        avgSM = sumSM/count 
pomegranate = [{"name":"pomegranate", "Nitrogen":avgN, "Min Nitrogen":minN, "Max Nitrogen":maxN, 
        "phosphorus":avgP, "Min phosphorus":minP, "Max phosphorus":maxP, 
        "potassium":avgK, "Min potassium":minK, "Max potassium":maxK, 
        "temperature":avgTemp, "Min temperature":minTemp, "Max temperature":maxTemp, 
        "humidity":avgHum, "Min humidity":minHum, "Max humidity":maxHum, 
        "pH":avgPH, "Min pH":minPH, "Max pH":maxPH, "soil moisture":avgSM, 
        "Min soil moisture":minSM, "Max soil moisture":maxSM, "selected":False}]


count = len(banana)
sumN, avgN, minN, maxN = 0, 0, 1000, 0
sumP, avgP, minP, maxP = 0, 0, 1000, 0
sumK, avgK, minK, maxK = 0, 0, 1000, 0
sumTemp, avgTemp, minTemp, maxTemp = 0, 0, 1000, 0
sumHum, avgHum, minHum, maxHum = 0, 0, 1000, 0
sumPH, avgPH, minPH, maxPH = 0, 0, 1000, 0
sumSM, avgSM, minSM, maxSM = 0, 0, 1000, 0
for i in banana:
        sumN += i['Nitrogen']
        if i['Nitrogen'] == 0:
             minN = minN
        else:
             minN = min(minN, i['Nitrogen'])
        maxN = max(maxN, i['Nitrogen'])
        sumP += i['phosphorus']
        if i['phosphorus'] == 0:
             minP = minP
        else:
             minP = min(minP, i['phosphorus'])
        maxP = max(maxP, i['phosphorus'])
        sumK += i['potassium']
        if i['potassium'] == 0:
             minK = minK
        else:
             minK = min(minK, i['potassium'])
        maxK = max(maxK, i['potassium'])
        sumTemp += i['temperature']
        if i['temperature'] == 0:
             minTemp = minTemp
        else:
             minTemp = min(minTemp, i['temperature'])
        maxTemp = max(maxTemp, i['temperature'])
        sumHum += i['humidity']
        if i['humidity'] == 0:
             minHum = minHum
        else:
             minHum = min(minHum, i['humidity'])
        maxHum = max(maxHum, i['humidity'])
        sumPH += i['ph']
        if i['ph'] == 0:
             minPH = minPH
        else:
             minPH = min(minPH, i['ph'])
        maxPH = max(maxPH, i['ph'])
        sumSM += i['rainfall']
        if i['rainfall'] == 0:
             minSM = minSM
        else:
             minSM = min(minSM, i['rainfall'])
        maxSM = max(maxSM, i['rainfall'])
        avgN =  sumN/count 
        avgP = sumP/count 
        avgK = sumK/count 
        avgTemp = sumTemp/count 
        avgHum = sumHum/count 
        avgPH = sumPH/count 
        avgSM = sumSM/count 
banana = [{"name":"banana", "Nitrogen":avgN, "Min Nitrogen":minN, "Max Nitrogen":maxN, 
        "phosphorus":avgP, "Min phosphorus":minP, "Max phosphorus":maxP, 
        "potassium":avgK, "Min potassium":minK, "Max potassium":maxK, 
        "temperature":avgTemp, "Min temperature":minTemp, "Max temperature":maxTemp, 
        "humidity":avgHum, "Min humidity":minHum, "Max humidity":maxHum, 
        "pH":avgPH, "Min pH":minPH, "Max pH":maxPH, "soil moisture":avgSM, 
        "Min soil moisture":minSM, "Max soil moisture":maxSM, "selected":False}]



count = len(mango)
sumN, avgN, minN, maxN = 0, 0, 1000, 0
sumP, avgP, minP, maxP = 0, 0, 1000, 0
sumK, avgK, minK, maxK = 0, 0, 1000, 0
sumTemp, avgTemp, minTemp, maxTemp = 0, 0, 1000, 0
sumHum, avgHum, minHum, maxHum = 0, 0, 1000, 0
sumPH, avgPH, minPH, maxPH = 0, 0, 1000, 0
sumSM, avgSM, minSM, maxSM = 0, 0, 1000, 0
for i in mango:
        sumN += i['Nitrogen']
        if i['Nitrogen'] == 0:
             minN = minN
        else:
             minN = min(minN, i['Nitrogen'])
        maxN = max(maxN, i['Nitrogen'])
        sumP += i['phosphorus']
        if i['phosphorus'] == 0:
             minP = minP
        else:
             minP = min(minP, i['phosphorus'])
        maxP = max(maxP, i['phosphorus'])
        sumK += i['potassium']
        if i['potassium'] == 0:
             minK = minK
        else:
             minK = min(minK, i['potassium'])
        maxK = max(maxK, i['potassium'])
        sumTemp += i['temperature']
        if i['temperature'] == 0:
             minTemp = minTemp
        else:
             minTemp = min(minTemp, i['temperature'])
        maxTemp = max(maxTemp, i['temperature'])
        sumHum += i['humidity']
        if i['humidity'] == 0:
             minHum = minHum
        else:
             minHum = min(minHum, i['humidity'])
        maxHum = max(maxHum, i['humidity'])
        sumPH += i['ph']
        if i['ph'] == 0:
             minPH = minPH
        else:
             minPH = min(minPH, i['ph'])
        maxPH = max(maxPH, i['ph'])
        sumSM += i['rainfall']
        if i['rainfall'] == 0:
             minSM = minSM
        else:
             minSM = min(minSM, i['rainfall'])
        maxSM = max(maxSM, i['rainfall'])
        avgN =  sumN/count 
        avgP = sumP/count 
        avgK = sumK/count 
        avgTemp = sumTemp/count 
        avgHum = sumHum/count 
        avgPH = sumPH/count 
        avgSM = sumSM/count 
mango = [{"name":"mango", "Nitrogen":avgN, "Min Nitrogen":minN, "Max Nitrogen":maxN, 
        "phosphorus":avgP, "Min phosphorus":minP, "Max phosphorus":maxP, 
        "potassium":avgK, "Min potassium":minK, "Max potassium":maxK, 
        "temperature":avgTemp, "Min temperature":minTemp, "Max temperature":maxTemp, 
        "humidity":avgHum, "Min humidity":minHum, "Max humidity":maxHum, 
        "pH":avgPH, "Min pH":minPH, "Max pH":maxPH, "soil moisture":avgSM, 
        "Min soil moisture":minSM, "Max soil moisture":maxSM, "selected":False}]


count = len(grapes)
sumN, avgN, minN, maxN = 0, 0, 1000, 0
sumP, avgP, minP, maxP = 0, 0, 1000, 0
sumK, avgK, minK, maxK = 0, 0, 1000, 0
sumTemp, avgTemp, minTemp, maxTemp = 0, 0, 1000, 0
sumHum, avgHum, minHum, maxHum = 0, 0, 1000, 0
sumPH, avgPH, minPH, maxPH = 0, 0, 1000, 0
sumSM, avgSM, minSM, maxSM = 0, 0, 1000, 0
for i in grapes:
        sumN += i['Nitrogen']
        if i['Nitrogen'] == 0:
             minN = minN
        else:
             minN = min(minN, i['Nitrogen'])
        maxN = max(maxN, i['Nitrogen'])
        sumP += i['phosphorus']
        if i['phosphorus'] == 0:
             minP = minP
        else:
             minP = min(minP, i['phosphorus'])
        maxP = max(maxP, i['phosphorus'])
        sumK += i['potassium']
        if i['potassium'] == 0:
             minK = minK
        else:
             minK = min(minK, i['potassium'])
        maxK = max(maxK, i['potassium'])
        sumTemp += i['temperature']
        if i['temperature'] == 0:
             minTemp = minTemp
        else:
             minTemp = min(minTemp, i['temperature'])
        maxTemp = max(maxTemp, i['temperature'])
        sumHum += i['humidity']
        if i['humidity'] == 0:
             minHum = minHum
        else:
             minHum = min(minHum, i['humidity'])
        maxHum = max(maxHum, i['humidity'])
        sumPH += i['ph']
        if i['ph'] == 0:
             minPH = minPH
        else:
             minPH = min(minPH, i['ph'])
        maxPH = max(maxPH, i['ph'])
        sumSM += i['rainfall']
        if i['rainfall'] == 0:
             minSM = minSM
        else:
             minSM = min(minSM, i['rainfall'])
        maxSM = max(maxSM, i['rainfall'])
        avgN =  sumN/count 
        avgP = sumP/count 
        avgK = sumK/count 
        avgTemp = sumTemp/count 
        avgHum = sumHum/count 
        avgPH = sumPH/count 
        avgSM = sumSM/count 
grapes = [{"name":"grapes", "Nitrogen":avgN, "Min Nitrogen":minN, "Max Nitrogen":maxN, 
        "phosphorus":avgP, "Min phosphorus":minP, "Max phosphorus":maxP, 
        "potassium":avgK, "Min potassium":minK, "Max potassium":maxK, 
        "temperature":avgTemp, "Min temperature":minTemp, "Max temperature":maxTemp, 
        "humidity":avgHum, "Min humidity":minHum, "Max humidity":maxHum, 
        "pH":avgPH, "Min pH":minPH, "Max pH":maxPH, "soil moisture":avgSM, 
        "Min soil moisture":minSM, "Max soil moisture":maxSM, "selected":False}]


count = len(watermelon)
sumN, avgN, minN, maxN = 0, 0, 1000, 0
sumP, avgP, minP, maxP = 0, 0, 1000, 0
sumK, avgK, minK, maxK = 0, 0, 1000, 0
sumTemp, avgTemp, minTemp, maxTemp = 0, 0, 1000, 0
sumHum, avgHum, minHum, maxHum = 0, 0, 1000, 0
sumPH, avgPH, minPH, maxPH = 0, 0, 1000, 0
sumSM, avgSM, minSM, maxSM = 0, 0, 1000, 0
for i in watermelon:
        sumN += i['Nitrogen']
        if i['Nitrogen'] == 0:
             minN = minN
        else:
             minN = min(minN, i['Nitrogen'])
        maxN = max(maxN, i['Nitrogen'])
        sumP += i['phosphorus']
        if i['phosphorus'] == 0:
             minP = minP
        else:
             minP = min(minP, i['phosphorus'])
        maxP = max(maxP, i['phosphorus'])
        sumK += i['potassium']
        if i['potassium'] == 0:
             minK = minK
        else:
             minK = min(minK, i['potassium'])
        maxK = max(maxK, i['potassium'])
        sumTemp += i['temperature']
        if i['temperature'] == 0:
             minTemp = minTemp
        else:
             minTemp = min(minTemp, i['temperature'])
        maxTemp = max(maxTemp, i['temperature'])
        sumHum += i['humidity']
        if i['humidity'] == 0:
             minHum = minHum
        else:
             minHum = min(minHum, i['humidity'])
        maxHum = max(maxHum, i['humidity'])
        sumPH += i['ph']
        if i['ph'] == 0:
             minPH = minPH
        else:
             minPH = min(minPH, i['ph'])
        maxPH = max(maxPH, i['ph'])
        sumSM += i['rainfall']
        if i['rainfall'] == 0:
             minSM = minSM
        else:
             minSM = min(minSM, i['rainfall'])
        maxSM = max(maxSM, i['rainfall'])
        avgN =  sumN/count 
        avgP = sumP/count 
        avgK = sumK/count 
        avgTemp = sumTemp/count 
        avgHum = sumHum/count 
        avgPH = sumPH/count 
        avgSM = sumSM/count 
watermelon = [{"name":"watermelon", "Nitrogen":avgN, "Min Nitrogen":minN, "Max Nitrogen":maxN, 
        "phosphorus":avgP, "Min phosphorus":minP, "Max phosphorus":maxP, 
        "potassium":avgK, "Min potassium":minK, "Max potassium":maxK, 
        "temperature":avgTemp, "Min temperature":minTemp, "Max temperature":maxTemp, 
        "humidity":avgHum, "Min humidity":minHum, "Max humidity":maxHum, 
        "pH":avgPH, "Min pH":minPH, "Max pH":maxPH, "soil moisture":avgSM, 
        "Min soil moisture":minSM, "Max soil moisture":maxSM, "selected":False}]


count = len(muskmelon)
sumN, avgN, minN, maxN = 0, 0, 1000, 0
sumP, avgP, minP, maxP = 0, 0, 1000, 0
sumK, avgK, minK, maxK = 0, 0, 1000, 0
sumTemp, avgTemp, minTemp, maxTemp = 0, 0, 1000, 0
sumHum, avgHum, minHum, maxHum = 0, 0, 1000, 0
sumPH, avgPH, minPH, maxPH = 0, 0, 1000, 0
sumSM, avgSM, minSM, maxSM = 0, 0, 1000, 0
for i in muskmelon:
        sumN += i['Nitrogen']
        if i['Nitrogen'] == 0:
             minN = minN
        else:
             minN = min(minN, i['Nitrogen'])
        maxN = max(maxN, i['Nitrogen'])
        sumP += i['phosphorus']
        if i['phosphorus'] == 0:
             minP = minP
        else:
             minP = min(minP, i['phosphorus'])
        maxP = max(maxP, i['phosphorus'])
        sumK += i['potassium']
        if i['potassium'] == 0:
             minK = minK
        else:
             minK = min(minK, i['potassium'])
        maxK = max(maxK, i['potassium'])
        sumTemp += i['temperature']
        if i['temperature'] == 0:
             minTemp = minTemp
        else:
             minTemp = min(minTemp, i['temperature'])
        maxTemp = max(maxTemp, i['temperature'])
        sumHum += i['humidity']
        if i['humidity'] == 0:
             minHum = minHum
        else:
             minHum = min(minHum, i['humidity'])
        maxHum = max(maxHum, i['humidity'])
        sumPH += i['ph']
        if i['ph'] == 0:
             minPH = minPH
        else:
             minPH = min(minPH, i['ph'])
        maxPH = max(maxPH, i['ph'])
        sumSM += i['rainfall']
        if i['rainfall'] == 0:
             minSM = minSM
        else:
             minSM = min(minSM, i['rainfall'])
        maxSM = max(maxSM, i['rainfall'])
        avgN =  sumN/count 
        avgP = sumP/count 
        avgK = sumK/count 
        avgTemp = sumTemp/count 
        avgHum = sumHum/count 
        avgPH = sumPH/count 
        avgSM = sumSM/count 
muskmelon = [{"name":"muskmelon", "Nitrogen":avgN, "Min Nitrogen":minN, "Max Nitrogen":maxN, 
        "phosphorus":avgP, "Min phosphorus":minP, "Max phosphorus":maxP, 
        "potassium":avgK, "Min potassium":minK, "Max potassium":maxK, 
        "temperature":avgTemp, "Min temperature":minTemp, "Max temperature":maxTemp, 
        "humidity":avgHum, "Min humidity":minHum, "Max humidity":maxHum, 
        "pH":avgPH, "Min pH":minPH, "Max pH":maxPH, "soil moisture":avgSM, 
        "Min soil moisture":minSM, "Max soil moisture":maxSM, "selected":False}]


count = len(apple)
sumN, avgN, minN, maxN = 0, 0, 1000, 0
sumP, avgP, minP, maxP = 0, 0, 1000, 0
sumK, avgK, minK, maxK = 0, 0, 1000, 0
sumTemp, avgTemp, minTemp, maxTemp = 0, 0, 1000, 0
sumHum, avgHum, minHum, maxHum = 0, 0, 1000, 0
sumPH, avgPH, minPH, maxPH = 0, 0, 1000, 0
sumSM, avgSM, minSM, maxSM = 0, 0, 1000, 0
for i in apple:
        sumN += i['Nitrogen']
        if i['Nitrogen'] == 0:
             minN = minN
        else:
             minN = min(minN, i['Nitrogen'])
        maxN = max(maxN, i['Nitrogen'])
        sumP += i['phosphorus']
        if i['phosphorus'] == 0:
             minP = minP
        else:
             minP = min(minP, i['phosphorus'])
        maxP = max(maxP, i['phosphorus'])
        sumK += i['potassium']
        if i['potassium'] == 0:
             minK = minK
        else:
             minK = min(minK, i['potassium'])
        maxK = max(maxK, i['potassium'])
        sumTemp += i['temperature']
        if i['temperature'] == 0:
             minTemp = minTemp
        else:
             minTemp = min(minTemp, i['temperature'])
        maxTemp = max(maxTemp, i['temperature'])
        sumHum += i['humidity']
        if i['humidity'] == 0:
             minHum = minHum
        else:
             minHum = min(minHum, i['humidity'])
        maxHum = max(maxHum, i['humidity'])
        sumPH += i['ph']
        if i['ph'] == 0:
             minPH = minPH
        else:
             minPH = min(minPH, i['ph'])
        maxPH = max(maxPH, i['ph'])
        sumSM += i['rainfall']
        if i['rainfall'] == 0:
             minSM = minSM
        else:
             minSM = min(minSM, i['rainfall'])
        maxSM = max(maxSM, i['rainfall'])
        avgN =  sumN/count 
        avgP = sumP/count 
        avgK = sumK/count 
        avgTemp = sumTemp/count 
        avgHum = sumHum/count 
        avgPH = sumPH/count 
        avgSM = sumSM/count 
apple = [{"name":"apple", "Nitrogen":avgN, "Min Nitrogen":minN, "Max Nitrogen":maxN, 
        "phosphorus":avgP, "Min phosphorus":minP, "Max phosphorus":maxP, 
        "potassium":avgK, "Min potassium":minK, "Max potassium":maxK, 
        "temperature":avgTemp, "Min temperature":minTemp, "Max temperature":maxTemp, 
        "humidity":avgHum, "Min humidity":minHum, "Max humidity":maxHum, 
        "pH":avgPH, "Min pH":minPH, "Max pH":maxPH, "soil moisture":avgSM, 
        "Min soil moisture":minSM, "Max soil moisture":maxSM, "selected":False}]


count = len(orange)
sumN, avgN, minN, maxN = 0, 0, 1000, 0
sumP, avgP, minP, maxP = 0, 0, 1000, 0
sumK, avgK, minK, maxK = 0, 0, 1000, 0
sumTemp, avgTemp, minTemp, maxTemp = 0, 0, 1000, 0
sumHum, avgHum, minHum, maxHum = 0, 0, 1000, 0
sumPH, avgPH, minPH, maxPH = 0, 0, 1000, 0
sumSM, avgSM, minSM, maxSM = 0, 0, 1000, 0
for i in orange:
        sumN += i['Nitrogen']
        if i['Nitrogen'] == 0:
             minN = minN
        else:
             minN = min(minN, i['Nitrogen'])
        maxN = max(maxN, i['Nitrogen'])
        sumP += i['phosphorus']
        if i['phosphorus'] == 0:
             minP = minP
        else:
             minP = min(minP, i['phosphorus'])
        maxP = max(maxP, i['phosphorus'])
        sumK += i['potassium']
        if i['potassium'] == 0:
             minK = minK
        else:
             minK = min(minK, i['potassium'])
        maxK = max(maxK, i['potassium'])
        sumTemp += i['temperature']
        if i['temperature'] == 0:
             minTemp = minTemp
        else:
             minTemp = min(minTemp, i['temperature'])
        maxTemp = max(maxTemp, i['temperature'])
        sumHum += i['humidity']
        if i['humidity'] == 0:
             minHum = minHum
        else:
             minHum = min(minHum, i['humidity'])
        maxHum = max(maxHum, i['humidity'])
        sumPH += i['ph']
        if i['ph'] == 0:
             minPH = minPH
        else:
             minPH = min(minPH, i['ph'])
        maxPH = max(maxPH, i['ph'])
        sumSM += i['rainfall']
        if i['rainfall'] == 0:
             minSM = minSM
        else:
             minSM = min(minSM, i['rainfall'])
        maxSM = max(maxSM, i['rainfall'])
        avgN =  sumN/count 
        avgP = sumP/count 
        avgK = sumK/count 
        avgTemp = sumTemp/count 
        avgHum = sumHum/count 
        avgPH = sumPH/count 
        avgSM = sumSM/count 
orange = [{"name":"orange", "Nitrogen":avgN, "Min Nitrogen":minN, "Max Nitrogen":maxN, 
        "phosphorus":avgP, "Min phosphorus":minP, "Max phosphorus":maxP, 
        "potassium":avgK, "Min potassium":minK, "Max potassium":maxK, 
        "temperature":avgTemp, "Min temperature":minTemp, "Max temperature":maxTemp, 
        "humidity":avgHum, "Min humidity":minHum, "Max humidity":maxHum, 
        "pH":avgPH, "Min pH":minPH, "Max pH":maxPH, "soil moisture":avgSM, 
        "Min soil moisture":minSM, "Max soil moisture":maxSM, "selected":False}]


count = len(papaya)
sumN, avgN, minN, maxN = 0, 0, 1000, 0
sumP, avgP, minP, maxP = 0, 0, 1000, 0
sumK, avgK, minK, maxK = 0, 0, 1000, 0
sumTemp, avgTemp, minTemp, maxTemp = 0, 0, 1000, 0
sumHum, avgHum, minHum, maxHum = 0, 0, 1000, 0
sumPH, avgPH, minPH, maxPH = 0, 0, 1000, 0
sumSM, avgSM, minSM, maxSM = 0, 0, 1000, 0
for i in papaya:
        sumN += i['Nitrogen']
        if i['Nitrogen'] == 0:
             minN = minN
        else:
             minN = min(minN, i['Nitrogen'])
        maxN = max(maxN, i['Nitrogen'])
        sumP += i['phosphorus']
        if i['phosphorus'] == 0:
             minP = minP
        else:
             minP = min(minP, i['phosphorus'])
        maxP = max(maxP, i['phosphorus'])
        sumK += i['potassium']
        if i['potassium'] == 0:
             minK = minK
        else:
             minK = min(minK, i['potassium'])
        maxK = max(maxK, i['potassium'])
        sumTemp += i['temperature']
        if i['temperature'] == 0:
             minTemp = minTemp
        else:
             minTemp = min(minTemp, i['temperature'])
        maxTemp = max(maxTemp, i['temperature'])
        sumHum += i['humidity']
        if i['humidity'] == 0:
             minHum = minHum
        else:
             minHum = min(minHum, i['humidity'])
        maxHum = max(maxHum, i['humidity'])
        sumPH += i['ph']
        if i['ph'] == 0:
             minPH = minPH
        else:
             minPH = min(minPH, i['ph'])
        maxPH = max(maxPH, i['ph'])
        sumSM += i['rainfall']
        if i['rainfall'] == 0:
             minSM = minSM
        else:
             minSM = min(minSM, i['rainfall'])
        maxSM = max(maxSM, i['rainfall'])
        avgN =  sumN/count 
        avgP = sumP/count 
        avgK = sumK/count 
        avgTemp = sumTemp/count 
        avgHum = sumHum/count 
        avgPH = sumPH/count 
        avgSM = sumSM/count 
papaya = [{"name":"papaya", "Nitrogen":avgN, "Min Nitrogen":minN, "Max Nitrogen":maxN, 
        "phosphorus":avgP, "Min phosphorus":minP, "Max phosphorus":maxP, 
        "potassium":avgK, "Min potassium":minK, "Max potassium":maxK, 
        "temperature":avgTemp, "Min temperature":minTemp, "Max temperature":maxTemp, 
        "humidity":avgHum, "Min humidity":minHum, "Max humidity":maxHum, 
        "pH":avgPH, "Min pH":minPH, "Max pH":maxPH, "soil moisture":avgSM, 
        "Min soil moisture":minSM, "Max soil moisture":maxSM, "selected":False}]


count = len(coconut)
sumN, avgN, minN, maxN = 0, 0, 1000, 0
sumP, avgP, minP, maxP = 0, 0, 1000, 0
sumK, avgK, minK, maxK = 0, 0, 1000, 0
sumTemp, avgTemp, minTemp, maxTemp = 0, 0, 1000, 0
sumHum, avgHum, minHum, maxHum = 0, 0, 1000, 0
sumPH, avgPH, minPH, maxPH = 0, 0, 1000, 0
sumSM, avgSM, minSM, maxSM = 0, 0, 1000, 0
for i in coconut:
        sumN += i['Nitrogen']
        if i['Nitrogen'] == 0:
             minN = minN
        else:
             minN = min(minN, i['Nitrogen'])
        maxN = max(maxN, i['Nitrogen'])
        sumP += i['phosphorus']
        if i['phosphorus'] == 0:
             minP = minP
        else:
             minP = min(minP, i['phosphorus'])
        maxP = max(maxP, i['phosphorus'])
        sumK += i['potassium']
        if i['potassium'] == 0:
             minK = minK
        else:
             minK = min(minK, i['potassium'])
        maxK = max(maxK, i['potassium'])
        sumTemp += i['temperature']
        if i['temperature'] == 0:
             minTemp = minTemp
        else:
             minTemp = min(minTemp, i['temperature'])
        maxTemp = max(maxTemp, i['temperature'])
        sumHum += i['humidity']
        if i['humidity'] == 0:
             minHum = minHum
        else:
             minHum = min(minHum, i['humidity'])
        maxHum = max(maxHum, i['humidity'])
        sumPH += i['ph']
        if i['ph'] == 0:
             minPH = minPH
        else:
             minPH = min(minPH, i['ph'])
        maxPH = max(maxPH, i['ph'])
        sumSM += i['rainfall']
        if i['rainfall'] == 0:
             minSM = minSM
        else:
             minSM = min(minSM, i['rainfall'])
        maxSM = max(maxSM, i['rainfall'])
        avgN =  sumN/count 
        avgP = sumP/count 
        avgK = sumK/count 
        avgTemp = sumTemp/count 
        avgHum = sumHum/count 
        avgPH = sumPH/count 
        avgSM = sumSM/count 
coconut = [{"name":"coconut", "Nitrogen":avgN, "Min Nitrogen":minN, "Max Nitrogen":maxN, 
        "phosphorus":avgP, "Min phosphorus":minP, "Max phosphorus":maxP, 
        "potassium":avgK, "Min potassium":minK, "Max potassium":maxK, 
        "temperature":avgTemp, "Min temperature":minTemp, "Max temperature":maxTemp, 
        "humidity":avgHum, "Min humidity":minHum, "Max humidity":maxHum, 
        "pH":avgPH, "Min pH":minPH, "Max pH":maxPH, "soil moisture":avgSM, 
        "Min soil moisture":minSM, "Max soil moisture":maxSM, "selected":False}]


count = len(cotton)
sumN, avgN, minN, maxN = 0, 0, 1000, 0
sumP, avgP, minP, maxP = 0, 0, 1000, 0
sumK, avgK, minK, maxK = 0, 0, 1000, 0
sumTemp, avgTemp, minTemp, maxTemp = 0, 0, 1000, 0
sumHum, avgHum, minHum, maxHum = 0, 0, 1000, 0
sumPH, avgPH, minPH, maxPH = 0, 0, 1000, 0
sumSM, avgSM, minSM, maxSM = 0, 0, 1000, 0
for i in cotton:
        sumN += i['Nitrogen']
        if i['Nitrogen'] == 0:
             minN = minN
        else:
             minN = min(minN, i['Nitrogen'])
        maxN = max(maxN, i['Nitrogen'])
        sumP += i['phosphorus']
        if i['phosphorus'] == 0:
             minP = minP
        else:
             minP = min(minP, i['phosphorus'])
        maxP = max(maxP, i['phosphorus'])
        sumK += i['potassium']
        if i['potassium'] == 0:
             minK = minK
        else:
             minK = min(minK, i['potassium'])
        maxK = max(maxK, i['potassium'])
        sumTemp += i['temperature']
        if i['temperature'] == 0:
             minTemp = minTemp
        else:
             minTemp = min(minTemp, i['temperature'])
        maxTemp = max(maxTemp, i['temperature'])
        sumHum += i['humidity']
        if i['humidity'] == 0:
             minHum = minHum
        else:
             minHum = min(minHum, i['humidity'])
        maxHum = max(maxHum, i['humidity'])
        sumPH += i['ph']
        if i['ph'] == 0:
             minPH = minPH
        else:
             minPH = min(minPH, i['ph'])
        maxPH = max(maxPH, i['ph'])
        sumSM += i['rainfall']
        if i['rainfall'] == 0:
             minSM = minSM
        else:
             minSM = min(minSM, i['rainfall'])
        maxSM = max(maxSM, i['rainfall'])
        avgN =  sumN/count 
        avgP = sumP/count 
        avgK = sumK/count 
        avgTemp = sumTemp/count 
        avgHum = sumHum/count 
        avgPH = sumPH/count 
        avgSM = sumSM/count 
cotton = [{"name":"cotton", "Nitrogen":avgN, "Min Nitrogen":minN, "Max Nitrogen":maxN, 
        "phosphorus":avgP, "Min phosphorus":minP, "Max phosphorus":maxP, 
        "potassium":avgK, "Min potassium":minK, "Max potassium":maxK, 
        "temperature":avgTemp, "Min temperature":minTemp, "Max temperature":maxTemp, 
        "humidity":avgHum, "Min humidity":minHum, "Max humidity":maxHum, 
        "pH":avgPH, "Min pH":minPH, "Max pH":maxPH, "soil moisture":avgSM, 
        "Min soil moisture":minSM, "Max soil moisture":maxSM, "selected":False}]


count = len(jute)
sumN, avgN, minN, maxN = 0, 0, 1000, 0
sumP, avgP, minP, maxP = 0, 0, 1000, 0
sumK, avgK, minK, maxK = 0, 0, 1000, 0
sumTemp, avgTemp, minTemp, maxTemp = 0, 0, 1000, 0
sumHum, avgHum, minHum, maxHum = 0, 0, 1000, 0
sumPH, avgPH, minPH, maxPH = 0, 0, 1000, 0
sumSM, avgSM, minSM, maxSM = 0, 0, 1000, 0
for i in jute:
        sumN += i['Nitrogen']
        if i['Nitrogen'] == 0:
             minN = minN
        else:
             minN = min(minN, i['Nitrogen'])
        maxN = max(maxN, i['Nitrogen'])
        sumP += i['phosphorus']
        if i['phosphorus'] == 0:
             minP = minP
        else:
             minP = min(minP, i['phosphorus'])
        maxP = max(maxP, i['phosphorus'])
        sumK += i['potassium']
        if i['potassium'] == 0:
             minK = minK
        else:
             minK = min(minK, i['potassium'])
        maxK = max(maxK, i['potassium'])
        sumTemp += i['temperature']
        if i['temperature'] == 0:
             minTemp = minTemp
        else:
             minTemp = min(minTemp, i['temperature'])
        maxTemp = max(maxTemp, i['temperature'])
        sumHum += i['humidity']
        if i['humidity'] == 0:
             minHum = minHum
        else:
             minHum = min(minHum, i['humidity'])
        maxHum = max(maxHum, i['humidity'])
        sumPH += i['ph']
        if i['ph'] == 0:
             minPH = minPH
        else:
             minPH = min(minPH, i['ph'])
        maxPH = max(maxPH, i['ph'])
        sumSM += i['rainfall']
        if i['rainfall'] == 0:
             minSM = minSM
        else:
             minSM = min(minSM, i['rainfall'])
        maxSM = max(maxSM, i['rainfall'])
        avgN =  sumN/count 
        avgP = sumP/count 
        avgK = sumK/count 
        avgTemp = sumTemp/count 
        avgHum = sumHum/count 
        avgPH = sumPH/count 
        avgSM = sumSM/count 
jute = [{"name":"jute", "Nitrogen":avgN, "Min Nitrogen":minN, "Max Nitrogen":maxN, 
        "phosphorus":avgP, "Min phosphorus":minP, "Max phosphorus":maxP, 
        "potassium":avgK, "Min potassium":minK, "Max potassium":maxK, 
        "temperature":avgTemp, "Min temperature":minTemp, "Max temperature":maxTemp, 
        "humidity":avgHum, "Min humidity":minHum, "Max humidity":maxHum, 
        "pH":avgPH, "Min pH":minPH, "Max pH":maxPH, "soil moisture":avgSM, 
        "Min soil moisture":minSM, "Max soil moisture":maxSM, "selected":False}]


count = len(coffee)
sumN, avgN, minN, maxN = 0, 0, 1000, 0
sumP, avgP, minP, maxP = 0, 0, 1000, 0
sumK, avgK, minK, maxK = 0, 0, 1000, 0
sumTemp, avgTemp, minTemp, maxTemp = 0, 0, 1000, 0
sumHum, avgHum, minHum, maxHum = 0, 0, 1000, 0
sumPH, avgPH, minPH, maxPH = 0, 0, 1000, 0
sumSM, avgSM, minSM, maxSM = 0, 0, 1000, 0
for i in coffee:
        sumN += i['Nitrogen']
        if i['Nitrogen'] == 0:
             minN = minN
        else:
             minN = min(minN, i['Nitrogen'])
        maxN = max(maxN, i['Nitrogen'])
        sumP += i['phosphorus']
        if i['phosphorus'] == 0:
             minP = minP
        else:
             minP = min(minP, i['phosphorus'])
        maxP = max(maxP, i['phosphorus'])
        sumK += i['potassium']
        if i['potassium'] == 0:
             minK = minK
        else:
             minK = min(minK, i['potassium'])
        maxK = max(maxK, i['potassium'])
        sumTemp += i['temperature']
        if i['temperature'] == 0:
             minTemp = minTemp
        else:
             minTemp = min(minTemp, i['temperature'])
        maxTemp = max(maxTemp, i['temperature'])
        sumHum += i['humidity']
        if i['humidity'] == 0:
             minHum = minHum
        else:
             minHum = min(minHum, i['humidity'])
        maxHum = max(maxHum, i['humidity'])
        sumPH += i['ph']
        if i['ph'] == 0:
             minPH = minPH
        else:
             minPH = min(minPH, i['ph'])
        maxPH = max(maxPH, i['ph'])
        sumSM += i['rainfall']
        if i['rainfall'] == 0:
             minSM = minSM
        else:
             minSM = min(minSM, i['rainfall'])
        maxSM = max(maxSM, i['rainfall'])
        avgN =  sumN/count 
        avgP = sumP/count 
        avgK = sumK/count 
        avgTemp = sumTemp/count 
        avgHum = sumHum/count 
        avgPH = sumPH/count 
        avgSM = sumSM/count 
coffee = [{"name":"coffee", "Nitrogen":avgN, "Min Nitrogen":minN, "Max Nitrogen":maxN, 
        "phosphorus":avgP, "Min phosphorus":minP, "Max phosphorus":maxP, 
        "potassium":avgK, "Min potassium":minK, "Max potassium":maxK, 
        "temperature":avgTemp, "Min temperature":minTemp, "Max temperature":maxTemp, 
        "humidity":avgHum, "Min humidity":minHum, "Max humidity":maxHum, 
        "pH":avgPH, "Min pH":minPH, "Max pH":maxPH, "soil moisture":avgSM, 
        "Min soil moisture":minSM, "Max soil moisture":maxSM, "selected":False}]

crops = rice + maize + chickpea + kidneybeans + pigeonpeas + mothbeans + mungbean + blackgram + lentil + pomegranate + banana + mango + grapes + watermelon + muskmelon + apple + orange + papaya + coconut + cotton + jute + coffee

print(crops)

# Convert the list of dictionaries to a DataFrame
df = pd.DataFrame(crops)

# Write the DataFrame to an Excel file
df.to_excel("mongoDB_Kaggle_Data.xlsx", index=False)  # index=False to exclude the row index

print("Excel file generated successfully: mongoDB_Kaggle_Data.xlsx")


def insertCrop():
     '''INSERT KAGGLE DATASET INTO CROPS COLLECTION'''
     try:
          # Insert the documents into the collection
          result = collection.insert_many(crops)
          # Print the IDs of inserted documents
          print("Inserted document IDs:", result.inserted_ids)
     except Exception as e:
          msg = str(e)
          print("insertCrop error ",msg)
     else:
          print("insertCrop success")
          return result
     

#insertCrop()


        