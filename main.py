import requests
import os
import colorama
import time
from colorama import Fore, Back, Style

colorama.init(autoreset=True)

valid = 0
invalid = 0
words_left_out = 0
word_set = set()

with open('list.txt', 'r') as handle:
    lines = handle.readlines()
    total_words = len(lines)
    for van in lines:
        vanity = van.rstrip()
        if len(vanity) < 3:
            words_left_out += 1
            continue
        word_set.add(vanity)
    
    for vanity in word_set:
        check = requests.get(f"https://discord.com/api/v10/invites/{vanity}")
        if check.status_code == 404:
            print(f"{Fore.GREEN}{vanity} Valid")
            with open("valid.txt", "a+") as file:
                file.write(vanity)
                file.write("\n")
            valid += 1
        else:
            print(f"{Fore.RED}{vanity} Invalid")
            invalid += 1
        time.sleep(0.7)

print(f"{words_left_out} words were left out as they were less than 3 letters.")
print(f"Went through the list... {valid} valid, {invalid} invalid, total {total_words}")
