import requests
from app import *

HOST = 'http://127.0.0.1:5000'

def test2():
    pload = { "queries": ["total_deaths_all_time"] }
    r = requests.get(
        HOST + "/stats", 
        json = pload
    )
    assert(r.status_code == 200)
    print("test 2 new_deaths:", json.loads(r.text))
    

if __name__ == "__main__":1
    test2()