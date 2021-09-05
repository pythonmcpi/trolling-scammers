import requests
import random
import string
import os

def randomString(stringLength=8):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

with open("1names.txt") as f:
    numedefamilie = f.readlines()

numedefamilie = [x.strip() for x in numedefamilie]

with open("lnames.txt") as f:
    prenume = f.readlines()

prenume = [x.strip() for x in prenume]

while True:

    numef_n = random.choice(numedefamilie)
    prenume_n = random.choice(prenume)

    username = numef_n + prenume_n
    username = username.lower()

    password = randomString()

    url = 'https://steamnltros.ru/login/dologin'
    obj = {'username' : username, 'password' : password}
    headers = {'authority' : 'steamn1tros.ru', 'method' : 'POST', 'path' : '/login/dologin', 'scheme' : 'https', 'accept' : '*/*', 'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36', 'accept-encoding' : 'gzip, deflate, br', 'accept-language' : 'en-US,en;q=0.9', 'content-length' : '31', 'content-type' : 'application/x-www-form-urlencoded; charset=UTF-8', 'cookie' : 'lumen_session=EnrSREZKKzulSKwxxb5WOSkMKdnxhRXlulYGGFxt; _TDG=6f527f8d338c0c8896253111fd986ed6; timezoneOffset=25200,0', 'origin' : 'https://steamnltros.ru', 'referer' : 'ttps://steamnltros.ru/wjrKzQCnD0Oyol9a1R2ntkOKci7nbd4a5a8d2kvoszITw9Ussl84QlKy8', 'sec-fetch-dest' : 'empty', 'sec-fetch-mode' : 'cors', 'sec-fetch-site' : 'same-origin', 'x-requested-with' : 'XMLHttpRequest'} #if needed

    r = requests.post(url, data=obj, headers=headers)
    
    print(f"POST {r.status_code} {r.reason} using {username}:{password}")
