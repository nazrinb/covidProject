from urllib.request import urlopen
from flask import Flask, request

import numpy as np
import pandas as pd 
import requests
import json
import csv
import io


app = Flask(__name__)

# Get the daily stats for Azerbaijan from World Bank
url = 'https://covid.ourworldindata.org/data/owid-covid-data.csv'
response = urlopen(url)
s = requests.get(url).content

df = pd.read_csv(io.StringIO(s.decode('utf-8')))
df_aze = df.loc[df["location"] == "Azerbaijan", :]

# http://127.0.0.1:5000/
@app.route('/')
def home():
    return "Welcome to COVID-19 Project"

# http://127.0.0.1:5000/new_cases
@app.route('/stats', methods=["GET"])
def get_new_cases():
    pload = request.get_json()
    if pload is None or "queries" not in pload.keys():
        return "Bad Query", 400
     
    queries = pload["queries"]

    res = {}
    if "new_cases_today" in queries:
        res["new_cases_today"] = get_new_cases_today()
    if "new_deaths" in queries:
        res["new_deaths"] = get_new_deaths_today() 
    if "total_cases" in queries:
        res["total_cases"] = get_total_cases_today() 
    if "total_deaths" in queries:
        res["total_deaths"] = get_total_deaths_today() 
    if "new_cases_all_time" in queries:
        res["new_cases_all_time"] = get_new_cases_all_time()
    if "new_deaths_all_time" in queries:
        res["new_deaths_all_time"] = get_new_deaths_all_time()
    if "total_cases_all_time" in queries:
        res["total_cases_all_time"] = get_total_cases_all_time()
    if "total_deaths_all_time" in queries:
        res["total_deaths_all_time"] = get_total_deaths_all_time()
    if "dates" in queries:
        res["dates"] = get_dates_all_time()
        
    return json.dumps(res), 200

def get_new_cases_today():
    return df_aze.iloc[-1]["new_cases"]

def get_new_deaths_today():
    return df_aze.iloc[-1]["new_deaths"]

def get_total_cases_today():
    return df_aze.iloc[-1]["total_cases"]

def get_total_deaths_today():
    return df_aze.iloc[-1]["total_deaths"]

def get_new_cases_all_time():
    return df_aze.loc[:, "new_cases"].to_list()

def get_new_deaths_all_time():
    return df_aze.loc[:, "new_deaths"].to_list()

def get_total_cases_all_time():
    return df_aze.loc[:, "total_cases"].to_list()

def get_total_deaths_all_time():
    df_aze.fillna(0)
    return df_aze.loc[:, "total_deaths"].to_list()
    

def get_dates_all_time():
    return df_aze.loc[:, "date"].to_list()

# {
#     "new_cases_today": 212,
#     "new_cases_all_time": [3, 0, 0, 3, 0, 0, 2, 1, 0, ...],
#     "dates_all_time": ["3/1/20", "3/3/20", "3/3/20", ...]
# }

if __name__ == "__main__":
    app.run(debug=True)