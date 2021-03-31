import requests
import colorama
import time
import os
os.system('cls')
os.system('title cutehook on top LOL')
colorama.init()

print(f"""{colorama.Fore.MAGENTA}
               __           __                      __         
              /\ \__       /\ \                    /\ \        
  ___   __  __\ \ ,_\    __\ \ \___     ___     ___\ \ \/'\    
 /'___\/\ \/\ \\\\ \ \/  /'__`\ \  _ `\  / __`\  / __`\ \ , <    
/\ \__/\ \ \_\ \\\\ \ \_/\  __/\ \ \ \ \/\ \L\ \/\ \L\ \ \ \\\\`\  
\ \____\\\\ \____/ \ \__\ \____\\\\ \_\ \_\ \____/\ \____/\ \_\ \_\\
 \/____/ \/___/   \/__/\/____/ \/_/\/_/\/___/  \/___/  \/_/\/_/
                                                      by cattyn
 """)

def hookValid(hook):
    info = requests.get(hook).text
    if "\"message\": \"Unknown Webhook\"" in info:
        return False
    else:
        return True

def main():
    i = 0
    try :
        webhook = input("Enter ur webhook > ")
        if not hookValid(webhook):
            print("invalid webhook")
            time.sleep(5)
            exit()
        name = input("Enter a webhook name > ")
        message = input("Enter a message > ")
        delay = input("Enter a delay [int] > ")
        try:
            x = int(delay)
        except ValueError:
            print(f"{colorama.Back.RED}{colorama.Fore.WHITE}\"{str(delay)}\" isnt int")
            time.sleep(5)
            exit()
        amount = input("Enter an amount [int/inf] > ")
        if amount != "inf":
            try:
                x = int(amount)
            except ValueError:
                print(f"{colorama.Back.RED}{colorama.Fore.WHITE}\"{str(delay)}\" isnt int")
                time.sleep(5)
                exit()
        hookDeleter = input("Delete webhook after spam? [Y/N] > ")
        if hookDeleter != "Y" and hookDeleter != "N":
            print(f"{colorama.Back.RED}{colorama.Fore.WHITE}\"{hookDeleter}\" isnt Y/N")
            time.sleep(5)
            exit()

        while True if amount == "inf" else i < int(amount):
            try:
                data = requests.post(webhook, json={"content": str(message), "name": str(name), "avatar_url": "https://i.imgur.com/lk79Hlc.jpeg"})
                if data.status_code == 204:
                    print(f"{colorama.Back.MAGENTA} {colorama.Fore.WHITE}[+] Sent{colorama.Back.RESET}")
                else:
                    print(f"{colorama.Back.RED} {colorama.Fore.WHITE}[-] Fail{colorama.Back.RESET}")
            except:
                print
            time.sleep(int(delay))
            i += 1

        if hookDeleter == "Y": 
            requests.delete(webhook)
            print(f'{colorama.Fore.MAGENTA}webhook deleted')
        print(f'{colorama.Fore.GREEN}done...')
        time.sleep(5)
        exit()
    except KeyboardInterrupt:
        print(f"{colorama.Fore.RED}\ngood bye!")
        exit()

if __name__ == "__main__":
    main()