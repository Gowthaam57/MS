import json,requests


url="http://0.0.0.0:5005/webhooks/rest/webhook?format=json"
obj={"message":"restart","sender":"g"}
response=requests.post(url,data=json.dumps(obj))
# print("a",response.status_code)
# print("b",response.text)
print(response.json())