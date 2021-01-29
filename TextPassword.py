import requests
key = '2d794c6f46094ceb96bd719c1c26c984'
url = 'https://randommer.io/api/Text/Password'

h = {'X-Api-Key': key}
p = {
    'length': 5,
    'hasDigits': 'true',
    'hasUppercase': 'true',
    'hasSpecial': 'true'
}
r = requests.get(url, params=p, headers=h)
print(r.status_code)
print(r.url)
print(r.json())
