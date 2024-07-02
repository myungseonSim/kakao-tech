import requests

response = requests.get("https://naver.com")

print(response.status_code)
print(response.text)
