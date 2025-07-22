import requests


cookies = {
    
}

headers = {
    "Accept": "application/json",
    "X-XSRF-TOKEN": cookies.get("XSRF-TOKEN")
}

response = requests.get(url, headers=headers, cookies=cookies)

print("Status code:", response.status_code)
print("Response text:", response.text)
