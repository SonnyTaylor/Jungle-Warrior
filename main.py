from colorama import Fore, Style
import game_functions

# Reset the inventory file
game_functions.reset_inventory_file()

correct_sensations = {
    "sky": "You feel a gentle breeze and a sense of weightlessness.",
    "earth": "The ground feels solid and reassuring beneath your feet.",
    "water": "Coolness and fluidity embrace your step, like a soothing embrace.",
    "fire": "A warm and invigorating energy courses through your body as you step onto the fiery tile."
}


incorrect_sound = "The ground beneath your foot feels unsettling."

game_over = False
text = """
▄▄▄█████▓▓█████  ███▄ ▄███▓ ██▓███   ██▓    ▓█████     █     █░ ▄▄▄       ██▀███   ██▀███   ██▓ ▒█████   ██▀███  
▓  ██▒ ▓▒▓█   ▀ ▓██▒▀█▀ ██▒▓██░  ██▒▓██▒    ▓█   ▀    ▓█░ █ ░█░▒████▄    ▓██ ▒ ██▒▓██ ▒ ██▒▓██▒▒██▒  ██▒▓██ ▒ ██▒
▒ ▓██░ ▒░▒███   ▓██    ▓██░▓██░ ██▓▒▒██░    ▒███      ▒█░ █ ░█ ▒██  ▀█▄  ▓██ ░▄█ ▒▓██ ░▄█ ▒▒██▒▒██░  ██▒▓██ ░▄█ ▒
░ ▓██▓ ░ ▒▓█  ▄ ▒██    ▒██ ▒██▄█▓▒ ▒▒██░    ▒▓█  ▄    ░█░ █ ░█ ░██▄▄▄▄██ ▒██▀▀█▄  ▒██▀▀█▄  ░██░▒██   ██░▒██▀▀█▄  
  ▒██▒ ░ ░▒████▒▒██▒   ░██▒▒██▒ ░  ░░██████▒░▒████▒   ░░██▒██▓  ▓█   ▓██▒░██▓ ▒██▒░██▓ ▒██▒░██░░ ████▓▒░░██▓ ▒██▒
  ▒ ░░   ░░ ▒░ ░░ ▒░   ░  ░▒▓▒░ ░  ░░ ▒░▓  ░░░ ▒░ ░   ░ ▓░▒ ▒   ▒▒   ▓▒█░░ ▒▓ ░▒▓░░ ▒▓ ░▒▓░░▓  ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░
    ░     ░ ░  ░░  ░      ░░▒ ░     ░ ░ ▒  ░ ░ ░  ░     ▒ ░ ░    ▒   ▒▒ ░  ░▒ ░ ▒░  ░▒ ░ ▒░ ▒ ░  ░ ▒ ▒░   ░▒ ░ ▒░
  ░         ░   ░      ░   ░░         ░ ░      ░        ░   ░    ░   ▒     ░░   ░   ░░   ░  ▒ ░░ ░ ░ ▒    ░░   ░ 
            ░  ░       ░                ░  ░   ░  ░       ░          ░  ░   ░        ░      ░      ░ ░     ░                                                                                                                
"""

# Split the text into lines
lines = text.split('\n')

# Print each line in green
for line in lines:
    if line.strip() != "":
        print(Fore.GREEN + line + Style.RESET_ALL)

# Check if the current module is being executed as the main program
if __name__ == "__main__":
    # Call the main function
    game_functions.main()
