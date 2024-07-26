import colorama
import os
import requests
import time


def _exit():
    time.sleep(5)
    exit()


def check_hook(hook):
    info = requests.get(hook).text
    if "\"message\": \"Unknown Webhook\"" in info:
        return False
    return True


def main(webhook, name, delay, amount, message, hookDeleter):
    counter = 0
    while True if amount == "inf" else counter < int(amount):
        try:
            data = requests.post(webhook, json={"content": str(message), "name": str(name),
                                                "avatar_url": "https://i.imgur.com/lk79Hlc.jpeg"})
            if data.status_code == 204:
                print(f"{colorama.Back.MAGENTA} {colorama.Fore.WHITE}[+] Sent{colorama.Back.RESET}")
            else:
                print(f"{colorama.Back.RED} {colorama.Fore.WHITE}[-] Fail{colorama.Back.RESET}")
        except:
            print()
        time.sleep(float(delay))
        counter += 1
    if hookDeleter.lower() == "y":
        requests.delete(webhook)
        print(f'{colorama.Fore.MAGENTA}webhook deleted')
    print(f'{colorama.Fore.GREEN}done...')


def initialize():
    print(rf"""{colorama.Fore.MAGENTA}
                   __           __                      __         
                  /\ \__       /\ \                    /\ \        
      ___   __  __\ \ ,_\    __\ \ \___     ___     ___\ \ \/'\    
     /'___\/\ \/\ \\ \ \/  /'__`\ \  _ `\  / __`\  / __`\ \ , <    
    /\ \__/\ \ \_\ \\ \ \_/\  __/\ \ \ \ \/\ \L\ \/\ \L\ \ \ \\`\  
    \ \____\\ \____/ \ \__\ \____\\ \_\ \_\ \____/\ \____/\ \_\ \_\
     \/____/ \/___/   \/__/\/____/ \/_/\/_/\/___/  \/___/  \/_/\/_/
                                                          by cattyn
     """)
    webhook = input("Enter ur webhook > ")
    name = input("Enter a webhook name > ")
    message = input("Enter a message > ")
    delay = input("Enter a delay [int/float] > ")
    amount = input("Enter an amount [int/inf] > ")
    hookDeleter = input("Delete webhook after spam? [Y/N] > ")
    try:
        delay = float(delay)
    except ValueError:
        _exit()
    if not check_hook(webhook) or (not amount.isdigit() and amount != "inf") or (
            hookDeleter.lower() != "y" and hookDeleter.lower() != "n"):
        _exit()
    else:
        main(webhook, name, delay, amount, message, hookDeleter)
        _exit()


if __name__ == '__main__':
    os.system('cls' if os.name == "nt" else "clear")
    os.system('title cutehook on top LOL')
    colorama.init()
    initialize()
