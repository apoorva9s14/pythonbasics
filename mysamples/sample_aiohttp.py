import asyncio
import aiohttp
import sys
print(sys.version_info)

async def make_request(session, req_n):
    url = "https://google.com"
    print(f"making request {req_n} to {url}")
    async with session.get(url) as resp:
        if resp.status == 200:
            await resp.text()

async def main():
    n_requests = 100
    async with aiohttp.ClientSession() as session:
        await asyncio.gather(
            *[make_request(session, i) for i in range(n_requests)]
        )

loop = asyncio.get_event_loop()
loop.run_until_complete(main())