import requests

key = '2d794c6f46094ceb96bd719c1c26c984'
url = 'https://randommer.io/api/Name/Suggestions'

h = {'X-Api-Key': key}
query = {'startingWords': 'Rose'}

r = requests.get(url, params=query, headers=h)

print(r.url)
print(r.json())
