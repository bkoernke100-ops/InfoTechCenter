# Welcome Branch

# Libraries Imported Here
import sys
import time

# ANSI color codes
RESET = "\033[0m"
GREEN = "\033[92m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RED = "\033[91m"
BOLD = "\033[1m"

print(f"\n{CYAN}{BOLD}Welcome Branch - Developer: Brennen Koernke{RESET}")
print(f"\n{GREEN}Welcome to Info Tech Center v.1.0{RESET}")

x = 0
ellipsis = 0

while x != 20:
    x += 1
    ellipsisMessage = f"{YELLOW}InfoTechCenter OS Booting{'.' * ellipsis}{RESET}"
    ellipsis += 1
    sys.stdout.write("\r\033[K" + ellipsisMessage)
    sys.stdout.flush()
    time.sleep(0.5)

    if ellipsis == 4:
        ellipsis = 0

    if x == 20:
        print(f"\n{GREEN}{BOLD}Operating System Booted Up - Retina Scanned - Access Granted{RESET}")
