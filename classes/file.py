import requests

url = "https://inquiry.mof.gov.ly/api/me"

cookies = {
    "khdm_alastaalam_ozar_almaly_se...": "eyJpd...long_token_here...",
    "XSRF-TOKEN": "eyJpd...long_token_here..."
}

headers = {
    "Accept": "application/json",
    "X-XSRF-TOKEN": cookies.get("XSRF-TOKEN")
}

response = requests.get(url, headers=headers, cookies=cookies)

print("Status code:", response.status_code)
print("Response text:", response.text)
