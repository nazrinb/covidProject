from app import *
import requests

HOST = 'http://127.0.0.1:5000'

def test1():
    pload = { "queries": ["new_cases_today"] }
    r = requests.get(
        HOST + "/stats", 
        json = pload

    )
    assert(r.status_code == 200)
    print("test 1:", json.loads(r.text))



if __name__ == "__main__":
    test1()