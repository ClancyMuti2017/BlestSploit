import json
from colorama import Fore
import os
import jsbeautifier
exploits = 0
payloads = 0
posts = 0
version = 1.1
usbs = 0
# Banner = banner()
welcome = '''
+ -- ---={ '''+Fore.YELLOW+'''BlestSploit Framework V.'''+str(version)+''''''+Fore.RESET+'''
- -- ---={ Tüm Exploitler : '''+str(exploits)+'''
- -- ---={ Tüm Payloadlar : '''+str(payloads)+'''    
- -- ---={ Tüm USB Exploitler : '''+str(usbs)+''' 
- -- ---={ Tüm POSTlar : '''+str(posts)+'''
'''
print(welcome)

user = os.environ['USERNAME']
print(user)
num = 0
for i in range(11):
    num += 1
    if num < 10:
        print("OK")
    elif num > 10:
        print("10 >!!")

js = '''
{
    "1": {
        "ok": "ok",
        "options": {
            "1": "name"
        }
    }
}
'''
d = json.loads(js)
for i in d:
    for n in d[i]:
        print(n)
        for g in d[i]['options']:
            print(g)
            print(d[i]['options'][g])

s = ""
s =