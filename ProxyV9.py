import os
import sys
import requests
import time
from time import sleep
from urllib3.exceptions import InsecureRequestWarning
from urllib3 import disable_warnings

disable_warnings(InsecureRequestWarning)

def check_internet_connection():
    try:
        response = requests.get("https://www.google.com/", timeout=5)
        return True
    except requests.ConnectionError:
        return False

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def print_banner():
    print("""
        ██████╗ ███████╗████████╗    ██████╗ ██████╗  ██████╗ ██╗  ██╗██╗   ██╗
        ██╔══██╗██╔════╝╚══██╔══╝    ██╔══██╗██╔══██╗██╔═══██╗██║ ██╔╝██║   ██║
        ██████╔╝█████╗     ██║       ██████╔╝██████╔╝██║   ██║█████╔╝ ██║   ██║
        ██╔═══╝ ██╔══╝     ██║       ██╔═══╝ ██╔══██╗██║   ██║██╔═██╗ ██║   ██║
        ██║     ███████╗   ██║       ██║     ██║  ██║╚██████╔╝██║  ██╗╚██████╔╝
        ╚═╝     ╚══════╝   ╚═╝       ╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝ ╚═════╝

    ┌─────────────────── Welcome ───────────────────┐
    │
    │   Tool Name: Get Proxy V9
    │   Version: 9.0
    │   Updated Date: 03/22/2025
    │   Tool Admin: Ca Tool - [ Duong Ngoc & Quynh Anh ]
    │
    └───────────────────────────────────────────────┘
    """)

def main():
    clear()
    if not check_internet_connection():
        print("\n\033[1;36mNo Internet Connection!")
        sys.exit(1)

    print_banner()
    
    proxies = []
    proxy_links = [
        "https://api.proxyscrape.com/?request=displayproxies&proxytype=http",
        "https://daudau.org/api/http.txt",
        "https://api.openproxylist.xyz/http.txt",
        "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
        "http://worm.rip/http.txt",
        "https://proxy-spider.com/api/proxies.example.txt",
        "https://raw.githubusercontent.com/proxy4parsing/proxy-list/main/http.txt",
        "https://proxyspace.pro/http.txt",
        "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-https.txt",
        "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt",
        "https://raw.githubusercontent.com/MuRongPIG/Proxy-Master/main/http.txt",
        "https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/http/http.txt",
        "https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/https/https.txt",
        "https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt",
        "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
        "https://raw.githubusercontent.com/mmpx12/proxy-list/master/http.txt",
        "https://raw.githubusercontent.com/mmpx12/proxy-list/master/https.txt",
        "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt",
        "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/https.txt",
        "https://raw.githubusercontent.com/proxy4parsing/proxy-list/main/http.txt",
        "https://raw.githubusercontent.com/ErcinDedeoglu/proxies/main/proxies/http.txt",
        "https://raw.githubusercontent.com/ErcinDedeoglu/proxies/main/proxies/https.txt",
        "https://firet.io/firetx_retro/datacanthiet/proxies.txt",
        "https://raw.githubusercontent.com/proxy4parsing/proxy-list/main/http.txt",
        "https://raw.githubusercontent.com/almroot/proxylist/master/list.txt",
        "https://openproxylist.xyz/http.txt",
        "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies_anonymous/http.txt",
        "http://rootjazz.com/proxies/proxies.txt",
        "https://api.proxyscrape.com/?request=displayproxies&proxytype=https",
        "https://www.proxy-list.download/api/v1/get?type=http",
        "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt",
        "https://api.openproxylist.xyz/http.txt",
        "https://raw.githubusercontent.com/shiftytr/proxy-list/master/proxy.txt",
        "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt",
        "https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt",
        "https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies.txt",
        "https://raw.githubusercontent.com/opsxcq/proxy-list/master/list.txt",
        "https://proxy-spider.com/api/proxies.example.txt",
        "https://multiproxy.org/txt_all/proxy.txt",
        "https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt",
        "https://proxyspace.pro/https.txt",
        "https://raw.githubusercontent.com/almroot/proxylist/master/list.txt",
        "https://raw.githubusercontent.com/aslisk/proxyhttps/main/https.txt",
        "https://raw.githubusercontent.com/B4RC0DE-TM/proxy-list/main/HTTP.txt",
        "https://raw.githubusercontent.com/hendrikbgr/Free-Proxy-Repo/master/proxy_list.txt",
        "https://raw.githubusercontent.com/ALIILAPRO/Proxy/main/http.txt",
        "https://raw.githubusercontent.com/mmpx12/proxy-list/master/http.txt",
        "https://raw.githubusercontent.com/mmpx12/proxy-list/master/https.txt",
        "https://raw.githubusercontent.com/proxy4parsing/proxy-list/main/http.txt",
        "https://raw.githubusercontent.com/saisuiu/uiu/main/free.txt",
        "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/https.txt",
        "https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt",
        "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt",
        "https://www.proxy-list.download/api/v1/get?type=https",
        "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt",
        "https://raw.githubusercontent.com/saisuiu/Lionkings-Http-Proxys-Proxies/main/free.txt",
        "https://raw.githubusercontent.com/saisuiu/Lionkings-Http-Proxys-Proxies/main/cnfree.txt",
        "https://raw.githubusercontent.com/ErcinDedeoglu/proxies/main/proxies/http.txt",
        "https://raw.githubusercontent.com/ErcinDedeoglu/proxies/main/proxies/https.txt",
        "https://raw.githubusercontent.com/zevtyardt/proxy-list/main/http.txt",
        "https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt",
        "https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/http.txt",
        "https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies_anonymous/http.txt",
        "https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt",
        "https://sunny9577.github.io/proxy-scraper/proxies.txt"
    ]

    print("\033[1;36m       Get Proxy V9 - Update: Removed Timeout and Error-Prone APIs")
    print("\033[1;36m       Tool Coded By Duong Ngoc & Quynh Anh")
    print("\033[1;36m       Proxy Save File: Proxies.txt")

    for site in proxy_links:
        try:
            response = requests.get(site, verify=False, timeout=10)
            if response.status_code == 200:
                for line in response.text.split("\n"):
                    if ':' in line:
                        ip, port = line.split(':', maxsplit=2)[:2]
                        proxies.append(f'{ip}:{port}')
        except Exception:
            pass

    with open('Proxies.txt', 'w') as f:
        for proxy in proxies:
            f.write(proxy + '\n')

    clear()
    print_banner()
    print("\033[1;36mRedirecting to Check Proxy")
    sleep(3)
    os.system('clear && python Check.py')

if __name__ == "__main__":
    main()
