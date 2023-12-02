# A game by Sonny, Lerot(y) and Cooper
import random
from colorama import Fore, Style
import time
from PIL import Image
import os
import threading

# Scorpion name in color
giant_scorpion = Fore.RED + "Giant Scorpion" + Style.RESET_ALL

# Descriptions for puzzle
correct_sensations = {
  "sky":
  "You feel a gentle breeze and a sense of weightlessness as you succesfully step right.",
  "earth":
  "The ground feels solid and reassuring beneath your feet.",
  "water":
  "Coolness and fluidity embrace your step, like a soothing embrace as you step on the correct tile.",
  "fire":
  "A warm and invigorating energy courses through your body as you step onto the right tile."
}

# Descriptions for puzzle if you die
incorrect_sound = "The ground beneath your foot feels unsettling."


def play_again():
  # Play again sequence
  play_again = input("Would you like to play again? (y/n) ")
  if play_again == "y":
    main()
  else:
    quit()


def add_item_to_inventory(item):
  """
    Adds an item to the inventory file.

    Args:
        item (str): The item to be added to the inventory.
    """
  with open("inventory.txt", "a") as file:
    file.write(item + "\n")


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


def reset_inventory_file():
  """
    Resets the inventory file by clearing its contents.
    """
  with open("inventory.txt", "w") as file:
    pass  # This will clear the contents of the file


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
    On Windows, it uses the 'cls' command. On Unix-like systems, it uses the 'clear' command, this makes it compatible on different OS's

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
        print("{0} takes fatal damage from {1}, with {2} overkill!".format(
          self.name.capitalize(), attacker, overkill))
      else:
        print("{0} takes fatal damage from {1}!".format(
          self.name.capitalize(), attacker))
    else:
      self.health -= damage_amount
      print("{0} takes {1} damage from {2}!".format(self.name.capitalize(),
                                                    damage_amount, attacker))

  def calculate_heal(self, heal_amount):
    # Calculates healing and stuff
    if (heal_amount + self.health > 100):
      self.health = 100
      print("{0} heals back to full health!".format(self.name.capitalize()))
    else:
      self.health += heal_amount
      print("{0} heals for {1}!".format(self.name.capitalize(), heal_amount))


def parse_int(input):
  """
    Attempt to parse the given input as an integer.

    Args:
        input (str or any): The input value to be checked for integer compatibility.

    Returns:
        bool: True if the input can be converted to an integer, False otherwise.

    This function attempts to convert the provided input into an integer using the built-in
    'int()' function. If successful, it returns True to indicate that the input can be
    interpreted as an integer. If the conversion raises a ValueError, indicating that the
    input cannot be an integer, it returns False.

    Example:
        >>> parse_int("42")
        True

        >>> parse_int("3.14")
        False

        >>> parse_int("abc")
        False
    """
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
    # Swap the current player each round
    if (current_player == computer):
      current_player = human
    else:
      current_player = computer

    print()
    print("You have {0} health remaining and the "
          "Giant Scorpion has {1} health remaining.".format(
            human.health, computer.health))
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
      print("The input was not valid. Please select a choice again.")

    if (human.health == 0):
      print("Sorry, you lose!")
      exit()

    if (computer.health == 0):
      print(f"Congratulations, you beat the {giant_scorpion}!")
      human.wins += 1
      game_in_progress = False


def scorpion_fight(username_color):
  """Starts scorpion fight sequence

    Args:
        username_color (variable): just here to bring over users name in its color version
    """

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
  """
    This function represents the action of leaving the temple in the 'Jungle Warrior' game.
    
    It prints a message to indicate that the player is leaving the temple and then
    waits for 2 seconds before quitting the game.
    """
  print_letter_by_letter("You leave the temple never to return.")
  time.sleep(2)
  quit()


def main():
  """
  The main function that initiates and controls the game's execution.

  This function serves as the entry point for the game and manages its overall flow.
  """
  print_letter_by_letter("Welcome to an ancient adventure.")
  user_name = input("What is your name? ")
  username_color = Fore.GREEN + user_name + Style.RESET_ALL  # Make username color
  if user_name == "Sonny" or user_name == "Cooper" or user_name == "Leroy" or user_name == "Lerot":
    print("Welcome back GOAT")
    while True:
      item_to_add = input(
        "What item do you want to add to your inventory? (Enter 'q' to go to level select): "
      )

      if item_to_add.lower() == 'q':
        break

      add_item_to_inventory(item_to_add)

    print("Welcome to the dev menu, pick a level to skip to")
    print("1. Continue from start")
    print("2. Room 1")
    print("3. Room 2")
    print("4. Room 3")
    print("5. Temple Chase")
    print("6. Gem Ending")
    dev_choice = input("What level do you want to skip to? ")
    if dev_choice == "1":
      pass
    elif dev_choice == "2":
      room1(username_color)
    elif dev_choice == "3":
      room2(username_color)
    elif dev_choice == "4":
      room3()
    elif dev_choice == "5":
      temple_chase_game()
    elif dev_choice == "6":
      gem_chase_ending()

  print_letter_by_letter(
    f"Hello, {username_color}! Welcome to an ancient adventure.")
  time.sleep(2)
  clear_terminal()

  print_letter_by_letter(
    "You stand before the entrance of a mysterious temple.")
  time.sleep(1)
  print_letter_by_letter("The Door lies ahead")
  # Temple ASCII art
  temple_art = """
   `,.      .   .        *   .    .      .  _    ..          .
     \,~-.         *           .    .       ))       *    .
          \ *          .   .   |    *  . .  ~    .      .  .  ,
 ,           `-.  .            :               *           ,-
  -             `-.        *._/_\_.       .       .   ,-'
  -                 `-_.,     |n|     .      .       ;
    -                    \ ._/_,_\_.  .          . ,'         ,
     -                    `-.|.n.|      .   ,-.__,'         -
      -                   ._/_,_,_\_.    ,-'              -
      -                     |..n..|-`'-'                -
       -                 ._/_,_,_,_\_.                 -
         -               ,-|...n...|                  -
           -         ,-'._/_,_,_,_,_\_.              -
             -  ,-=-'     |....n....|              -
              -;       ._/_,_,_,_,_,_\_.         -
             ,-          |.....n.....|          -
           ,;         ._/_,_,_,_,_,_,_\_.         -
  `,  '.  `.  ".  `,  '.| n   ,-.   n |  ",  `.  `,  '.  `,  ',
,.:;..;;..;;.,:;,.;:,o__|__o !.|.! o__|__o;,.:;.,;;,,:;,.:;,;;:
 ][  ][  ][  ][  ][  |_i_i_H_|_|_|_H_i_i_|  ][  ][  ][  ][  ][
                     |     //=====\\     |
                     |____//=======\\____|
.                        //=========\\
"""

  print(temple_art)

  print_letter_by_letter("Please select a number")
  print_letter_by_letter("1. Enter the temple")
  print_letter_by_letter("2. Leave")
  door_choice = input("What do you do? ")
  if door_choice == "1":
    room1(username_color)
  elif door_choice == "2":
    print_letter_by_letter("You leave the temple never to return.")
    time.sleep(2)
    quit()


def room1(username_color):
  print_letter_by_letter(
    "You decide to go through the door, your heart pounding with anticipation..."
  )
  time.sleep(0.5)
  print_letter_by_letter(
    "\nAfter walking down the path for a while, you come across a small room with a table, a chest, and another door."
  )
  time.sleep(2)
  while True:
    time.sleep(0.5)
    clear_terminal()
    time.sleep(1)
    print_letter_by_letter("What do you do next?")
    print_letter_by_letter("1. Search the table")
    print_letter_by_letter("2. Check the chest")
    print_letter_by_letter("3. Continue through the door")
    print_letter_by_letter("4. Check inventory")
    print_letter_by_letter("5. Leave")
    room1_choice = int(input())
    if room1_choice == 1:
      if check_item_in_inventory("Key"):
        print("You have already found the key.")
      else:
        print_letter_by_letter(
          "You walk up to the table and brush off the dust.")
        print_letter_by_letter("You notice a Key.")
        # Key ASCII art
        key_art = """
        8 8 8 8                     ,ooo.
        8a8 8a8                    oP   ?b
        d888a888zzzzzzzzzzzzzzzzzzzz8     8b
        `""^""'                    ?o___oP'
                  """
        print(key_art)
        take_key = input("Do you take the key (y/n)? ").lower()

        if take_key == "y":
          add_item_to_inventory("Key")
          print_letter_by_letter(
            "You take the key and put it in your inventory.")

        elif take_key == "n":
          print_letter_by_letter("You leave the key on the table.")

    if room1_choice == 2:
      # Chest ASCII art
      chest_art_string = r"""
                     ____...------------...____
               _.-"` /o/__ ____ __ __  __ \o\_`"-._
             .'     / /                    \ \     '.
             |=====/o/======================\o\=====|
             |____/_/________..____..________\_\____|
             /   _/ \_     <_o#\__/#o_>     _/ \_   \
                    \_________\####/_________/
              |===\!/========================\!/===|
              |   |=|          .---.         |=|   |
              |===|o|=========/     \========|o|===|
              |   | |         \() ()/        | |   |
              |===|o|======{'-.) A (.-'}=====|o|===|
              | __/ \__     '-.\uuu/.-'    __/ \__ |
              |==== .'.'^'.'.====|
              |  _\o/   __  {.' __  '.} _   _\o/  _|
              `""" "-" """""" """""" """""" """""" "-" """`
              """
      print(chest_art_string)

      if check_item_in_inventory("Key"):
        print_letter_by_letter("You use the key to open the chest.")
        print_letter_by_letter("You find a large ominous gem.")
        # Gem ASCII art
        gem_art = r"""
           _____ ____ _____
          /    /      \    \
        /____ /_________\____\
        \    \          /    /
          \  \        /  /
              \ \    / /
                \ \/ /
                  \/
                  """
        print(gem_art)
        take_gem = input("Do you take the gem (y/n)? ").lower()
        if take_gem == "y":
          add_item_to_inventory("Gem")
          print_letter_by_letter(
            "You take the gem and put it in your inventory.")
      else:
        print_letter_by_letter("It looks like it needs a key")
        print_letter_by_letter("it does look pretty fragile though")
        chest_break = input("Do you try break the chest? (y/n): ")
        if chest_break == "y":
          chest_chance = random.randint(0, 10)
          if chest_chance < 8:
            print_letter_by_letter(
              "You attempt to break the chest, but have no luck")
          else:
            print_letter_by_letter('you manage to break the chest')
            print_letter_by_letter("You find a large ominous gem.")
            take_gem_break = input("Do you take the gem (yes/no)? ").lower()
            if take_gem_break == "y":
              add_item_to_inventory("Gem")
              print_letter_by_letter(
                "You take the gem and put it in your inventory.")
        if chest_break == "n":
          print_letter_by_letter("You decide to leave it alone")

        else:
          print_letter_by_letter("Invalid Answer")

    if room1_choice == 5:
      print_letter_by_letter("You leave for some reason")
      quit()

    if room1_choice == 3:
      room2(username_color)
      return

    if room1_choice == 4:
      display_inventory()


def room2(username_color):
  # This is all jumbled around because replit formats it wierdly ¯\_(ツ)_/¯ dont know, dont care
  print_letter_by_letter(
    "You go through the door, it locks behind you and you find yourself in a long corridor with a mosaic on the floor and a poem on the wall that reads:"
  )
  print_letter_by_letter(Fore.RED + "Dawn breaks with stirring " + Fore.RESET +
                         "air,")
  print_letter_by_letter(Fore.RED + "As sun shines down on new day fair" +
                         Fore.RESET)
  print_letter_by_letter(Fore.RED + "Midday blaze bakes " + Fore.GREEN +
                         "earth" + Fore.RED + " and grass," + Fore.RESET)
  print_letter_by_letter(Fore.RED + "The farmer waits for heat to pass")
  print_letter_by_letter(Fore.RED + "Evening cool brings " + Fore.BLUE +
                         "water, " + Fore.RED + "wine")
  print_letter_by_letter(Fore.RED + "Drink and laughter passing time")
  print_letter_by_letter(Fore.RED + "Night sees shining, roaring " +
                         Fore.YELLOW + "fire," + Fore.RESET)
  print_letter_by_letter(Fore.RED + "as wood and coals burn on the pyre" +
                         Fore.RESET)

  mosaic_image = Image.open(
    "mosaic_image.png")  # Puzzle image to pop up using pillow library
  mosaic_image.show()

  print_letter_by_letter(
    "You notice an arrow lodged in the wall and a pool of blood below it")
  print_letter_by_letter("This is a trap")
  step1 = input("Where do you step on the first tile? ")
  if step1.lower() == "sky" or step1.lower() == "air" or step1.lower(
  ) == "blue" or step1.lower() == "clouds" or step1.lower() == "heavens":
    print_letter_by_letter(correct_sensations["sky"])
  else:
    print_letter_by_letter(
      "The ground gives way beneath your feet, and you fall into a pit. Your journey ends here."
    )
    quit()

  step2 = input("Where do you step on the second tile? ")
  if step2.lower() == "earth" or step2.lower() == "hill" or step2.lower(
  ) == "grass" or step2.lower() == "green" or step2.lower() == "nature":
    print_letter_by_letter(correct_sensations["earth"])
  else:
    print_letter_by_letter(
      "Arrows shoot out from the walls as you step on the wrong tile. Your adventure comes to an abrupt end."
    )
    quit()

  step3 = input("Where do you step on the third tile? ")
  if step3.lower() == "water" or step3.lower() == "river" or step3.lower(
  ) == "stream" or step3.lower() == "flow":
    print_letter_by_letter(correct_sensations["water"])
  else:
    print_letter_by_letter(
      "The ground shakes and crumbles beneath your feet. You fall into darkness, and your journey ends here."
    )
    quit()

  step4 = input("Where do you step on the fourth tile? ")
  if step4.lower() == "fire" or step4.lower() == "flame" or step4.lower(
  ) == "blaze" or step4.lower() == "heat" or step4.lower() == "ignite":
    print_letter_by_letter(correct_sensations["fire"])
  else:
    print_letter_by_letter(
      "You feel a searing heat as you step on the wrong tile. Flames engulf you, and your quest ends here."
    )
    print_letter_by_letter("YOU DIED")
    play_again()  # Asks if user wants to play again

  print_letter_by_letter(
    "Congratulations! You successfully step on each tile in the correct order. A hidden door opens, revealing a new path ahead."
  )

  pattern = [
    "   {_}                     _.-''''--.._",
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
  print_letter_by_letter(
    "As you move forward, you enter a dimly lit chamber. A gargantuan scorpion lurks in the shadows, its stinger poised for attack."
  )
  print_letter_by_letter("It's a fight for survival!")
  time.sleep(3)
  scorpion_fight(username_color)


def room3():
  time.sleep(1)
  print_letter_by_letter(
    "You breathe a sigh of relief after vanquishing the beast.")
  time.sleep(1)
  print_letter_by_letter(
    "You walk past its limp body and make your way to the next room where you find a large pedestal and a trapdoor on the roof."
  )

  if check_item_in_inventory("Gem"):
    time.sleep(1)
    print_letter_by_letter(
      "You notice a slot on the pedestal that seems to fit the gem you obtained earlier."
    )
    use_gem = input(
      "Do you want to place the gem on the pedestal? (y/n) ").lower()

    if "y" in use_gem:
      time.sleep(1)
      print_letter_by_letter(
        "As you place the gem on the pedestal, a hidden mechanism is triggered."
      )
      time.sleep(1)
      print_letter_by_letter(
        "The walls begin to rumble, and the ground beneath you shakes.")
      time.sleep(1)
      print_letter_by_letter(
        "A secret passage opens before you, revealing a new path forward.")
      time.sleep(1)
      print_letter_by_letter(
        "You step into the passage, ready to face whatever challenges await.")
      temple_chase_game()

    else:
      time.sleep(1)
      print_letter_by_letter(
        "You decide not to place the gem on the pedestal.")
      time.sleep(1)
      print_letter_by_letter(
        "Curiosity piqued, you climb up to the trapdoor on the roof, wondering what lies above."
      )
      time.sleep(1)
      print_letter_by_letter(
        "You open the trapdoor and find yourself outside the temple.")
      time.sleep(1)
      print_letter_by_letter("You leave the temple feeling unsatisfied")

  else:
    time.sleep(1)
    print_letter_by_letter(
      "Without the gem, you are left with only one option: the trapdoor on the roof."
    )
    time.sleep(1)
    print_letter_by_letter(
      "Curiosity piqued, you climb up to the trapdoor and open it.")
    time.sleep(1)
    print_letter_by_letter(
      "You open the trapdoor and find yourself outside the temple.")
    time.sleep(1)
    print_letter_by_letter("You leave the temple feeling unsatisfied")


def temple_chase_game():
  # Temple guardian ASCII art
  print("         ,     .")
  print("        /(     )\\               A")
  print("   .--.( `.___.' ).--.         /_\\\\")
  print("   `._ `%_&%#%$_ ' _.'     /| <___> |\\")
  print("      `|(@\\*%%/@)|'       / (  |L|  ) \\")
  print("       |  |%%#|  |       J d8bo|=|od8b L")
  print("        \\ $|#%/ /        | 8888|=|8888 |")
  print("        |\\|%%#|/|        J Y8P\"|=|\"Y8P F")
  print("        | (\\\".\\\")%|         \\ (  |L|  ) /")
  print("    ___.'  `-'  `.___      \\|  |L|  |/")
  print("  .'#*#`-       -'$#*`.       / )|")
  print(" /#%^#%*_ *%^%_  #  %$%\\    .J (__)")
  print(" #&  . %%%#% ###%*.   *%\\.-'&# (__)")
  print(" %*  J %.%#_|_#$.J* \\ %#'#%*^  (__)")
  print(" *#% J %$%%#|#% J\\%   *   .--|(_)")
  print(" |%  J\\ `%%#|#%%' / `.   _.'  |L|")
  print(" |#$%||` %%%$### '|   `-`      |L|")
  print(" (#%%||` #$#$%%% '|            |L|")
  print(" | ##||  $%%.%$%  |            |L|")
  print(" |$%^||   $%#$%   |            |L|")
  print(" |&^ ||  #%#$%#%  |            |L|")
  print(" |#$*|| #$%$$#%%$ |\\          |L|")
  print(" ||||||  %%(@)$#  |\\\\        |L|")
  print(" `|||||  #$$|%#%  | L|         |L|")
  print("      |  #$%|$%%  | ||l        |L|")
  print("      |  ##$H$%%  | |\\\\       |L|")
  print("      |  #%%H%##  | |\\\\|     |L|")
  print("      |  ##% $%#  | Y|||       |L|")
  print("      J $$#* *%#% L  |E/")
  print("      (__ $F J$ __)  F/")
  print("      J#%$ | |%%#%L")
  print("      |$$%#& & %%#|")
  print("      J##$ J % %%$F")
  print("       %$# * * %#&")
  print("       %#$ | |%#$%")
  print("       *#$%| | #$*")
  print("      /$#' ) ( `%%\\")
  print("     /#$# /   \\ %$%\\")
  print("    ooooO'     `Ooooo")

  print("A Temple Guardian is chasing you!")
  print("Type the word that appears. Press Enter after each word.")
  time.sleep(3)

  word_list = ["jump", "run", "slide"]
  success_count = 0

  # Change jump_runs for the amount of times the player should type the words
  jump_runs = (10)
  for _ in range(jump_runs):
    word = random.choice(word_list)
    color = Fore.GREEN if word == "jump" else (
      Fore.RED if word == "run" else Fore.YELLOW)
    print("\nType:", color + word + Style.RESET_ALL)  # Color the word

    user_input = ""
    timeout = 3  # Set the time limit (in seconds) for typing the word

    def input_thread():
      nonlocal user_input
      user_input = input()

    input_thread = threading.Thread(target=input_thread)  # type: ignore
    input_thread.start()
    input_thread.join(timeout)

    if input_thread.is_alive():
      print("\nTime's up! The Temple Guardian caught you.")
      print_letter_by_letter("YOU DIED")
      time.sleep(1)
      play_again()
      return False

    if user_input == word:
      if word == "jump":
        print("\nYou jumped over the gap!")
      elif word == "run":
        print("\nYou keep running from it.")
      elif word == "slide":
        print("\nYou slide under the fallen pillar")
        success_count += 1
    else:
      print("\nThe Temple Guardian caught you!")
      time.sleep(0.5)
      print("YOU DIED")
      play_again()
      return False

  if success_count >= 1:
    print_letter_by_letter(
      "\nCongratulations! You successfully escaped the Temple Guardian!")
    gem_chase_ending()
    return False


def gem_chase_ending():
  print_letter_by_letter(
    "After successfully escaping from the Temple Guardian, you make your way to the end of the cave."
  )
  time.sleep(1)  # Add a pause for dramatic effect
  print_letter_by_letter(
    "As you emerge from the cave, you're greeted by a breathtaking view of a hidden paradise."
  )
  time.sleep(1)
  print_letter_by_letter(
    "The sun's warm rays caress your skin, and a gentle breeze carries the scent of blooming flowers."
  )
  time.sleep(1)
  print_letter_by_letter(
    "In front of you lies the fabled Lost City of Gems, sparkling with untold riches and mysteries."
  )
  time.sleep(1)
  print_letter_by_letter(
    "Congratulations, brave adventurer! You've not only survived but discovered unimaginable treasures."
  )
  time.sleep(1)
  print_letter_by_letter(
    "You are hailed as a hero and a legend, and your name will be remembered for generations to come."
  )
  print_letter_by_letter("Thanks for playing!")
  time.sleep(1)
  play_again()  # Ask if user wants to play again
