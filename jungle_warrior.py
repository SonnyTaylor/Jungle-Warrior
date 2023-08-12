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

correct_sensations = {
    "sky": "You feel a gentle breeze and a sense of weightlessness.",
    "earth": "The ground feels solid and reassuring beneath your feet.",
    "water": "Coolness and fluidity embrace your step, like a soothing embrace.",
    "fire": "A warm and invigorating energy courses through your body as you step onto the fiery tile."
}


incorrect_sound = "The ground beneath your foot feels unsettling."

game_over = False
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
            
            step1 = input("Where do you step on the first tile? ")
            if step1.lower() == "sky" or step1.lower() == "air":
                print_letter_by_letter(correct_sensations["sky"])
            else:
                print_letter_by_letter("The ground gives way beneath your feet, and you fall into a pit. Your journey ends here.")
                quit()
            
            step2 = input("Where do you step on the second tile? ")
            if step2.lower() == "earth" or step2.lower() == "hill":
                print_letter_by_letter(correct_sensations["earth"])
            else:
                print_letter_by_letter("Arrows shoot out from the walls as you step on the wrong tile. Your adventure comes to an abrupt end.")
                quit()
            
            step3 = input("Where do you step on the third tile? ")
            if step3.lower() == "water" or step3.lower() == "river":
                print_letter_by_letter(correct_sensations["water"])
            else:
                print_letter_by_letter("The ground shakes and crumbles beneath your feet. You fall into darkness, and your journey ends here.")
                quit()
            
            step4 = input("Where do you step on the fourth tile? ")
            if step4.lower() == "fire":
                print_letter_by_letter(correct_sensations["fire"])
            else:
                print_letter_by_letter("You feel a searing heat as you step on the wrong tile. Flames engulf you, and your quest ends here.")
                quit()

            print_letter_by_letter("Congratulations! You successfully step on each tile in the correct order. A hidden door opens, revealing a new path ahead.")
            print_letter_by_letter("As you move forward, you enter a dimly lit chamber. A gargantuan scorpion lurks in the shadows, its stinger poised for attack.")
            print_letter_by_letter("It's a fight for survival!")

            player_health = 100
            scorpion_health = 150

            while player_health > 0 and scorpion_health > 0:
                print("Your health:", player_health)
                print("Scorpion's health:", scorpion_health)
                print("What do you do?")
                print("1. Attack")
                print("2. Defend")
                
                choice = input("> ")
                
                if choice == "1":
                    player_attack = random.randint(15, 25)
                    scorpion_defense = random.randint(10, 20)
                    player_damage = max(player_attack - scorpion_defense, 0)
                    scorpion_health -= player_damage
                    print_letter_by_letter(f"You strike the scorpion for {player_damage} damage!")
                    
                    scorpion_attack = random.randint(10, 20)
                    player_defense = random.randint(5, 15)
                    scorpion_damage = max(scorpion_attack - player_defense, 0)
                    player_health -= scorpion_damage
                    print_letter_by_letter(f"The scorpion retaliates, dealing {scorpion_damage} damage to you.")
                
                elif choice == "2":
                    player_defense = random.randint(10, 20)
                    scorpion_attack = random.randint(5, 15)
                    player_damage = max(scorpion_attack - player_defense, 0)
                    player_health -= player_damage
                    print_letter_by_letter(f"You defend against the scorpion's attack, but still take {player_damage} damage.")
                    
                else:
                    print_letter_by_letter("You hesitate and the scorpion seizes the opportunity to strike, dealing a significant blow.")
                    player_health -= random.randint(20, 30)
                
                print("\n")
                
            if player_health <= 0:
                print_letter_by_letter("Your vision blurs as you collapse to the ground. The scorpion's stinger pierces your body, and darkness overtakes you.")
                print_letter_by_letter("Your journey ends here.")
            else:
                print_letter_by_letter("With a final blow, you defeat the gargantuan scorpion. Its lifeless body collapses to the ground.")
                print_letter_by_letter("Exhausted but victorious, you catch your breath and continue your quest.")


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
            
elif "leave" in another or "no" in another or "exit" in another:
    quit()

else:
    print_letter_by_letter("INVALID OPTION")