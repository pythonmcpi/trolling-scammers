import requests
import random
import string
import os
from itertools import cycle
import time
import math

from options import sync_get_target, sync_get_protocol, sync_get_path, sync_get_headers, sync_get_payload

domain = sync_get_target()
path = sync_get_path()
proto = sync_get_protocol()
method = "POST" # Edit the requests.METHOD call too

sends = 0
spinner = '/-\\|' # eye candy lol
start = time.time()

url = f'{proto}://{domain}{path}'

while True:
    payload = sync_get_payload()
    headers = sync_get_headers(payload)
    
    try:
        r = requests.post(url, json=payload, headers=headers)
    except requests.ConnectionError as e:
        print(f"(#{sends}) {type(e).__name__}: {e}")
    else:
        sends += 1
        elapsed = time.time() - start
        print(f"POST {r.status_code} {r.reason} (#{sends}) [{math.floor(elapsed // 3600)}:{'0' if elapsed // 60 < 10 else ''}{math.floor(elapsed // 60)}:{'0' if elapsed % 60 < 10 else ''}{math.floor(elapsed % 60)}] {spinner[sends % 4]} | {payload['login']}:{payload['password']}", end='\r')
        print(r.text)
