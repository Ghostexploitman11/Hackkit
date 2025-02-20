import os
from colorama import Fore, Style, init

init(autoreset=True)

def install_tool(choice):
    tools = { 
        "1" : "sudo apt-get install nmap -y",
        "2" : "git clone https://github.com/beefproject/beef",
        "3" : "git clone https://github.com/snort3/snort3",
        "4" : "git clone https://github.com/gentilkwi/mimikatz",
        "5" : "git clone https://github.com/sherlock-project/sherlock",
        "6" : "git clone https://github.com/larmaies/theHavester",
        "7" : "git clone https://github.com/htr-tech/zphisher",
        "8" : "git clone https://github.com/s0md3v/XSStrike",
        "9" : "git clone https://github.com/sundowndev/PhoneInfoga",
        "10" : "git clone https://github.com/kgretzky/evilginx2",
        "11" : "git clone https://github.com/lockfale/OSINT-Framwork",
        "12" : "git clone https://github.com/althonos/InstaLooter",
        "13" : "git clone https://github.com/quasar/Quasar",
        "14" : "git clone https://github.com/r00t-3xp10it/venom",
        "15" : "git clone https://github.com/UndeadSec/SocialFish",
        "16" : "git clone https://github.com/kucukemre96/PhishX",
        "17" : "git clone https://github.com/KasRoudra/PyPhisher",
        "18" : "git clone https://github.com/gophish/gophish",
        "19" : "git clone https://github.com/Screetsec/TheFatRat",
        "20" : "git clone https://github.com/smicallef/spiderfoot",
        "21" : "git clone https://github.com/Hackingzone/airgeddon.git",
    }
    
    command = tools.get(choice)
    
    if command:
        os.system(command)
        print(f"{choice} numaralı araç başarıyla kuruldu ")
    else:
        print("Geçersiz seçim")

if __name__ == "__main__":
   
    print(Fore.GREEN + """
██   ██  █████   ██████ ██   ██     ██   ██ ██ ████████ 
██   ██ ██   ██ ██      ██  ██      ██  ██  ██    ██    
███████ ███████ ██      █████       █████   ██    ██    
██   ██ ██   ██ ██      ██  ██      ██  ██  ██    ██    
██   ██ ██   ██  ██████ ██   ██     ██   ██ ██    ██    
    """)

    # Daha küçük bir fontla ASCII sanatı yazdırıyoruz
    print(Fore.GREEN + """
   ___ _           _                _     _ _                   
  / __| |_  ___ __| |_ _____ ___ __| |___(_) |_ _ __  __ _ _ _  
 | (_ | ' \/ _ (_-<  _/ -_) \ / '_ \ / _ \ |  _| '  \/ _` | ' \ 
  \___|_||_\___/__/\__\___/_\_\ .__/_\___/_|\__|_|_|_\__,_|_||_|
                              |_|                               
    """)

    
    print(Fore.GREEN + """
                                      ghostexploitman
    """)


    print(Fore.GREEN + Style.BRIGHT + "Kurmak istediğiniz aracı lütfen seçiniz: ")
    print(Fore.GREEN + Style.BRIGHT + "1 - Nmap")
    print(Fore.GREEN + Style.BRIGHT + "2 - Beef")
    print(Fore.GREEN + Style.BRIGHT + "3 - Snort3")
    print(Fore.GREEN + Style.BRIGHT + "4 - Mimikatz")
    print(Fore.GREEN + Style.BRIGHT + "5 - Sherlock")
    print(Fore.GREEN + Style.BRIGHT + "6 - TheHavester")
    print(Fore.GREEN + Style.BRIGHT + "7 - Zphisher")
    print(Fore.GREEN + Style.BRIGHT + "8 - XSStrike")
    print(Fore.GREEN + Style.BRIGHT + "9 - PhoneInfoga")
    print(Fore.GREEN + Style.BRIGHT + "10 - Evilginx2")
    print(Fore.GREEN + Style.BRIGHT + "11 - OSINT-Framwork")
    print(Fore.GREEN + Style.BRIGHT + "12 - InstaLooter")
    print(Fore.GREEN + Style.BRIGHT + "13 - Quasar")
    print(Fore.GREEN + Style.BRIGHT + "14 - Venom")
    print(Fore.GREEN + Style.BRIGHT + "15 - SocialFish")
    print(Fore.GREEN + Style.BRIGHT + "16 - PhishX")
    print(Fore.GREEN + Style.BRIGHT + "17 - PyPhisher")
    print(Fore.GREEN + Style.BRIGHT + "18 - Gophish")
    print(Fore.GREEN + Style.BRIGHT + "19 - TheFatRat")
    print(Fore.GREEN + Style.BRIGHT + "20 - Spiderfoot")
    print(Fore.GREEN + Style.BRIGHT + "21 - Airgeddon")
    
    
    choice = input(Fore.GREEN + "Seçiminizi yapın: ")
    install_tool(choice)
