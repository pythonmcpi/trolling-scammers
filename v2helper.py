"""
Version 2 of the scammer spammer, written almost completely from scratch.

This file contains helper functions, including fake name/password generators.
"""

from random import choice, randint
from itertools import cycle

__all__ = [
    'get_fake_password',
    'get_fake_token',
    'get_fake_first_name',
    'get_fake_last_name',
    'get_fake_name',
    'get_fake_username',
    'get_fake_email'
]

def get_fake_password(length: int = 16) -> str:
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()`~-=_+[]{}\\|/?,.<>'
    return ''.join(choice(letters) for i in range(length))

def get_fake_token(length: int = 57) -> str:
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    return ''.join(choice(letters) for i in range(length))

def get_fake_email(domain: str = None) -> str:
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_.'
    if domain is None:
        domain = choice(["gmail.com", "yahoo.com", "hotmail.com", "outlook.com", "mail.com"])
    return "".join(choice(letters) for i in range(randint(5, 30))) + '@' + domain

with open("1names.txt", "r") as f:
    first_names = [l.strip() for l in f.readlines()]

with open("lnames.txt", "r") as f:
    last_names = [l.strip() for l in f.readlines()]

def get_fake_first_name() -> str:
    return choice(first_names)

def get_fake_last_name() -> str:
    return choice(last_names)

def get_fake_name() -> str:
    return choice(first_names) + " " + choice(last_names)

def get_fake_username() -> str:
    v1 = randint(1, 4) # First name capitialization
    v2 = randint(1, 4) # Last name capitalization
    v3 = randint(1, 4) # Name separator
    v4 = randint(1, 4) # Trailing number
    v5 = randint(1, 4) # Name number separator
    v6 = randint(1, 7) # Pre/Suffix "x"
    v7 = randint(1, 8) # Pre/Suffix "_"
    
    fn, ln = get_fake_first_name(), get_fake_last_name()
    
    if v6 == 1:
        pf, sf = "Xx", "xX"
    elif v6 == 2:
        pf, sf = "xXx", "xXx"
    else:
        pf, sf = "", ""
    
    if v7 == 1:
        pf = "__" + pf
        sf += "__"
    elif v7 == 2:
        pf = "___" + pf
        sf += "___"
    elif v7 == 3:
        pf = "_" + pf
        sf += "_"
    
    un = pf
    
    if v1 == 1:
        un += fn.upper()
    elif v1 == 2:
        un += fn.lower()
    elif v1 == 3:
        un += fn
    # v1 == 4 means no first name
    
    if v3 == 1:
        un += "_"
    elif v3 == 2:
        un += "-"
    elif v3 == 3:
        un += "."
    # v3 == 4 means no separator
    
    if v2 == 1:
        un += ln.upper()
    elif v2 == 2:
        un += ln.lower()
    elif v2 == 3:
        un += fn
    # v2 == 4 means no last name
    
    if v5 == 1:
        un += "_"
    elif v5 == 2:
        un += "-"
    elif v5 == 3:
        un += "."
    # v5 == 4 means no separator
    
    if v4 == 1:
        un += str(randint(0, 9))
    elif v4 == 2:
        un += str(randint(0, 99))
    elif v4 == 3:
        un += str(randint(0, 999))
    # v4 == 4 means no number
    
    un += sf
    
    return un
