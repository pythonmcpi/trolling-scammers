"""
Version 2 of the scammer spammer, written almost completely from scratch.

Proxy list in proxies.txt
Get list by visiting free-proxy-list.net and running the following js snippet:
Array.prototype.slice.call(document.querySelectorAll('table')[0].rows, 1).map(row => `${row.cells[0].innerText}:${row.cells[1].innerText}`).join(",")

Modify options.py to fit the scammer's website.
"""

import asyncio
import aiohttp
from options import get_target, get_protocol, get_path, get_headers, get_payload

with open('proxies.txt', 'r') as f:
    proxy_list = f.read().strip('\n').split(',')

async def add_proxies(proxies, proxy_list):
    print('[+] Adding proxies')
    for proxy in proxy_list:
        await proxies.put(proxy)
    print(f'[+] {len(proxy_list)} proxies added')

async def spam(id, url, proxies):
    """
    Send requests through a proxy.
    """
    print(f'[+] [{id}] Starting')
    async with aiohttp.ClientSession() as session:
        while True:
            try:
                proxy = await asyncio.wait_for(proxies.get(), timeout = 5)
            except asyncio.TimeoutError:
                print(f'[+] [{id}] Fetch proxy timed out')
                break
            if proxy is None:
                print(f'[+] [{id}] Out of proxies')
                break
            print(f'[+] [{id}] Using proxy: {proxy}')
            try:
                async with session.post(url, data = await get_payload(), proxy = 'http://' + proxy, ssl = False) as resp:
                    print(f'[+] [{id}] {resp.status}')
            except Exception as e:
                print(f'{type(e).__name__}: {e}')
            proxies.task_done()
    print(f'[+] [{id}] Done')

async def main():
    """
    The main function for all async tasks.
    """
    
    print('[+] Starting ProxyBroker and fake info spammer')
    
    proxies = asyncio.Queue()
    url = f'{await get_protocol()}://{await get_target()}{await get_path()}'
    
    
    spammers = []
    for i in range(10):
        spammers.append(spam(i, url, proxies)) # Not awaited
    
    await asyncio.gather(
        add_proxies(proxies, proxy_list),
        *spammers
    )
    
    print('[+] Finished')

# https://stackoverflow.com/a/67056687
policy = asyncio.WindowsSelectorEventLoopPolicy()
asyncio.set_event_loop_policy(policy)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
