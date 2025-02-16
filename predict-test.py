#!/usr/bin/env python
# coding: utf-8



import requests

host = 'churn-serving-env.eba-j648gpbv.eu-central-1.elasticbeanstalk.com'
url = f'http://{host}/predict'
# url = 'http://localhost:9696/predict'



customer = {
    "gender": "male",
    "seniorcitizen": 0,
    "partner": "yes",
    "dependents": "no",
    "phoneservice": "no",
    "multiplelines": "no_phone_service",
    "internetservice": "dsl",
    "onlinesecurity": "no",
    "onlinebackup": "yes",
    "deviceprotection": "no",
    "techsupport": "no",
    "streamingtv": "no",
    "streamingmovies": "no",
    "contract": "month-to-month",
    "paperlessbilling": "yes",
    "paymentmethod": "electronic_check",
    "tenure": 1,
    "monthlycharges": 29.85,
    "totalcharges":   (24 * 12.85)
}


responce = requests.post(url, json=customer).json()

print(responce)
