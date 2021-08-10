from app import *
import requests

HOST = 'http://127.0.0.1:5000'

def test4():
    pload = { "queries": ["total_deaths"] }
    r = requests.get(
        HOST + "/stats", 
        json = pload
    )
    assert(r.status_code == 200)
    print("test 4 total_deaths:", json.loads(r.text))
    print(df_aze)



    

if __name__ == "__main__":
    test4()