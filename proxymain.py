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
    BOLD = Style.BRIGHT


user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:70.0) " "Gecko/20100101 Firefox/70.0",
]


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
        ▒▒░░    ▓▓  ▒▒      ░░▒▒      ▒▒     - version 2.0                
          ▒▒      ▒▒          ▒▒  ▒▒  ▒▒     - made by hax and dan    
        ▒▒  ▒▒  ▒▒  ▒▒  ▒▒  ▒▒▒▒▒▒▒▒▒▒       
        ▒▒▓▓▒▒▒▒    ▓▓▒▒▒▒▒▒        

"""

print(ascii_art)

valid_proxy_file = "./valid_proxy.txt"
URL = "https://www.us-proxy.org/"

if os.path.exists(valid_proxy_file):
    os.remove(valid_proxy_file)


def log(msg, level="INFO"):
    if level == "INFO":
        print(f"{Colors.CYAN}[INFO]{Colors.RESET} {msg}")
    elif level == "OK":
        print(f"{Colors.GREEN}[OK]{Colors.RESET}   {msg}")
    elif level == "FAIL":
        print(f"{Colors.RED}[FAIL]{Colors.RESET} {msg}")
    elif level == "DONE":
        print(f"{Colors.MAGENTA}[DONE]{Colors.RESET} {msg}")


def collect_proxies(url):
    log("Fetching proxy list...")
    headers = {"User-Agent": random.choice(user_agents)}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    table = soup.find("table", {"class": "table table-striped table-bordered"})
    proxies = []

    for row in table.find_all("tr")[1:]:
        cols = row.find_all("td")
        ip = cols[0].text.strip()
        port = cols[1].text.strip()
        if port in ["80", "8080", "3128"]:
            proxies.append(f"{ip}:{port}")

    log(f"Total proxies fetched: {len(proxies)}")
    return proxies


def test_proxy(proxy):
    url = "https://httpbin.org/ip"
    proxies = {"http": f"http://{proxy}", "https": f"http://{proxy}"}

    try:
        headers = {"User-Agent": random.choice(user_agents)}
        response = requests.get(url, proxies=proxies, headers=headers, timeout=5)
        if response.status_code == 200:
            log(f"Valid proxy → {proxy}", "OK")
            with open(valid_proxy_file, "a") as file:
                file.write(proxy + "\n")
            return True
        else:
            log(f"Invalid proxy → {proxy}", "FAIL")
            return False
    except requests.RequestException:
        log(f"Invalid proxy → {proxy}", "FAIL")
        return False


def main():
    proxies = collect_proxies(URL)

    log("Starting proxy tests...\n")
    valid_proxies = []
    invalid_count = 0

    for i, proxy in enumerate(proxies, 1):
        time.sleep(random.uniform(0.5, 1.2))  # natural delay
        if test_proxy(proxy):
            valid_proxies.append(proxy)
        else:
            invalid_count += 1
        print(
            f"{Colors.YELLOW}→ Tested {i}/{len(proxies)} | Valid: {len(valid_proxies)} | Invalid: {invalid_count}{Colors.RESET}"
        )

    log("\nFinal Report:", "DONE")
    log(f"Valid proxies found: {len(valid_proxies)}", "OK")
    log(f"Invalid proxies discarded: {invalid_count}", "FAIL")

    if valid_proxies:
        log("Valid proxy list saved to 'valid_proxy.txt'", "DONE")


if __name__ == "__main__":
    main()
