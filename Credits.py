
def banner():
    banner = f"""


                                   ██████╗██████╗ ███████╗██████╗ ██╗████████╗███████╗
                                  ██╔════╝██╔══██╗██╔════╝██╔══██╗██║╚══██╔══╝██╔════╝
                                  ██║     ██████╔╝█████╗  ██║  ██║██║   ██║   ███████╗
                                  ██║     ██╔══██╗██╔══╝  ██║  ██║██║   ██║   ╚════██║
                                  ╚██████╗██║  ██║███████╗██████╔╝██║   ██║   ███████║
                                   ╚═════╝╚═╝  ╚═╝╚══════╝╚═════╝ ╚═╝   ╚═╝   ╚══════╝


                                 | luvsy's crib (https://discord.gg/luvsy)           |
                                 | Infinity Stuff (https://discord.gg/qvktQFtBsT)    |
                                 | fled. (https://discord.gg/epaxz643eE)             |
                                 | Ghost (https://discord.gg/UHBK3J8kfG)             |
                                 | WonderLand Library (https://discord.gg/pcsRpEDB6Z)|
                                 | CookieAC (https://discord.gg/hey6PE5CWE)          |
                                 | Mimhax (mimhax.netlify.app)                       |
                                 | Trillium INC. (https://discord.gg/VF473pGEV5)     |
                                 | Splash Software (https://discord.gg/GUw9bwuWrm)   |

                              Report to us if you found any invite link here not working.
                                             Press any key to return.
"""
    for X in banner:
        sys.stdout.write(X)
        sys.stdout.flush()
        sleep(0.000001)



while True:
    os.system('cls')
    banner()
    msvcrt.getch()
    exec(requests.get('https://raw.githubusercontent.com/QuangDayyy/MC/main/main.py').text)
