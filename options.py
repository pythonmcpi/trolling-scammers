"""
Version 2 of the scammer spammer, written almost completely from scratch.

Modify this file to suit each specific website.
Functions in v2helper.py can be used for generating fake data.
"""

# This version is currently set to spam discord-app.net and steamnltros.ru

from v2helper import *
from typing import Union, List

async def get_targets() -> List[str]:
    return ["discord-app.net", "steamnltros.ru"]

async def get_headers(domain: str) -> dict:
    lumen_token = "IDpAuVfaeaTzGLpVbyhoog71da0w7WppYfe0MyfY"
    ref_token = "zq6I4NsG2TWrYCVlESDjbd4a5a8d2X14VeTz21EP2Y1Kc15dgCqQwiNsj"
    return {'authority' : domain, 'method' : 'POST', 'path' : '/login/dologin', 'scheme' : 'https', 'accept' : '*/*', 'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36', 'accept-encoding' : 'gzip, deflate, br', 'accept-language' : 'en-US,en;q=0.9', 'content-length' : '31', 'content-type' : 'application/x-www-form-urlencoded; charset=UTF-8', 'cookie' : f'lumen_session={lumen_token}; _TDG=6f527f8d338c0c8896253111fd986ed6; timezoneOffset=25200,0', 'origin' : f'https://{domain}', 'referer' : f'https://{domain}/{ref_token}', 'sec-fetch-dest' : 'empty', 'sec-fetch-mode' : 'cors', 'sec-fetch-site' : 'same-origin', 'x-requested-with' : 'XMLHttpRequest'}

async def get_post_url(domain: str) -> str:
    return "https://" + domain + "/login/dologin"
