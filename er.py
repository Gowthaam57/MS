import json,requests

url="http://0.0.0.0:5005/webhooks/rest/webhook"
obj={"message":"business idea"}
response= requests.post(url,data=json.dumps(obj))
print(response.json())