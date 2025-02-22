import os
from colorama import Fore, Style, init

init(autoreset=True)

def install_tool(choice):
    tools = { 
        "1" : "git clone https://github.com/sqlmapproject/sqlmap.git",
        "2" : "git clone https://github.com/xmendez/wfuzz.git",
        "3" : "git clone https://github.com/sullo/nikto.git",
        "4" : "git clone https://github.com/s0md3v/XSStrike",
        "5" : "git clone https://github.com/sherlock-project/sherlock",
        "6" : "git clone https://github.com/laramies/theHarvester.git",
        "7" : "git clone https://github.com/lockfale/OSINT-Framework.git",
        "8" : "git clone https://github.com/sundowndev/PhoneInfoga",
        "9" : "git clone https://github.com/althonos/InstaLooter",
        "10" : "git clone https://github.com/kgretzky/evilginx2.git ",
        "11" : "git clone https://github.com/UndeadSec/SocialFish",
        "12" : "git clone https://github.com/kucukemre96/PhishX",
        "13" : "git clone https://github.com/KasRoudra/PyPhisher",
        "14" : "git clone https://github.com/gophish/gophish",
        "15" : "curl https://raw.githubusercontent.com/rapid7/metasploit-framework/master/msfupdate | sudo bash",
        "16" : "apt install exploitdb",
        "17" : "git clone https://github.com/beefproject/beef.git",
        "18" : "git clone https://github.com/kohoutik/pspy.git",
        "19" : "git clone https://github.com/Screetsec/TheFatRat",
        "20" : "git clone https://github.com/r00t-3xp10it/venom.git",
        "21" : "git clone https://github.com/Fadi002/unshackle.git",
        "22" : "git clone https://github.com/The404Hacking/AndroRAT.git",
        "23" : "git clone https://github.com/Luveedu/DoS-Max.git",
        "24" : "git clone https://github.com/AmitDas4321/DDos-Attack.git",
        "25" : "git clone https://github.com/palahsu/DDoS-Ripper.git",
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
    print(Fore.BLUE + Style.BRIGHT + "WEB Pentest")
    print(Fore.GREEN + Style.BRIGHT + "[1] - Sqlmap")
    print(Fore.GREEN + Style.BRIGHT + "[2] - wfuzz")
    print(Fore.GREEN + Style.BRIGHT + "[3] - Nikto")
    print(Fore.GREEN + Style.BRIGHT + "[4] - XSStrike")
  
    print(Fore.BLUE + Style.BRIGHT + "OSINT Tool") 
    print(Fore.GREEN + Style.BRIGHT + "[5] - Sherlock")
    print(Fore.GREEN + Style.BRIGHT + "[6] - TheHavester")
    print(Fore.GREEN + Style.BRIGHT + "[7] -  OSINT-Framwork")
    print(Fore.GREEN + Style.BRIGHT + "[8] - PhoneInfoga")
    print(Fore.GREEN + Style.BRIGHT + "[9] - InstaLooter")
   
    print(Fore.BLUE + Style.BRIGHT + "Phising Tool") 
    print(Fore.GREEN + Style.BRIGHT + "[10] - Evilginx2")
    print(Fore.GREEN + Style.BRIGHT + "[11] - SocialFish")
    print(Fore.GREEN + Style.BRIGHT + "[12] - PhishX")
    print(Fore.GREEN + Style.BRIGHT + "[13] - PyPhisher")
    print(Fore.GREEN + Style.BRIGHT + "[14] - Gophish")
  
    print(Fore.BLUE + Style.BRIGHT + "Metasploit-Framwork") 
    print(Fore.GREEN + Style.BRIGHT + "[15] - Metasploit Framework")
    print(Fore.GREEN + Style.BRIGHT + "[16] - Searchsploit")
    print(Fore.GREEN + Style.BRIGHT + "[17] - Beef")
    print(Fore.GREEN + Style.BRIGHT + "[18] - Pspy")
  
    print(Fore.BLUE + Style.BRIGHT + "Rat Tool") 
    print(Fore.GREEN + Style.BRIGHT + "[19] - TheFatRat")
    print(Fore.GREEN + Style.BRIGHT + "[20] - Venom")
    print(Fore.GREEN + Style.BRIGHT + "[21] - unshackle")
    print(Fore.GREEN + Style.BRIGHT + "[22] - AndroRAT")
  
    print(Fore.BLUE + Style.BRIGHT + "DDOS/DOS Tool") 
    print(Fore.GREEN + Style.BRIGHT + "[23] - DoS-Max")
    print(Fore.GREEN + Style.BRIGHT + "[24] - DDos-Attack")
    print(Fore.GREEN + Style.BRIGHT + "[25] - DDos-Ripper")
    choice = input(Fore.GREEN + "Seçiminizi yapın: ")
    install_tool(choice)
