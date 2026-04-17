import threading
import requests

URL = "http://127.0.0.1:5000/recommend/1"

def hit_api():
    try:
        res = requests.get(URL)
        print(res.status_code)
    except:
        print("Error")

threads = []

for _ in range(10):  # simulate 10 users
    t = threading.Thread(target=hit_api)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("Load test completed")