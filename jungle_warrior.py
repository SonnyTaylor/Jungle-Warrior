import random
from colorama import Fore, Style
import time
from PIL import Image
# Function to add an item to the inventory file


def add_item_to_inventory(item):
    """
    Adds an item to the inventory file.

    Args:
        item (str): The item to be added to the inventory.
    """
    with open("inventory.txt", "a") as file:
        file.write(item + "\n")


# Function to check if an item is in the inventory
def check_item_in_inventory(item):
    """
    Checks if a given item exists in the inventory.

    Args:
        item (str): The item to check.

    Returns:
        bool: True if the item is in the inventory, False otherwise.
    """
    try:
        with open("inventory.txt", "r") as file:
            inventory = file.read().splitlines()
            return item in inventory
    except FileNotFoundError:
        return False


# Function to remove an item from the inventory
def remove_item_from_inventory(item):
    """
    Removes an item from the inventory.

    Args:
        item (str): The item to be removed.

    Returns:
        bool: True if the item was successfully removed, False if the item was not found or an error occurred.
    """
    try:
        with open("inventory.txt", "r") as file:
            inventory = file.read().splitlines()
        if item in inventory:
            inventory.remove(item)
            with open("inventory.txt", "w") as file:
                for i in inventory:
                    file.write(i + "\n")
            return True
        else:
            return False
    except FileNotFoundError:
        return False


# Function to reset the inventory file
def reset_inventory_file():
    """
    Resets the inventory file by clearing its contents.
    """
    with open("inventory.txt", "w") as file:
        pass  # This will clear the contents of the file


# Function to display the user's inventory
def display_inventory():
    """
    Displays the items in the user's inventory.
    """
    try:
        with open("inventory.txt", "r") as file:
            inventory = file.read().splitlines()
            if inventory:
                print("Inventory:")
                for item in inventory:
                    print("- " + item)
            else:
                print("Your inventory is empty.")
    except FileNotFoundError:
        print("Your inventory is empty.")


def print_letter_by_letter(text, delay=0.01):
    """
    Print text letter by letter with a specified delay between each letter.

    Args:
        text (str): The text to be printed.
        delay (float, optional): The time delay (in seconds) between each letter. Default is 0.1 seconds.
    """
    for char in text:
        # Print the current character without moving to the next line
        print(char, end='', flush=True)

        # Introduce a delay before printing the next character
        time.sleep(delay)

    # Print a newline character at the end to move to the next line
    print()


# Reset the inventory file
reset_inventory_file()

text = """
 ▄▄▄██▀ ▀█    ██  ███▄    █   ▄████  ██▓    ▓█████     █     █░ ▄▄▄       ██▀███   ██▀███   ██▓ ▒█████   ██▀███  
   ▒██   ██  ▓██▒ ██ ▀█   █  ██▒ ▀█▒▓██▒    ▓█   ▀    ▓█░ █ ░█░▒████▄    ▓██ ▒ ██▒▓██ ▒ ██▒▓██▒▒██▒  ██▒▓██ ▒ ██▒
   ░██  ▓██  ▒██░▓██  ▀█ ██▒▒██░▄▄▄░▒██░    ▒███      ▒█░ █ ░█ ▒██  ▀█▄  ▓██ ░▄█ ▒▓██ ░▄█ ▒▒██▒▒██░  ██▒▓██ ░▄█ ▒
▓██▄██▓ ▓▓█  ░██░▓██▒  ▐▌██▒░▓█  ██▓▒██░    ▒▓█  ▄    ░█░ █ ░█ ░██▄▄▄▄██ ▒██▀▀█▄  ▒██▀▀█▄  ░██░▒██   ██░▒██▀▀█▄  
 ▓███▒  ▒▒█████▓ ▒██░   ▓██░░▒▓███▀▒░██████▒░▒████▒   ░░██▒██▓  ▓█   ▓██▒░██▓ ▒██▒░██▓ ▒██▒░██░░ ████▓▒░░██▓ ▒██▒
 ▒▓▒▒░  ░▒▓▒ ▒ ▒ ░ ▒░   ▒ ▒  ░▒   ▒ ░ ▒░▓  ░░░ ▒░ ░   ░ ▓░▒ ▒   ▒▒   ▓▒█░░ ▒▓ ░▒▓░░ ▒▓ ░▒▓░░▓  ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░
 ▒ ░▒░  ░░▒░ ░ ░ ░ ░░   ░ ▒░  ░   ░ ░ ░ ▒  ░ ░ ░  ░     ▒ ░ ░    ▒   ▒▒ ░  ░▒ ░ ▒░  ░▒ ░ ░░▒ ░░ ░ ░ ▒    ░░   ░ 
 ░ ░ ░   ░░░ ░ ░    ░   ░ ░ ░ ░   ░   ░ ░      ░        ░   ░    ░   ▒     ░░   ░   ░░   ░  ▒ ░░ ░ ░ ▒    ░░   ░ 
 ░   ░     ░              ░       ░     ░  ░   ░  ░       ░          ░  ░   ░        ░      ░      ░ ░     ░     
"""

# Split the text into lines
lines = text.split('\n')

# Print each line in green
for line in lines:
    if line.strip() != "":
        print(Fore.GREEN + line + Style.RESET_ALL)


# Get user's name
user_name = input("What is your name? ")

# Greet the user
print_letter_by_letter(f"Hello, {Fore.BLUE}{user_name}{Style.RESET_ALL}! Welcome to an ancient adventure.")
time.sleep(1)

# Set the stage
print_letter_by_letter("\nYou stand before the entrance of a mysterious temple.")
time.sleep(1)
print_letter_by_letter("The Door lies ahead")
another = input("What do you do? ").lower()

# Begin the journey
if "go" in another or "door" in another or "walk" in another or "open" in another:
    print_letter_by_letter("\nYou decide to go through the door, your heart pounding with anticipation...")
    time.sleep(0.5)
    print_letter_by_letter("\nAfter walking down the path for a while, you come across a small room with a table, a chest, and another door.")
    
    while True:  # Loop to allow the player to stay in the room
        choice = input("What do you do next? ").lower()
        
        if "chest" in choice:
            if check_item_in_inventory("Mysterious key"):
                print_letter_by_letter("You use the key to open the chest.")
                print_letter_by_letter("You find a large ominous gem.")
                add_item_to_inventory("Gem")
            else:
                print_letter_by_letter("You look at the chest and notice there is a lock on it.")

        elif "door" in choice:
            print_letter_by_letter("You go through the door and find yourself in a long corridor with a mosaic on the floor and a poem on the wall that reads:")
            print_letter_by_letter("Dawn breaks with stirring air,")
            print_letter_by_letter("As sun shines down on new day fair")
            print_letter_by_letter("\"Midday blaze bakes earth and grass,")
            print_letter_by_letter("The farmer waits for heat to pass")
            print_letter_by_letter("\"Evening cool brings water, wine,")
            print_letter_by_letter("Drink and laughter passing time")
            print_letter_by_letter("\"Night sees shining, roaring fire,")
            print_letter_by_letter("as wood and coals burn on the pyre\"")
            
            mosaic_image = Image.open("mosaic_image.png")  # Replace with the actual image file path
            mosaic_image.show()
            
            step1 = input("Step on the first tile: ")
            if step1.lower() != "air":
                print_letter_by_letter("You step on the wrong tile and suddenly the ground gives way. You fall into a pit and your journey ends here.")
                # End the game
            
            step2 = input("Step on the second tile: ")
            if step2.lower() != "earth":
                print_letter_by_letter("A trap is triggered as you step on the wrong tile. Arrows shoot out from the walls, and you fall to the ground, lifeless. Your adventure is over.")
                # End the game
            
            step3 = input("Step on the third tile: ")
            if step3.lower() != "water":
                print_letter_by_letter("As your foot touches the tile, the ground beneath you shakes and crumbles. You tumble into darkness, and your journey comes to an abrupt end.")
                # End the game

            step4 = input("Step on the fourth tile: ")
            if step4.lower() != "fire":
                print_letter_by_letter("You feel a searing heat as you step on the wrong tile. Flames engulf you, and you are consumed by the fire. Your quest ends here.")
                # End the game

            print_letter_by_letter("Congratulations! You successfully step on each tile in the correct order. A hidden door opens, revealing a new path ahead.")
            print_letter_by_letter("You continue your adventure...")
        
        elif "leave" in choice:
            print_letter_by_letter("You decide to leave the room.")
            break  # Exit the loop and continue with the story

        elif "inventory" in choice:
            display_inventory()
        
        elif "table" in choice:
            print_letter_by_letter("You walk up to the table and brush off the dust.")
            print_letter_by_letter("You notice a mysterious key.")
            take_key = input("Do you take the key? ").lower()
            
            if "yes" in take_key:
                add_item_to_inventory("Mysterious key")
                print_letter_by_letter("You take the key and put it in your inventory.")
            
            elif "no" in take_key:
                print_letter_by_letter("You leave the key on the table.")
        
        else:
            print_letter_by_letter("You decide not to interact with the chest.")
            
else:
    print_letter_by_letter("\nYou opt for the right path, a sense of curiosity guiding your steps...")
    time.sleep(1)