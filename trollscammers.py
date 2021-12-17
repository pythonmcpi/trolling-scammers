import requests
import random
import string
import os
from itertools import cycle
import time
import math

def randomString(stringLength=8):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

def fakePassword(length = 16):
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()`~-=_+[]{}\\|/?,.<>'
    return ''.join(random.choice(letters) for i in range(length))

def randomToken(length = 57):
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    return ''.join(random.choice(letters) for i in range(length))

def randomBase64(length = 1685):
    charset = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890+/'
    return ''.join(random.choice(charset) for i in range(length))

with open("1names.txt") as f:
    numedefamilie = f.readlines()

numedefamilie = [x.strip() for x in numedefamilie]

with open("lnames.txt") as f:
    prenume = f.readlines()

prenume = [x.strip() for x in prenume]

domain = "nitro-get.xyz"
path = "/login"
proto = "https"
method = "POST" # Edit the requests.METHOD call too
ref_token = "login"

sends = 0
spinner = '/-\\|' # eye candy lol
start = time.time()

while True:

    #numef_n = random.choice(numedefamilie)
    #prenume_n = random.choice(prenume)

    #username = numef_n + prenume_n
    #username = username.lower()

    #password = randomString()
    
   # random_token = randomToken()

    url = f'{proto}://{domain}{path}'
    #obj = {'username' : username, 'password' : password}
    obj = randomBase64()
    headers = {'host' : domain,
               'origin': f"{proto}://{domain}",
               'method' : method,
               'path' : path,
               'scheme' : proto,
               'accept' : '*/*',
               'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
               'accept-encoding' : 'gzip, deflate, br',
               'accept-language' : 'en-US,en;q=0.9',
               'content-length' : '1687',
               'content-type' : 'application/json',
               'cookie' : 'ln=english; cookies=true; session=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkb21haW5QYXRoIjoiTmV3X3llYXIiLCJyZWYiOjMxMCwiYm90RGF0YSI6IjE4OC4xMjAuMjQ5LjE1NToyMDAwMiIsImlhdCI6MTYzOTcwNDQwNiwidmlldyI6dHJ1ZX0.mSkMKpeQ7KHkAPGHFsopM8qgZldJzQAjcBDswCyxeM8; timezoneOffset=-28800,0; _ga=GA1.2.14677122.1639704448; _gid=GA1.2.1181044151.1639704448',
               'origin' : f'https://{domain}',
               'referer' : f'https://{domain}/{ref_token}',
               'sec-fetch-dest' : 'empty',
               'sec-fetch-mode' : 'cors',
               'sec-fetch-site' : 'same-origin',
               'x-requested-with' : 'XMLHttpRequest'
    } #if needed
    
    try:
        r = requests.post(url, data=obj, headers=headers)
    except requests.ConnectionError as e:
        print(f"(#{sends}) {type(e).__name__}: {e}")
    else:
        sends += 1
        elapsed = time.time() - start
        print(f"POST {r.status_code} {r.reason} (#{sends}) [{math.floor(elapsed // 3600)}:{'0' if elapsed // 60 < 10 else ''}{math.floor(elapsed // 60)}:{'0' if elapsed % 60 < 10 else ''}{math.floor(elapsed % 60)}] {spinner[sends % 4]}", end='\r')
