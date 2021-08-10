import requests
from app import *

HOST = 'http://127.0.0.1:5000'

def test2():
    pload = { "queries": ["dates"] }
    r = requests.get(
        HOST + "/stats", 
        json = pload
    )
    assert(r.status_code == 200)
    print("test dates:", json.loads(r.text))
    

if __name__ == "__main__":
    test2()