import time
import sys
import random
from colorama import Fore, Style, init

init()

# typing effect
def type_text(text, speed=0.03):
    for char in text:
        sys.stdout.write(Fore.GREEN + char)
        sys.stdout.flush()
        time.sleep(speed)
    print(Style.RESET_ALL)

# loading animation
def loading(text):
    type_text(text)
    for i in range(3):
        sys.stdout.write(Fore.GREEN + ".")
        sys.stdout.flush()
        time.sleep(0.5)
    print()

# random IP generator
def generate_ip():
    return ".".join(str(random.randint(0,255)) for _ in range(4))

# main
print(Fore.GREEN + "\n[ SYSTEM BOOTING... ]\n")

target = input(Fore.GREEN + "Enter target system: ")

time.sleep(1)
type_text(f"\nTarget locked: {target}")
type_text(f"IP Address: {generate_ip()}")

loading("Connecting to server")
loading("Bypassing firewall")
loading("Decrypting data")

if random.choice([True, False]):
    type_text("ACCESS GRANTED ✅", 0.05)
    loading("Downloading files")
    type_text("Download complete 💾")
else:
    type_text("ACCESS DENIED ❌", 0.05)
    type_text("TRACE DETECTED ⚠️")
    type_text("Disconnecting...")

print(Fore.RED + "\n[ SESSION TERMINATED ]")