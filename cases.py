import pandas as pd 
import requests
import urllib2
import csv
import io

url = 'https://covid.ourworldindata.org/data/owid-covid-data.csv'
response = urllib2.urlopen(url)
cr = csv.reader(response)
s=requests.get(url).content
c=pd.read_csv(io.StringIO(s.decode('utf-8')))

for row in cr:
    print(row)

