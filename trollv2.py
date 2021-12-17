"""
Version 2 of the scammer spammer, written almost completely from scratch.

This file sets up proxies and runs the callback.
Modify options.py to fit the scammer's website.
"""

import asyncio
import proxybroker

async def main():
    """
    The main function for all async tasks.
    """
    
    proxies = asyncio.Queue()
    broker = proxybroker.Broker(queue = proxies_queue,
                                timeout = 8,
                                max_conn = 200,
                                max_tries = 3)
    
    await broker.find(type = ['HTTP', 'HTTPS'], limit = 150)
    

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
