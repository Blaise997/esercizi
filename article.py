import requests

API_KEY = 'YOUR_API_KEY'
TOPIC = 'Technology'

url = f'https://newsapi.org/v2/everything?q={TOPIC}&apiKey={API_KEY}'

response = requests.get(url)
data = response.json()

if data['status'] == 'ok':
    articles = data['articles']
    for article in articles:
        print(article['title'])
else:
    print('Error fetching data:', data['message'])

