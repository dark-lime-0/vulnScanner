import requests

logo='''
        __        __   _    ____  _ _                       
        \ \      / /__| |__/ ___|(_) |_ ___
         \ \ /\ / / _ \ '_ \___ \| | __/ _ \ 
          \ V  V /  __/ |_) |__) | | ||  __/
__     __  \_/\_/ \___|_.__/____/|_|\__\___| _ _ _
\ \   / /   _| |_ __   ___ _ __ __ _| |__ (_) (_) |_ _   _ 
 \ \ / / | | | | '_ \ / _ \ '__/ _` | '_ \| | | | __| | | |
  \ V /| |_| | | | | |  __/ | | (_| | |_) | | | | |_| |_| |
   \_/  \__,_|_|_| |_|\___|_|  \__,_|_.__/|_|_|_|\__|\__, |
         ____                                        |___/  
        / ___|  ___ __ _ _ __  _ __   ___ _ __
        \___ \ / __/ _` | '_ \| '_ \ / _ \ '__|
         ___) | (_| (_| | | | | | | |  __/ |
        |____/ \___\__,_|_| |_|_| |_|\___|_|
        
v0.0.1 by Youssef | dark-lime-0 
'''
print(logo)

domain=input("Enter Your Website Link : ")
headers=['Strict-Transport-Security','Content-Security-Policy','X-Frame-Options','X-Content-Type-Options','Referrer-Policy','Permissions-Policy']

try :
        wb_headers=requests.get(domain).headers

except requests.RequestException as e:
    print(f"Error: {e}")
    exit()
print("\n")

b=0
for a in headers:
    if a not in wb_headers:
        print(a + " :: doesn't exist")
        b+=1

if(b !=0):print("\nYour Website May Vulnerable to *Clickjacking* Vulnerability !! ")
else: print("All headers present.")
