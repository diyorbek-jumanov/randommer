import requests
key = '2d794c6f46094ceb96bd719c1c26c984'
url = 'https://randommer.io/api/Misc/Cultures'

h = {'X-Api-Key': key}
r = requests.get(url, headers=h)

print(r.url)
print(r.json())
