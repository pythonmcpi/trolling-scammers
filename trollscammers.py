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

domain = "dfscord.com"
path = "/login"
proto = "https"
method = "POST" # Edit the requests.METHOD call too
ref_token = "login"

sends = 0
spinner = '/-\\|' # eye candy lol
start = time.time()

while True:

    numef_n = random.choice(numedefamilie)
    prenume_n = random.choice(prenume)

    username = numef_n + prenume_n
    username = username.lower()

    password = randomString()
    
   # random_token = randomToken()

    url = f'{proto}://{domain}{path}'
    #obj = {'username' : username, 'password' : password}
    #obj = randomBase64()
    obj = {
        "headers": "fic1Jz8nNnJ8MzNzMzR/cCcpJzQnPydrZ2F2fXV1MDMnKSc3Jz8nd2wxMGtiNWk0JyknNic/J3ZgMWJgNn19dXUnKScxJz8nc3w0cDQ2b25kJyknMCc/J3R2NjE9YGd3NzInKSczJz8ndnVma3xwYTBmYCcpJzInPydtbWR3MWFpMmJvJyknPSc/J2FvZGJgcW02fycpJzwnPycxPTI3ajx1b3ZkJyknNDUnPyd2d3Btcz1pY2szJyknNDQnPydgb2g0dWJnZGpxJyknNDcnPyc1bXN8cm9rYmQzJyknNDYnPydrZjNhYmF/YDdgJyknNDEnPyd/YGRjb25nPWJqJyknNDAnPydhc309MjZoYn1oJyknNDMnPyc1NDNqcnRpazF3JyknNDInPycydXBwMm50Y2NrJyknND0nPydydWRpf3I3MnJtJyknNDwnPyczZGJvM39ybXx3JyknNzUnPydrMnMyNmJ8anBjJyknNzQnPyc2c2p8PTUxcTYnKSc3Nyc/Jzd2b2oyNXU9dzwnKSc3Nic/JzB2Y2NsaWpsYGlnJyknNzEnPyd8fDZqMHE2dWJ3JyknNzAnPydsc3FuYWtiPDFmJyknNzMnPyduNGhmdn9pN3d8JyknNzInPyd2NXAxMHY2a2phJyknNz0nPydnbmppMDFrfTYnKSc3PCc/JzFxZGFwbWkxdScpJzY1Jz8ndWNpNjdsNWxqJyknNjQnPydxYGh2PDBhMHN9JyknNjcnPyd/dXQ0c3Z3bHVrJyknNjYnPydsZ3xucGx9aGZoJyknNjEnPyc8f3ZsYXFjbG0nKSc2MCc/J3JvMjJsMTxrfycpJzYzJz8nZGE8c3J1dXI1YCcpJzYyJz8naz1hbnxsZjEzJyknNj0nPydkbDRobnBrMzxvJyknNjwnPydidjV8PXVpaTZiJyknMTUnPyc0YWA3Y3xsNnJqJyknMTQnPyd9YnBwYWEzYGdtJyknMTcnPyd8a3c2NGtnNTFiJyknMTYnPyd9NmpvNzF2anYzJyknMTEnPydvYDRxZzFqYmh2JyknMTAnPyc1ZzJpZ21hanRmJyknMTMnPydtfz0xamBuPW5gZycpJ3EnPzQzMTU2MjM2NjcpJ3ZxJz80MzE1NjIzNzwwKSd2ZGlxJz8weA==",
        "key": None, # Translates to null
        "payload": {
            "S": None,
            "at": None,
            "i": 4,
            "l": username,
            "p": password,
            "s": 11,
            "t": 1640375761,
            "ty": 0,
            "salt": 7
        }
    }
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
               'cookie' : '__ddg1=OnnYfYJZz8gdfqoYHm26; ln=english; cookies=true; session=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkb21haW5QYXRoIjoibmV3eWVhciIsInJlZiI6MTMwMywiYm90RGF0YSI6IjE4OC4xMjAuMjQ5LjE1NToyMDAwMiIsInJhbmQiOiI3MTVhYTUxZmVlNjUzMzNkMjgxMzdmMDcxNWFlODg0MyIsImlhdCI6MTY0MDM3NTY0MywiYXV0aFR5cGUiOjAsInJlZGlyZWN0VHlwZSI6MCwicmVkaXJlY3RMaW5rIjoiIiwidmlldyI6dHJ1ZSwibG9naW4iOnRydWUsImxvYWRlZCI6dHJ1ZX0.tcUK1ihDT-1_LUya-v5fgbwuYeXT-Y673eMJ57gESb8',
               'origin' : f'https://{domain}',
               'referer' : f'https://{domain}/{ref_token}',
               'sec-fetch-dest' : 'empty',
               'sec-fetch-mode' : 'cors',
               'sec-fetch-site' : 'same-origin',
               'x-requested-with' : 'XMLHttpRequest'
    } #if needed
    
    try:
        r = requests.post(url, json=obj, headers=headers)
    except requests.ConnectionError as e:
        print(f"(#{sends}) {type(e).__name__}: {e}")
    else:
        sends += 1
        elapsed = time.time() - start
        print(f"POST {r.status_code} {r.reason} (#{sends}) [{math.floor(elapsed // 3600)}:{'0' if elapsed // 60 < 10 else ''}{math.floor(elapsed // 60)}:{'0' if elapsed % 60 < 10 else ''}{math.floor(elapsed % 60)}] {spinner[sends % 4]} | {username}:{password}", end='\r')
