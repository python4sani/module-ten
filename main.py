import requests

response_url = requests.get('https://jsonplaceholder.typicode.com/posts')

print(response_url.status_code)
print(response_url.json())