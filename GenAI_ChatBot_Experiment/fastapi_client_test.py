import requests as rq

url="http://127.0.0.1:8000/sum"

data={"number1":11,"number2":18}

response=rq.post(url,json=data)

if response.status_code==200:
    print("Success",response.json())
else:
    print("Failed",response.status_code)