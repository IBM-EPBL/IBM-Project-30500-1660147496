import requests
import json
# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "juc9T5KAkFdmG-PfwQcmwKNpafHTvq2xxn5KA8c5LBj2"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey": API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

# NOTE: manually define and pass the array(s) of values to be scored in the next line
payload_scoring = {"input_data": [{"field": [["f0","f1","f2","f3","f4","f5","f6","f7","f8","f9","f10","f11","f12","f13","f14","f15","f16","f17","f18","f19","f20","f21","f22","f23","f24","f25","f26","f27","f28","f29"]], "values": [[1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, 1, -1, 0, -1, -1, 1, 1, 1, 1, 1, 1, 1, -1, 1, 1, 1, -1, 1, 1]]}]}

response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/f5d3868f-1645-4e07-b81f-bfd85810fce3/predictions?version=2022-11-18', json=payload_scoring,headers={'Authorization': 'Bearer ' + mltoken})
print("Scoring response")
print(response_scoring.json())

predictions=response_scoring.json()

pred=print(predictions['predictions'][0]['values'][0][0])
if(pred != 1):
         print("This is a Legitimate Website.")
else:
         print("This is a fake phishing website")