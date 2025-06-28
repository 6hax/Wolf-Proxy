import os
import requests
from bs4 import BeautifulSoup
import time
import random
from colorama import init, Fore, Style
init(autoreset=True)

class Colors:
    RED = Fore.RED
    GREEN = Fore.GREEN
    YELLOW = Fore.YELLOW
    BLUE = Fore.BLUE
    MAGENTA = Fore.MAGENTA
    CYAN = Fore.CYAN
    RESET = Style.RESET_ALL

user_agents = ["Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
               "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:70.0) Gecko/20100101 Firefox/70.0"]




ascii_art = f"""                                                                      

                                                 
              ▒▒              ▒▒                              
            ▒▒░░▒▒▒▒      ▒▒▒▒░░▒▒                            
          ▓▓░░  ░░░░▒▒▓▓▒▒░░░░  ░░▒▒                          
          ▓▓░░  ░░░░░░░░░░░░░░  ░░▒▒                          
          ▒▒░░    ░░░░░░░░░░    ░░▒▒                          
          ▒▒░░  ░░░░░░░░░░░░░░  ░░▒▒                          
            ▒▒░░░░  ░░░░░░  ░░░░▒▒                            
          ▒▒░░░░      ░░    ░░░░▒▒▒▒░░    ▒▒                  
          ▒▒░░    ██      ▓▓    ▒▒▓▓      ▒▒       _    _       _  __   _____                     
        ▒▒░░░░                  ░░░░▒▒    ▒▒  ▒▒  | |  | |     | |/ _| | ___ \                            
          ▒▒░░      ██████      ░░▒▒    ▒▒░░  ▒▒  | |  | | ___ | | |_  | |_/ / __ _____  ___   _          
            ▒▒░░      ██      ▒▒▓▓    ▒▒░░░░  ░░  | |/\| |/ _ \| |  _| |  __/ '__/ _ \ \/ / | | |          
          ▒▒░░▒▒░░          ░░▒▒░░▒▒▒▒░░░░░░▒▒    \  /\  / (_) | | |   | |  | | | (_) >  <| |_| |          
          ▒▒  ░░              ▓▓░░░░▒▒▒▒▒▒▒▒░░     \/  \/ \___/|_|_|   \_|  |_|  \___/_/\_\\__, |          
        ▒▒░░                ░░░░░░░░░░░░▒▒                                                  __/ |          
        ▒▒▒▒▒▒            ░░░░▒▒▒▒▒▒░░░░▒▒                                                 |___/        
        ▒▒░░░░▓▓      ▒▒  ░░░░▒▒░░░░░░░░▒▒                    
        ▒▒░░░░▒▒      ▒▒  ░░░░▒▒  ░░░░░░▒▒                    
        ▒▒░░    ▓▓  ▒▒      ░░▒▒      ▒▒     - version: 1.1                
          ▒▒      ▒▒          ▒▒  ▒▒  ▒▒     - github: https://github.com/emptyhax/proxy-hax                
        ▒▒  ▒▒  ▒▒  ▒▒  ▒▒  ▒▒▒▒▒▒▒▒▒▒       - made by hax and dan
        ▒▒▓▓▒▒▒▒    ▓▓▒▒▒▒▒▒        

"""

print(Colors.CYAN + ascii_art)

valid_proxy_file = "./valid_proxy.txt"
URL = "https://www.us-proxy.org/"

if os.path.exists(valid_proxy_file):
    os.remove(valid_proxy_file)


def collect_proxies(url):
    print(Colors.YELLOW + "[*] Fetching proxy list...")
    headers = {'User-Agent':
    random.choice(user_agents)}
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    table = soup.find('table', {'class': 'table table-striped table-bordered'})
    proxies = []

    for row in table.find_all('tr')[1:]:
        cols = row.find_all('td')
        ip = cols[0].text
        port = cols[1].text
        if port in ['80', '8080', '3128']:
            proxies.append(f"{ip}:{port}")

    return proxies

def test_proxy(proxy):
    url = "https://httpbin.org/ip"
    proxies = {"http": f"http://{proxy}", "https": f"http://{proxy}"}

    try:
        headers = {'User-Agent':
                   random.choice(user_agents)}
        response = requests.get(url,proxies=proxies, headers=headers, timeout=5)
        if response.status_code == 200:
            print(Colors.GREEN + f"[+] Valid proxy: {proxy}")
            with open(valid_proxy_file, 'a') as file:
                file.write(proxy + '\n')
            return True
        else:
            print(Colors.RED + f"[-] Invalid proxy: {proxy}")
            return False
    except requests.RequestException:
        print(Colors.RED + f"[-] Invalid proxy: {proxy}")
        return False

def main():
    proxies = collect_proxies(URL)

    print(Colors.CYAN + "\n[*] Testing proxies...")
    valid_proxies = []

    for proxy in proxies:
        time.sleep(random.uniform(1, 2))
        if test_proxy(proxy):
            valid_proxies.append(proxy)

    print(Colors.MAGENTA + "\n[*] Valid proxies found:")
    for proxy in valid_proxies:
        print(Colors.BLUE + f"  {proxy}")

if __name__ == "__main__":
    main()
