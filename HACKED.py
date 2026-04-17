import time
import sys
import random

# typing effect
def type_text(text, speed=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

# fake loading dots
def loading(text, duration=3):
    type_text(text)
    for _ in range(duration):
        for dot in "...":
            sys.stdout.write(dot)
            sys.stdout.flush()
            time.sleep(0.5)
        sys.stdout.write("\r" + " " * 50 + "\r")

# main program
target = input("Enter target system: ")

print("\nInitializing hack...\n")
time.sleep(1)

type_text(f"Connecting to {target} server...")
time.sleep(1)

loading("Bypassing firewall")
loading("Decrypting passwords")
loading("Accessing secure files")
