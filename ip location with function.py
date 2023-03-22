import requests

user_api = 'https://api.ipify.org?format=json'

def res_data(url):
    res = requests.get(url)
    if res.status_code == 200:
        deta = res.json()
    return deta

# response = requests.get(user_api)
#
# if response.status_code ==200:
#     data = response.json()
deta = res_data(user_api)
ip = deta.get('ip')


user_location_api = f'https://ipapi.co/{ip}/json/'


# r = requests.get(user_location_api)
# if r.status_code ==200:
#     ipdata = r.json()
ipdata = res_data(user_location_api)
city = ipdata.get('city')
region = ipdata.get('region')
country_name = ipdata.get('country_name')
sentence = f'My name is Sani from {city}'



print(sentence)
