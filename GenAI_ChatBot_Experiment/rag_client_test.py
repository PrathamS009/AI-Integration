import requests as rq

url="http://127.0.0.1:8000"

query_string="ASK YOUR QUESTION HERE"

response=rq.post(url,json={"question":query_string})

if response.status_code==200:
    print("Success",response.json())
else:
    print("Failed",response.status_code)