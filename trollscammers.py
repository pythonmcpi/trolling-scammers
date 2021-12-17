import requests
import random
import string
import os
from itertools import cycle

def randomString(stringLength=8):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

def fakePassword(length = 16):
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()`~-=_+[]{}\\|/?,.<>'
    return ''.join(random.choice(letters) for i in range(length))

def randomToken(length = 57):
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    return ''.join(random.choice(letters) for i in range(length))

with open("1names.txt") as f:
    numedefamilie = f.readlines()

numedefamilie = [x.strip() for x in numedefamilie]

with open("lnames.txt") as f:
    prenume = f.readlines()

prenume = [x.strip() for x in prenume]

domain = "discord-app.net"
lumen_token = "IDpAuVfaeaTzGLpVbyhoog71da0w7WppYfe0MyfY"
ref_token = "zq6I4NsG2TWrYCVlESDjbd4a5a8d2X14VeTz21EP2Y1Kc15dgCqQwiNsj"

while True:

    numef_n = random.choice(numedefamilie)
    prenume_n = random.choice(prenume)

    username = numef_n + prenume_n
    username = username.lower()

    password = randomString()
    
   # random_token = randomToken()

    url = f'https://{domain}/login/dologin'
    obj = {'username' : username, 'password' : password}
    headers = {'authority' : domain, 'method' : 'POST', 'path' : '/login/dologin', 'scheme' : 'https', 'accept' : '*/*', 'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36', 'accept-encoding' : 'gzip, deflate, br', 'accept-language' : 'en-US,en;q=0.9', 'content-length' : '31', 'content-type' : 'application/x-www-form-urlencoded; charset=UTF-8', 'cookie' : f'lumen_session={lumen_token}; _TDG=6f527f8d338c0c8896253111fd986ed6; timezoneOffset=25200,0', 'origin' : f'https://{domain}', 'referer' : f'https://{domain}/{ref_token}', 'sec-fetch-dest' : 'empty', 'sec-fetch-mode' : 'cors', 'sec-fetch-site' : 'same-origin', 'x-requested-with' : 'XMLHttpRequest'} #if needed
    
    try:
        r = requests.post(url, data=obj, headers=headers)
    except requests.ConnectionError as e:
        print(f"{type(e).__name__}: {e} using {username}:{password}")
    else:
        print(f"POST {r.status_code} {r.reason} using {username}:{password}")
