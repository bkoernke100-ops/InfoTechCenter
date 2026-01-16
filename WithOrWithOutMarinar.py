#BetaTestDev

# -------------------------------------------------
# Welcome Branch
# Simulates a boot-up sequence with colored text
# Developer: Brennen Koernke
# -------------------------------------------------

# Libraries Imported Here
import sys      # Used for writing to the terminal without new lines
import time     # Used to create delays (sleep)

# -------------------------------------------------
# ANSI color codes for terminal text styling
# These allow colored and bold text output
# -------------------------------------------------
RESET = "\033[0m"     # Resets text color/style back to default
GREEN = "\033[92m"   # Green text (success messages)
CYAN = "\033[96m"    # Cyan text (titles)
YELLOW = "\033[93m"  # Yellow text (loading animation)
RED = "\033[91m"     # Red text (errors or warnings)
BOLD = "\033[1m"     # Bold text style

# -------------------------------------------------
# Display welcome and version information
# -------------------------------------------------
print(f"\n{CYAN}{BOLD}Welcome Branch - Developer: Brennen Koernke{RESET}")
print(f"\n{GREEN}Welcome to Info Tech Center v.1.0{RESET}")

# -------------------------------------------------
# Initialize loop counters
# x controls how long the boot animation runs
# ellipsis controls how many dots appear (.)
# -------------------------------------------------
x = 0
ellipsis = 0

# -------------------------------------------------
# Boot-up animation loop
# Runs until x reaches 20 iterations
# -------------------------------------------------
while x != 20:
    x += 1  # Increment loop counter

    # Build the boot message with animated dots
    ellipsisMessage = f"{YELLOW}InfoTechCenter OS Booting{'.' * ellipsis}{RESET}"
    ellipsis += 1

    # Write the message on the same line (carriage return)
    # \r moves cursor to start of line
    # \033[K clears the line
    sys.stdout.write("\r\033[K" + ellipsisMessage)
    sys.stdout.flush()  # Forces the output to display immediately

    # Pause to control animation speed
    time.sleep(0.5)

    # Reset dot count after reaching 3 dots
    if ellipsis == 4:
        ellipsis = 0

    # -------------------------------------------------
    # Final message once boot sequence is complete
    # -------------------------------------------------
    if x == 20:
        print(f"\n{GREEN}{BOLD}Operating System Booted Up - Retina Scanned - Access Granted{RESET}")
