import requests
from concurrent.futures import ThreadPoolExecutor
import os
import sys
import time
from time import sleep
import random

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def check_internet_connection():
    try:
        response = requests.get("https://www.google.com", timeout=5)
        return True
    except requests.ConnectionError:
        return False

def loading(seconds):
    print("\033[1;35mLoading", end="", flush=True)
    for _ in range(seconds):
        time.sleep(1)
        print(".", end="", flush=True)
    print("\n\033[1;35mDone!")
    sleep(2)

def print_banner():
    print("""
    ███████╗██╗  ██╗██╗███╗   ██╗██╗  ██╗██╗   ██╗██╗██╗   ██╗
    ██╔════╝██║  ██║██║████╗  ██║██║ ██╔╝██║   ██║██║██║   ██║
    █████╗  ███████║██║██╔██╗ ██║█████╔╝ ██║   ██║██║██║   ██║
    ██╔══╝  ██╔══██║██║██║╚██╗██║██╔═██╗ ██║   ██║██║██║   ██║
    ██║     ██║  ██║██║██║ ╚████║██║  ██╗╚██████╔╝██║╚██████╔╝
    ╚═╝     ╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝ ╚═════╝ ╚═╝ ╚═════╝

    ┌─────────────────── Welcome ───────────────────┐
    │
    │   Tool Name: Check Proxy V7
    │   Version: 7.0
    │   Updated Date: 12/24/2024
    │   Tool Admin: Alex
    │
    └───────────────────────────────────────────────┘
    """)

def check_proxy(proxy):
    proxies = {
        'http': f'http://{proxy}',
        'https': f'http://{proxy}'
    }
    
    try:
        response = requests.get('http://httpbin.org/ip', proxies=proxies, timeout=5)
        if response.status_code in [200, 202, 500, 502, 503, 504]:
            detect_location(proxy)
            return True
    except requests.exceptions.RequestException:
        pass

    print(f" \033[1;37m[\033[1;31m★\033[1;37m] \033[1;37m{proxy} \033[1;31m× \033[1;37mFailed \033[1;31m× \033[1;31mDead")
    return False

def detect_location(proxy):
    ip_address = proxy.split(':')[0]
    url = f"http://ip-api.com/json/{ip_address}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if data["status"] == "success":
            print(f" \033[1;37m[\033[1;31m★\033[1;37m] \033[1;37m{proxy} \033[1;31m√ \033[1;37m{data['country']}/{data['city']} \033[1;31m√ \033[1;32mLive")
            with open(save_file, 'a') as f:
                f.write(proxy + '\n')
        else:
            print(f" \033[1;37m[\033[1;31m+\033[1;37m] \033[1;31mFailed to detect location for proxy.")

def process_proxy(proxy):
    if check_proxy(proxy):
        pass

def main():
    clear()
    if not check_internet_connection():
        print("\n\033[1;31mNo internet connection!")
        sys.exit(1)
    
    loading(5)
    clear()
    print_banner()
    print("\033[1;32m++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    proxy_file = input("\033[1;32mEnter Proxy File: \033[1;33m")
    with open(proxy_file, 'r') as file:
        proxy_list = file.read().splitlines()
        proxy_count = len(proxy_list)
    global save_file
    save_file = input("\033[1;31mEnter File to Save Live Proxies: \033[1;36m")
    print(f" \033[1;31mTotal: \033[1;37m{proxy_count} \033[1;31mProxies in File")
    print("\033[1;34mPlease Wait\033[1;37m Tool\033[1;31m is Starting\033[1;37m to Check \033[1;31mProxies")
    print("\033[1;32m++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    sleep(3)

    num_workers = 200
    with ThreadPoolExecutor(max_workers=num_workers) as executor:
        executor.map(process_proxy, proxy_list)

    live_count = len(open(save_file).readlines()) if os.path.exists(save_file) else 0
    print(f" \033[1;31mProxy Checking Complete - Saved to \033[1;37m{save_file} \033[1;31mwith \033[1;37m{live_count} \033[1;31mLive Proxies")
    print("\033[1;31mThank you for using the tool")
    input(" Press Enter to exit")
    sys.exit()

if __name__ == "__main__":
    main()
