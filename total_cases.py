from app import *
import requests

HOST = 'http://127.0.0.1:5000'

def test3():
    pload = { "queries": ["total_cases"] }
    r = requests.get(
        HOST + "/stats", 
        json = pload
    )
    assert(r.status_code == 200)
    print("test 3 total_cases:", json.loads(r.text))



    

if __name__ == "__main__":
    test3()