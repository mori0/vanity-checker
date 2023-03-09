import requests, os, colorama
from colorama import Fore , Back , Style
colorama.init (autoreset = True)

os.system('pip install requests')
os.system('pip install colorama')

print(f"""{Fore.TEAL}
                  _ _                _               _             
__   ____ _ _ __ (_) |_ _   _    ___| |__   ___  ___| | _____ _ __ 
\ \ / / _` | '_ \| | __| | | |  / __| '_ \ / _ \/ __| |/ / _ \ '__|
 \ V / (_| | | | | | |_| |_| | | (__| | | |  __/ (__|   <  __/ |   
  \_/ \__,_|_| |_|_|\__|\__, |  \___|_| |_|\___|\___|_|\_\___|_|   
                        |___/       
-------------------------------------------------------------------
"""


valid = 0
invalid = 0
with open('list.txt','r') as handle:
        list = handle.readlines()
        for van in list:
            vanity = van.rstrip()
            check = requests.get(f"https://discord.com/api/v9/invites/{vanity}")
            if check.status_code ==404:
             print(f"{Fore.GREEN} {vanity} Vaild")
             with open("vaild.txt","a+") as file:
              file.write(vanity)
              file.write("\n")
              Vaild =+ 1
              
            else:
             print(f"{Fore.RED} {vanity} invaild")
             with open("invaild.txt","a+") as file:
              file.write(vanity)
              file.write("\n")
              invaild =+ 1
        
        print(f"went through list.. {valid} - valid, {invalid} - invalid, total - {len(list)}")
