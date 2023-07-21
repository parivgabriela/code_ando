# demo of another kind of chatgpt

import requests

url = "https://api.writesonic.com/v2/business/content/chatsonic?engine=premium&language=en"

payload = {
    "enable_google_results": "true",
    "enable_memory": False
}
headers = {
    "accept": "application/json",
    "content-type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)