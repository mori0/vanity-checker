import requests, os, colorama
from colorama import Fore , Back , Style
colorama.init (autoreset = True)

print(f"""{Fore.TEAL}
                  _ _                _               _             
__   ____ _ _ __ (_) |_ _   _    ___| |__   ___  ___| | _____ _ __ 
\ \ / / _` | '_ \| | __| | | |  / __| '_ \ / _ \/ __| |/ / _ \ '__|
 \ V / (_| | | | | | |_| |_| | | (__| | | |  __/ (__|   <  __/ |   
  \_/ \__,_|_| |_|_|\__|\__, |  \___|_| |_|\___|\___|_|\_\___|_|   
                        |___/       
-------------------------------------------------------------------
"""

with open('list.txt','r') as handle:
        list = handle.readlines()
        for van in list:
            vanity = van.rstrip()
            check = requests.get(f"https://discord.com/api/v9/invites/{vanity}")
            if check.status_code ==404:
             print(f"{Fore.GREEN} {listnames} Vaild")
             with open("vaild.txt","a+") as file:
              file.write(listnames)
              file.write("\n")
              Vaild =+ 1
              
            else:
             print(f"{Fore.RED} {listnames} invaild")
             with open("invaild.txt","a+") as file:
              file.write(listnames)
              file.write("\n")
              invaild =+ 1
        
        print("went through list.. {valid} - valid, {invalid} - invalid, total - {len(list)}")
