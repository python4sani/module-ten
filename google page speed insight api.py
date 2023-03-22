import requests
api_key = 'AIzaSyDGxDv9KrDwClQ0RKfDEN_ZEGJKGTeF42I'

test_url = input('Enter Your url: ')
api_url = f'https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={test_url}&key={api_key}'

res = requests.get(api_url)

if res.status_code == 200:
    data = res.json()
    cls_data = data.get('loadingExperience').get('metrics').get('FIRST_CONTENTFUL_PAINT_MS').get('percentile')
    #cls_data = data.get('lighthouseResult').get('environment').get('benchmarkIndex')
    print(cls_data)
else:
    print('something is wrong')