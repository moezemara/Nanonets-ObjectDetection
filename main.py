import requests
import urllib
import json

url = "http://192.168.1.12:8080/shot.jpg"


urllib.request.urlretrieve(url, 'image.jpg')

url = 'https://app.nanonets.com/api/v2/ObjectDetection/Model/de3848e2-3d51-4863-baac-8983bfa0d33c/LabelFile/'

data = {'file': open('image.jpg', 'rb')}

response = requests.post(url, auth=requests.auth.HTTPBasicAuth('-62qCGLTC_sgdy6RMkx6k644C68Ea1bF', ''), files=data)

json_resp = (json.loads(response.text))

print(response.text)
print('============================================')
print(json.dumps(json_resp, indent=4,sort_keys=True))
print('============================================')
#print(json_resp['score'])
print('============================================')
print(response.json().get('prediction'))