"""
Version 2 of the scammer spammer, written almost completely from scratch.

Modify this file to suit each specific website.
Functions in v2helper.py can be used for generating fake data.
"""

# This version is currently set to spam discord-app.net and steamnltros.ru

from v2helper import *
from typing import Union, List
from json import dumps

def sync_get_target() -> str:
    return "disorde.gift"

def sync_get_protocol() -> str:
    return "http"

def sync_get_path() -> str:
    return "/discord/login"

def sync_get_page_path() -> str:
    return "/AVBrDhAbECvcW"

def sync_get_headers(payload: dict) -> dict:
    domain = sync_get_target()
    protocol = sync_get_protocol()
    return {
        'authority' : domain,
        'method' : 'POST',
        'path' : sync_get_path(),
        'scheme' : protocol,
        'accept' : 'application/json, text/plain, */*',
        'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
        'accept-encoding' : 'gzip, deflate, br',
        'accept-language' : 'en-US,en;q=0.9',
        'content-length' : str(len(dumps(payload))),
        'content-type' : 'application/x-www-form-urlencoded; charset=UTF-8',
        'cookie' : '',
        'origin' : f'{protocol}://{domain}',
        'referer' : f'https://{domain}{sync_get_page_path()}',
        'sec-fetch-dest' : 'empty',
        'sec-fetch-mode' : 'cors',
        'sec-fetch-site' : 'same-origin',
        'cookie': 'lumen_session=cbH3k842iIzO8sCLAL6vbD6H6Y7fcjh01MScXvt5'
    }

def sync_get_payload() -> dict:
    return {
        'login': get_fake_email(),
        'password': get_fake_password()
    }

async def get_target(): return sync_get_target()
async def get_protocol(): return sync_get_protocol()
async def get_path(): return sync_get_path()
async def get_page_path(): return sync_get_page_path()
async def get_headers(payload: dict): return sync_get_headers(payload)
async def get_payload(): return sync_get_payload()
