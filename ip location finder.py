import requests

user_api = 'https://api.ipify.org?format=json'

response = requests.get(user_api)

if response.status_code ==200:
    data = response.json()
    ip = data.get('ip')


user_location_api = f'https://ipapi.co/{ip}/json/'

r = requests.get(user_location_api)
if r.status_code ==200:
    ipdata = r.json()
    city = ipdata.get('city')
    region = ipdata.get('region')
    country_name = ipdata.get('country_name')
    country_code = ipdata.get('country_code')
    country_capital = ipdata.get('country_capital')
    timezone = ipdata.get('timezone')
    currency = ipdata.get('currency')
    country_calling_code = ipdata.get('country_calling_code')
    currency_name = ipdata.get('currency_name')

sentence = f'My name is Sani from {city}, {region}, {country_name}. my country code is {country_code}, where capital ' \
           f'is {country_capital} ' \
           f'and ' \
           f'{timezone} is and {currency} is if you are reach me via call you should add {country_calling_code} before the main ' \
           f'number. {country_name} currency name is {currency_name}'


print(sentence)
