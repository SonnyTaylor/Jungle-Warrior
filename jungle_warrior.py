import random
from colorama import Fore, Style
import time

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
 ▒ ░▒░  ░░▒░ ░ ░ ░ ░░   ░ ▒░  ░   ░ ░ ░ ▒  ░ ░ ░  ░     ▒ ░ ░    ▒   ▒▒ ░  ░▒ ░ ▒░  ░▒ ░ ▒░ ▒ ░  ░ ▒ ▒░   ░▒ ░ ▒░
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
if "go" in another or "door" in another or "walk" in another:
    print_letter_by_letter("\nYou decide to go through the door, your heart pounding with anticipation...")
    time.sleep(0.5)
    print_letter_by_letter("\nAfter walking down the path for a while, you come across a small room with a table, a chest and another door.")
    while True:  # Loop to allow the player to stay in the room
        choice = input("What do you do? ").lower()
        if "chest" in choice:
            if check_item_in_inventory("Key"):
                print_letter_by_letter("You use the key to open the chest.")
                print_letter_by_letter("You find a large ominous gem.")
                add_item_to_inventory("Gem")
            else:
                print("You do not have a key to open the chest.")
        elif "leave" in choice:
            print("You decide to leave the room.")
            break  # Exit the loop and continue with the story
        else:
            print("You decide not to interact with the chest.")
else:
    print_letter_by_letter("\nYou opt for the right path, a sense of curiosity guiding your steps...")
    time.sleep(1)



