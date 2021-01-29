import requests
key = '2d794c6f46094ceb96bd719c1c26c984'
url = 'https://randommer.io/api/Name'

h = {'X-Api-Key': key}
query = {
    'nameType': 'firstname',
    'quantity': 1
}
r = requests.get(url, params=query, headers=h)

print(r.url)
print(r.json())
