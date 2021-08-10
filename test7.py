from app import *
import requests

HOST = 'http://127.0.0.1:5000'

def test7():
    pload = { "queries": ["new_deaths_all_time"] }
    r = requests.get(
        HOST + "/stats", 
        json = pload
    )
    assert(r.status_code == 200)
    
    print("test 7 new_deaths_all_time:", json.loads(r.text))




    

if __name__ == "__main__":
    test7()