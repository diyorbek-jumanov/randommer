import requests
key = '2d794c6f46094ceb96bd719c1c26c984'
url = 'https://randommer.io/api/Text/LoremIpsum'

h = {'X-Api-Key': key}
p = {
    'loremType': 'normal',
    'type': 'words',
    'number': 1
}
r = requests.get(url, params=p, headers=h)

print(r.url)
print(r.json())
