# A game by Sonny, Leroy and Cooper
# best played on PC
from colorama import Fore, Style
import game_functions

# Reset the inventory file
game_functions.reset_inventory_file()

# Correct sequences for puzzle section
# I dont even think these are needed here lol
correct_sensations = {
  "sky":
  "You feel a gentle breeze and a sense of weightlessness.",
  "earth":
  "The ground feels solid and reassuring beneath your feet.",
  "water":
  "Coolness and fluidity embrace your step, like a soothing embrace.",
  "fire":
  "A warm and invigorating energy courses through your body as you step onto the fiery tile."
}

# Incorrect sequences for puzzle section
incorrect_sound = "The ground beneath your foot feels unsettling."

# Title screen
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