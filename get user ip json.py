import requests

user_url = 'https://api.ipify.org?format=json'

response = requests.get(user_url)

# print(response.status_code)
# print(response.json())
if response.status_code == 200:
    data = response.json()
    ip = data.get('ip')
    print('Your Ip Address Is',ip)