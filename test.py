import requests
import json
import uuid

url = "https://seorwrpmwh.execute-api.us-east-1.amazonaws.com/prod/mp3-lexv2-autograder"

payload = {
	"graphApi": "https://4ts3u0t3n4.execute-api.us-east-1.amazonaws.com/prod/resource",
	"botId": "DQBDPUYSGI", 
	"botAliasId": "13LNCZRBPJ",
	"identityPoolId": "us-east-1:1468af77-b656-4422-a43b-bfd147b9d697",
	"accountId": "471112919901",
	"submitterEmail": "qifanz3@illinois.edu",
	"secret": "HRtsbdd0j8PiwjEU",
	"region": "us-east-1" #<Region where your lex is deployed (Ex: us-east-1)>
    }

r = requests.post(url, data=json.dumps(payload))

print(r.status_code, r.reason)
print(r.text)
