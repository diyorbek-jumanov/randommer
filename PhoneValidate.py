import requests
key = '2d794c6f46094ceb96bd719c1c26c984'
url = 'https://randommer.io/api/Phone/Validate'

h = {'X-Api-Key': key}
p = {
    'telephone': 'xxxxxxxx',
    'CountryCode': 'en'
}
r = requests.get(url, params=p, headers=h)

print(r.url)
print(r.json())
