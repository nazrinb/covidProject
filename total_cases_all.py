from app import *
import requests

HOST = 'http://127.0.0.1:5000'

def test6():
    pload = { "queries": ["total_cases_all_time"] }
    r = requests.get(
        HOST + "/stats", 
        json = pload
    )
    assert(r.status_code == 200)
    print("test 5 total_cases_all_time:", json.loads(r.text))



    

if __name__ == "__main__":
    test6()