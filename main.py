import requests
key = '2d794c6f46094ceb96bd719c1c26c984'
headers = {'X-Api-Key': key}
url = 'https://randommer.io/api/Card'
r = requests.get(url, headers=headers)
print(r.url)
