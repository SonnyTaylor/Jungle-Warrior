import random
from colorama import Fore, Style
import time
from PIL import Image
import os
import threading

giant_scorpion = Fore.RED + "Giant Scorpion" + Style.RESET_ALL


correct_sensations = {
    "sky": "You feel a gentle breeze and a sense of weightlessness.",
    "earth": "The ground feels solid and reassuring beneath your feet.",
    "water": "Coolness and fluidity embrace your step, like a soothing embrace.",
    "fire": "A warm and invigorating energy courses through your body as you step onto the fiery tile."
}


def main():
    print_letter_by_letter("Welcome to an ancient adventure.")
    user_name = input("What is your name? ")
    username_color = Fore.GREEN + user_name + Style.RESET_ALL
    clear_terminal()

    print_letter_by_letter(f"Hello, {username_color}! Welcome to an ancient adventure.")
    time.sleep(2)

    print_letter_by_letter("\nYou stand before the entrance of a mysterious temple.")
    time.sleep(1)
    print_letter_by_letter("The Door lies ahead")
    door_choice = validate_input("What do you do?\n1. Go through the door\n2. Leave\n", ["1", "2"])

    if door_choice == "1":
        room1(username_color)
    elif door_choice == "2":
        print_letter_by_letter("You leave the temple never to return.")
        time.sleep(2)
        quit()

incorrect_sound = "The ground beneath your foot feels unsettling."

def validate_input(prompt, valid_choices):
    while True:
        choice = input(prompt).strip()
        if choice in valid_choices:
            return choice
        print("Invalid input. Please try again.")

def clear_terminal():
    """
    Clears the terminal screen.

    This function uses the 'os' module to clear the terminal screen based on the operating system.
    On Windows, it uses the 'cls' command. On Unix-like systems, it uses the 'clear' command.

    Note:
        This function's behavior depends on the 'os' module and the operating system's terminal commands.

    Example usage:
        clear_terminal()  # Clears the terminal screen.
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    
class Player():
    def __init__(self, name):
        self.health = 100
        self.name = name
        self.wins = 0

    def calculate_damage(self, damage_amount, attacker):
        if (damage_amount > self.health):
            overkill = abs(self.health - damage_amount)
            self.health = 0
            if (overkill > 0):
                print("{0} takes fatal damage from {1}, with {2} overkill!"
                    .format(self.name.capitalize(), attacker, overkill))
            else:
                print("{0} takes fatal damage from {1}!"
                    .format(self.name.capitalize(), attacker))
        else:
            self.health -= damage_amount
            print("{0} takes {1} damage from {2}!"
                .format(self.name.capitalize(), damage_amount, attacker))

    def calculate_heal(self, heal_amount):
        if (heal_amount + self.health > 100):
            self.health = 100
            print("{0} heals back to full health!"
                .format(self.name.capitalize()))
        else:
            self.health += heal_amount
            print("{0} heals for {1}!"
                .format(self.name.capitalize(), heal_amount))


def parse_int(input):
    try:
        int(input)
        return True
    except ValueError:
        return False


def get_selection():
    valid_input = False
    while (valid_input is False):
        print()
        choice = input("Select an attack: ")
        if (parse_int(choice) is True):
            return int(choice)
        else:
            print("The input was invalid. Please try again.")


def get_computer_selection(health):
    sleep_time = random.randrange(2, 5)
    print("....thinking....")
    time.sleep(sleep_time)

    if (health <= 35):
        # Have the computer heal ~50% of its turns when <= 35
        result = random.randint(1, 6)
        if (result % 2 == 0):
            return 3
        else:
            return random.randint(1, 2)
    elif (health == 100):
        return random.randint(1, 2)
    else:
        return random.randint(1, 3)

def play_round(computer, human):
    game_in_progress = True
    current_player = computer

    while game_in_progress:
        # swap the current player each round
        if (current_player == computer):
            current_player = human
        else:
            current_player = computer

        print()
        print(
            "You have {0} health remaining and the "
            "Giant Scorpion has {1} health remaining."
            .format(human.health, computer.health))
        print()

        if (current_player == human):
            print("Available attacks:")
            print("1) Punch - Causes moderate damage.")
            print("2) Wild Swing - high or low damage, "
                "depending on your luck!")
            print("3) Herbal Drink - Restores a moderate amount of health.")
            move = get_selection()
        else:
            move = get_computer_selection(computer.health)

        if (move == 1):
            damage = random.randrange(18, 25)
            if (current_player == human):
                computer.calculate_damage(damage, human.name.capitalize())
            else:
                human.calculate_damage(damage, computer.name.capitalize())
        elif (move == 2):
            damage = random.randrange(10, 35)
            if (current_player == human):
                computer.calculate_damage(damage, human.name.capitalize())
            else:
                human.calculate_damage(damage, computer.name.capitalize())
        elif (move == 3):
            heal = random.randrange(18, 25)
            current_player.calculate_heal(heal)
        else:
            print ("The input was not valid. Please select a choice again.")

        if (human.health == 0):
            print("Sorry, you lose!")
            computer.wins += 1
            game_in_progress = False

        if (computer.health == 0):
            print(f"Congratulations, you beat the {giant_scorpion}!")
            human.wins += 1
            game_in_progress = False

def start_game(username_color):

    computer = Player(giant_scorpion)

    name = username_color
    human = Player(name)

    keep_playing = True

    while (keep_playing is True):

        computer.health = 100
        human.health = 100
        play_round(computer, human)
        print()
        if (computer.health == 0):
            room3()  # Call the function to continue the game
            keep_playing = False


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

def leave():
    print_letter_by_letter("You leave the temple never to return.")
    time.sleep(2)
    quit()

def room1(username_color):
    print_letter_by_letter("You decide to go through the door, your heart pounding with anticipation...")
    time.sleep(0.5)
    clear_terminal()
    print_letter_by_letter("\nAfter walking down the path for a while, you come across a small room with a table, a chest, and another door.")
    while True: 
        print_letter_by_letter("What do you do next?")
        print_letter_by_letter("1. Check the table")
        print_letter_by_letter("2. Check the chest")
        print_letter_by_letter("3. Go through the door")
        print_letter_by_letter("4. Leave")
        room1_choice = int(input())
        if room1_choice == 1:
            if check_item_in_inventory("Mysterious key"):
                print("You have already got the key.")
            else:
                print_letter_by_letter("You walk up to the table and brush off the dust.")
                print_letter_by_letter("You notice a mysterious key.")
                take_key = input("Do you take the key (yes/no)? ").lower()
            
                if "yes" in take_key:
                    add_item_to_inventory("Mysterious key")
                    print_letter_by_letter("You take the key and put it in your inventory.")
            
                elif "no" in take_key:
                    print_letter_by_letter("You leave the key on the table.")

        if room1_choice == 2:
            if check_item_in_inventory("Mysterious key"):
                print_letter_by_letter("You use the key to open the chest.")
                print_letter_by_letter("You find a large ominous gem.")
                take_gem = input("Do you take the gem (yes/no)? ").lower()
                if take_gem == "yes":
                    add_item_to_inventory("Gem")
                    print_letter_by_letter("You take the gem and put it in your inventory.")
        if room1_choice == 4:
            print_letter_by_letter("You leave for some reason")
            quit()

        if room1_choice == 3:
            room2(username_color)

def room2(username_color):
            print_letter_by_letter("You go through the door and find yourself in a long corridor with a mosaic on the floor and a poem on the wall that reads:")
            print_letter_by_letter(Fore.RED + "Dawn breaks with stirring " + Fore.RESET + "air,")
            print_letter_by_letter(Fore.RED + "As sun shines down on new day fair" + Fore.RESET)
            print_letter_by_letter(Fore.RED + "Midday blaze bakes " + Fore.GREEN + "earth" + Fore.RED + " and grass," + Fore.RESET)
            print_letter_by_letter(Fore.RED + "The farmer waits for heat to pass")
            print_letter_by_letter(Fore.RED + "Evening cool brings " + Fore.BLUE + "water, " + Fore.RED + "wine")
            print_letter_by_letter(Fore.RED + "Drink and laughter passing time")
            print_letter_by_letter(Fore.RED + "Night sees shining, roaring " + Fore.YELLOW + "fire," + Fore.RESET)
            print_letter_by_letter(Fore.RED + "as wood and coals burn on the pyre" + Fore.RESET)
            
            mosaic_image = Image.open("mosaic_image.png")  # Replace with the actual image file path
            mosaic_image.show()
            
            print_letter_by_letter("You notice an arrow lodged in the wall and a pool of blood below it")
            print_letter_by_letter("This is a trap")
            step1 = input("Where do you step on the first tile? ")
            if step1.lower() == "sky" or step1.lower() == "air" or step1.lower() == "blue" or step1.lower() == "clouds" or step1.lower() == "heavens":
                print_letter_by_letter(correct_sensations["sky"])
            else:
                print_letter_by_letter("The ground gives way beneath your feet, and you fall into a pit. Your journey ends here.")
                quit()
            
            step2 = input("Where do you step on the second tile? ")
            if step2.lower() == "earth" or step2.lower() == "hill" or step2.lower() == "grass" or step2.lower() == "green" or step2.lower() == "nature":
                print_letter_by_letter(correct_sensations["earth"])
            else:
                print_letter_by_letter("Arrows shoot out from the walls as you step on the wrong tile. Your adventure comes to an abrupt end.")
                quit()
            
            step3 = input("Where do you step on the third tile? ")
            if step3.lower() == "water" or step3.lower() == "river" or step3.lower() == "stream" or step3.lower() == "flow":
                print_letter_by_letter(correct_sensations["water"])
            else:
                print_letter_by_letter("The ground shakes and crumbles beneath your feet. You fall into darkness, and your journey ends here.")
                quit()
            
            step4 = input("Where do you step on the fourth tile? ")
            if step4.lower() == "fire" or step4.lower() == "flame" or step4.lower() == "blaze" or step4.lower() == "heat" or step4.lower() == "ignite":
                print_letter_by_letter(correct_sensations["fire"])
            else:
                print_letter_by_letter("You feel a searing heat as you step on the wrong tile. Flames engulf you, and your quest ends here.")
                quit()

            print_letter_by_letter("Congratulations! You successfully step on each tile in the correct order. A hidden door opens, revealing a new path ahead.")

            pattern = [
                "       ___ __",
                "     _{___{__}\\",
                "    {_}      `\\)",
                "   {_}        `            _.-''''--.._",
                "   {_}                    //'.--.  \\___`.",
                "    { }__,_.--~~~-~~~-~~-::.---. `-\\.  `.)",
                "     `-:.{_{_{_{_{_{_{_{_//  -- 8;=- `",
                "        `-:,_.:,_:,_:,.`\\\\._ ..'=- ,",
                "            // // // //`-.`\\`   .-'/",
                "           << << << <<    \\ `--'  /----)",
                "            ^  ^  ^  ^     `-.....--'''"
            ]
            
            color = Fore.YELLOW  # Brown color from Colorama
            for line in pattern:
                print(color + line)

            print(Style.RESET_ALL)  # Reset the color
            print_letter_by_letter("As you move forward, you enter a dimly lit chamber. A gargantuan scorpion lurks in the shadows, its stinger poised for attack.")
            print_letter_by_letter("It's a fight for survival!")
            time.sleep(3)
            clear_terminal()
            start_game(username_color)

def room3():
    time.sleep(1)
    clear_terminal()
    print_letter_by_letter("You breathe a sigh of relief after vanquishing the beast.")
    print_letter_by_letter("You walk past its limp body and make your way to the next room where you find a large pedestal and a trapdoor on the roof.")
    
    if check_item_in_inventory("Gem"):
        print_letter_by_letter("You notice a slot on the pedestal that seems to fit the gem you obtained earlier.")
        use_gem = input("Do you want to place the gem on the pedestal? ").lower()
        
        if "yes" in use_gem:
            print_letter_by_letter("As you place the gem on the pedestal, a hidden mechanism is triggered.")
            print_letter_by_letter("The walls begin to rumble, and the ground beneath you shakes.")
            print_letter_by_letter("A secret passage opens before you, revealing a new path forward.")
            print_letter_by_letter("You step into the passage, ready to face whatever challenges await.")
            temple_chase_game()
            # Add the gem ending here
            
        else:
            print_letter_by_letter("You decide not to place the gem on the pedestal.")
            print_letter_by_letter("Curiosity piqued, you climb up to the trapdoor on the roof, wondering what lies above.")
            print_letter_by_letter("You open the trapdoor and find yourself outside the temple.")
            print_letter_by_letter("You leave the temple feeling unsatisfied")
            # Add the trapdoor ending here
    
    else:
        print_letter_by_letter("Without the gem, you are left with only one option: the trapdoor on the roof.")
        print_letter_by_letter("Curiosity piqued, you climb up to the trapdoor and open it.")
        print_letter_by_letter("You open the trapdoor and find yourself outside the temple.")
        print_letter_by_letter("You leave the temple feeling unsatisfied")
        # Add the trapdoor ending here
        
def temple_chase_game():
    print("A Temple Guardian is chasing you!")
    print("Type 'jump' or 'run' to escape. Press Enter after each word.")

    word_list = ["jump", "run"]
    success_count = 0

    for _ in range(10):
        word = random.choice(word_list)
        print("\nType: ", word)

        user_input = ""
        timeout = 5  # Set the time limit (in seconds) for typing the word

        def input_thread():
            nonlocal user_input
            user_input = input()

        input_thread = threading.Thread(target=input_thread) # type: ignore
        input_thread.start()
        input_thread.join(timeout)

        if input_thread.is_alive():
            print("\nTime's up! The Temple Guardian caught you.")
            return False

        if user_input == word:
            if word == "jump":
                print("\nYou jumped over the gap!")
            elif word == "run":
                print("\nYou keep running from it.")
            success_count += 1
        else:
            print("\nIncorrect! The Temple Guardian caught you.")
            return False

    if success_count == 10:
        print("\nCongratulations! You successfully escaped the Temple Guardian!")
        return True

    print("Game over.")
    return False