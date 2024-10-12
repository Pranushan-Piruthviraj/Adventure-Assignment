# Pranushan Piruthviraj
# 2024-10-11
# The Temple's Awakening

# import random module to generate random events
import random


# Global inventory dictionary to keep track of player's items
inventory = {
    "rubies": 0,
    "sapphires": 0,
    "emeralds": 0,
    "gold coins": 0,
    "ancient scrolls": 0,
    "magical artifacts": 0
}

# Global variables for player and Tony's powers
player_name = input("Please enter your name: ")
player_power = None
tony_power = None
Tony = False  # Flag to check if Tony is present

# Function to display the current inventory
def display_inventory():
    print("\nYour Inventory:")
    for item, count in inventory.items():
        if count > 0:
            print(f"{item.capitalize()}: {count}")
    print()

# Function to add items to the inventory
def add_to_inventory(item, amount):
    inventory[item] += amount
    print(f"You added {amount} {item} to your inventory!")

# Function to handle item encounters and potential traps
def item_encounter(item, amount):
    print(f"\nYou see {amount} {item} nearby.")
    choice = input(f"Do you want to grab the {item}? (yes/no): ").lower()
    if choice == 'yes':
        if random.random() < 0.7:  # 70% chance of success
            add_to_inventory(item, amount)
        else:
            print(f"Oh no! As you reach for the {item}, you trigger a trap!")
            trap_consequence()
    else:
        print(f"You decide to leave the {item} alone.")

# Function to handle consequences of triggering a trap
def trap_consequence():
    consequences = [
        "You fall through a trapdoor!",
        "Poisonous gas fills the room!",
        "The walls start closing in!",
        "A boulder starts rolling towards you!",
        "The floor becomes lava!"
    ]
    print(random.choice(consequences))

    total_lost = 0
    for item in inventory:
        if inventory[item] > 0:
            # Determine the maximum amount that can be lost
            max_loss = inventory[item] if not Tony else inventory[item] // 2
            lost_amount = random.randint(0, max_loss)
            
            inventory[item] -= lost_amount
            total_lost += lost_amount
            
            if lost_amount > 0:
                print(f"You lost {lost_amount} {item}.")

def display_temple():
    print(r"""
         `,.      .   .        *   .    .      .  _    ..          .
     ,~-.         *           .    .       ))       *    .
           *          .   .   |    *  . .  ~    .      .  .  ,
 ,           `-.  .            :               *           ,-
  -             `-.        *._/_.       .       .   ,-'
  -                 `-_.,     |n|     .      .       ;
    -                     ._/_,_.  .          . ,'         ,
     -                    `-.|.n.|      .   ,-.__,'         -
      -                   ._/_,_,_.    ,-'              -
      -                     |..n..|-`'-'                -
       -                 ._/_,_,_,_.                 -
         -               ,-|...n...|                  -
           -         ,-'._/_,_,_,_,_.              -
             -  ,-=-'     |....n....|              -
              -;       ._/_,_,_,_,_,_.         -
             ,-          |.....n.....|          -
           ,;         ._/_,_,_,_,_,_,_.         -
  `,  '.  `.  ".  `,  '.| n   ,-.   n |  ",  `.  `,  '.  `,  ',
,.:;..;;..;;.,:;,.;:,o__|__o !.|.! o__|__o;,.:;.,;;,,:;,.:;,;;:
 
    """)


def display_boat():
    print(r"""
               |___..--"/
   __..--``        /
  ______________/ 
    """)

def display_book():
    print(r"""
         __...--~~~~~-._   _.-~~~~~--...__
    //               `V'                
   //                 |                  
  //__...--~~~~~~-._  |  _.-~~~~~~--...__ 
 //__.....----~~~~._ | /_.~~~~----.....__
====================|//====================
    """)

def display_mirror():
    print(r"""
         //-----------
     //       | |   | 
   //  _   /    /  | 
  ||            |  / __||
  ||               | |_/  ||
  ||     __  |   |/ __  ||
  ||  __/   |   |_/  ||
  ||  _    ___|  /     ||
  ||_/ __/   |/_     /||
  ||          o        _||
  ||       / |    ___/ ||
  ||  ___/   |        /||
  ||     |   /     )-<_||
  ||    /  /       /    ||
    /   |      _><    //
   //   |     /    //
  ||   -----------//   ||
  ||                     ||
 /||                   /||
/____                 /____

    """)
def display_holographic_map():
    print("""
              *     *
         *       *       *
      *   *  *       *    *
   *        *  *  *      *
      *    *   |   *     *
           *    |    *
                |    
                |  
         +------+------+
         |             |
         |   SECRET    |
         |   CHAMBER   |
         |             |
         +------+------+
                |
                |
          *     *
      *       *
          *  *
""")
def display_map():
    print("""
         .
'~~~-,
     '-,_ 
      `~'~''         
  _           ~ 
  _                 
     .               
                   `~~
       ' .             /
        L             |
                   |             _.----,
               |                      !     /
              '._                 __/    _/
                            ''--''    __/
                   .__                |
                       ''.__  __.._   __
                            ''     './  `

""")
    
def display_earth_aurasphere():
    green_text = "\033[32m"  # ANSI escape code for green text
    reset_color = "\033[0m"  # ANSI escape code to reset color
    print(green_text + """
      ⠀⠀⠀⠀⠀⣀⣠⣤⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣰⣿⣿⣿⣿⣿⡿⠿⠿⠿⢿⣿⣿⣄⠀⠀⠀⠀⠀⠀⠀⠈⢄⠀⠀⠀⠀
⠀⠀⢰⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠈⠙⢿⣦⠀⠀⠀⠀⠀⠀⠈⣧⠀⠀⠀⠀
⠀⠀⣾⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠆⠀⠀⠀⠀⠀⠀⠸⣧⠀⠀⠀
⠀⠀⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⢀⣤⣴⣶⣶⣤⣀⠀⠀⠀⠀⠀⠀⠀⣿⡆⠀⠀
⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⢻⣿⡀⠀
⠀⠀⣿⣿⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⣼⣿⡇⠀
⠀⠀⠸⣿⡀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀⢀⣿⣿⡇⠀
⠀⠀⠀⢻⡇⠀⠀⠀⠀⠀⠀⢀⠈⠙⠛⠿⠛⠛⠁⠀⠀⠀⠀⠀⠀⣼⣿⣿⡇⠀
⠀⠀⠀⠈⢿⡀⠀⠀⠀⠀⠀⠀⢳⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⣿⣿⠃⠀
⠀⠀⠀⠀⠈⢧⠀⠀⠀⠀⠀⠀⠀⢻⣷⣦⣀⠀⠀⠀⠀⣀⣴⣿⣿⣿⣿⠏⠀⠀
⠀⠀⠀⠀⠀⠀⠣⠀⠀⠀⠀⠀⠀⠀⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠿⣿⣿⣿⣿⠿⠛⠁⠀⠀⠀⠀⠀
    """ + reset_color)
    print(green_text + "A green aurasphere floats above the pillar, pulsing with earthly energy." + reset_color)

def display_fire_aurasphere():
    red_text = "\033[38;5;208m"  # ANSI escape code for red text
    reset_color = "\033[0m"  # ANSI escape code to reset color
    print(red_text + """
      ⠀⠀⠀⠀⠀⣀⣠⣤⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣰⣿⣿⣿⣿⣿⡿⠿⠿⠿⢿⣿⣿⣄⠀⠀⠀⠀⠀⠀⠀⠈⢄⠀⠀⠀⠀
⠀⠀⢰⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠈⠙⢿⣦⠀⠀⠀⠀⠀⠀⠈⣧⠀⠀⠀⠀
⠀⠀⣾⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠆⠀⠀⠀⠀⠀⠀⠸⣧⠀⠀⠀
⠀⠀⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⢀⣤⣴⣶⣶⣤⣀⠀⠀⠀⠀⠀⠀⠀⣿⡆⠀⠀
⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⢻⣿⡀⠀
⠀⠀⣿⣿⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⣼⣿⡇⠀
⠀⠀⠸⣿⡀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀⢀⣿⣿⡇⠀
⠀⠀⠀⢻⡇⠀⠀⠀⠀⠀⠀⢀⠈⠙⠛⠿⠛⠛⠁⠀⠀⠀⠀⠀⠀⣼⣿⣿⡇⠀
⠀⠀⠀⠈⢿⡀⠀⠀⠀⠀⠀⠀⢳⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⣿⣿⠃⠀
⠀⠀⠀⠀⠈⢧⠀⠀⠀⠀⠀⠀⠀⢻⣷⣦⣀⠀⠀⠀⠀⣀⣴⣿⣿⣿⣿⠏⠀⠀
⠀⠀⠀⠀⠀⠀⠣⠀⠀⠀⠀⠀⠀⠀⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠿⣿⣿⣿⣿⠿⠛⠁⠀⠀⠀⠀⠀
    """ + reset_color)
    print(red_text + "An orange aurasphere floats above the pillar, flickering with fiery power." + reset_color)

def display_water_aurasphere():
    blue_text = "\033[34m"  # ANSI escape code for blue text
    reset_color = "\033[0m"  # ANSI escape code to reset color
    print(blue_text + """
      ⠀⠀⠀⠀⠀⣀⣠⣤⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣰⣿⣿⣿⣿⣿⡿⠿⠿⠿⢿⣿⣿⣄⠀⠀⠀⠀⠀⠀⠀⠈⢄⠀⠀⠀⠀
⠀⠀⢰⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠈⠙⢿⣦⠀⠀⠀⠀⠀⠀⠈⣧⠀⠀⠀⠀
⠀⠀⣾⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠆⠀⠀⠀⠀⠀⠀⠸⣧⠀⠀⠀
⠀⠀⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⢀⣤⣴⣶⣶⣤⣀⠀⠀⠀⠀⠀⠀⠀⣿⡆⠀⠀
⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⢻⣿⡀⠀
⠀⠀⣿⣿⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⣼⣿⡇⠀
⠀⠀⠸⣿⡀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀⢀⣿⣿⡇⠀
⠀⠀⠀⢻⡇⠀⠀⠀⠀⠀⠀⢀⠈⠙⠛⠿⠛⠛⠁⠀⠀⠀⠀⠀⠀⣼⣿⣿⡇⠀
⠀⠀⠀⠈⢿⡀⠀⠀⠀⠀⠀⠀⢳⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⣿⣿⠃⠀
⠀⠀⠀⠀⠈⢧⠀⠀⠀⠀⠀⠀⠀⢻⣷⣦⣀⠀⠀⠀⠀⣀⣴⣿⣿⣿⣿⠏⠀⠀
⠀⠀⠀⠀⠀⠀⠣⠀⠀⠀⠀⠀⠀⠀⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠿⣿⣿⣿⣿⠿⠛⠁⠀⠀⠀⠀⠀
    """ + reset_color)
    print(blue_text + "A blue aurasphere floats above the pillar, swirling with oceanic might." + reset_color)


# Function to handle the secret ruin aura encounter
def secret_ruin_aura():
    global player_power
    
    print("\nAs you explore, you stumble upon a hidden chamber. The air shimmers with an ancient energy.")
    print("Suddenly, the ground trembles, and three pillars rise from the earth.")
    
    
    # Display the three auraspheres
    display_earth_aurasphere()
    display_fire_aurasphere()
    display_water_aurasphere()
    
    # Ask if the player wants to read the signs
    read_signs = input("Do you want to read the signs next to each pillar? (yes/no): ").lower()
    
    if read_signs == 'yes':
        # Display descriptions and warnings for each pillar
        print("\nGreen Pillar: The power of Earth. Command the very ground beneath your feet.")
        print("Beware: This power is said to be near impossible to control unless the wielder possesses")
        print("patience, stability, and a deep connection to nature.")
        
        print("\nRed Pillar: The power of Fire. Harness the destructive and purifying flames.")
        print("Beware: This power is said to be near impossible to control unless the wielder possesses")
        print("passion, determination, and an indomitable spirit.")
        
        print("\nBlue Pillar: The power of Water. Control the life-giving and shape-shifting liquid.")
        print("Beware: This power is said to be near impossible to control unless the wielder possesses")
        print("adaptability, empathy, and a calm, reflective nature.")
    
    # Player chooses a power or disregards them
    choice = input("\nDo you want to (1) approach the green pillar, (2) approach the red pillar, (3) approach the blue pillar, or (4) disregard the pillars? ")
    
    if choice in ['1', '2', '3']:
        # Assign power based on player's choice
        if choice == '1':
            player_power = "Earth"
            display_earth_aurasphere()
        elif choice == '2':
            player_power = "Fire"
            display_fire_aurasphere()
        else:
            player_power = "Water"
            display_water_aurasphere()
        
        print(f"\nYou approach the pillar and touch the {player_power} aurasphere. Its power flows into you!")
        
    else:
        print("\nYou decide to leave the pillars alone, respecting the ancient magic and its warnings.")

    # The pillars sink back into ground 
    print("\nThe pillars slowly sink back into the ground, leaving no trace of their existence.")
    print("You feel forever changed by this encounter, whether you chose a power or not.")
    post_aura_encounter()



    



def start_game():
    display_temple()  # Function to display ASCII art of the temple
    print("The Temple's Awakening: Pranushan Piruthviraj")
    print("Before playing this game, please extend your terminal.")
    print("\nYou stand before an ancient temple, its stone facade weathered by time.")
    print("Two entrances beckon: a grand archway and a small, hidden door.")
    # Player chooses their entry point
    choice = input("Do you enter through the (1) grand archway, (2) hidden door, or (3) look for another way? ")
    if choice == "1":
        grand_hall()
    elif choice == "2":
        secret_passage()
    elif choice == "3":
        jungle_path()
    else:
        teleportation_accident()  # Handles invalid input

def grand_hall():
    print("\nYou enter a vast hall adorned with golden statues.")
    print("To your left is a spiraling staircase. To your right, a corridor lined with mirrors.")
    item_encounter("gold coins", 5)  # Player encounters gold coins
    # Player chooses their next move
    choice = input("Do you take the (1) spiraling staircase, (2) mirror corridor, or (3) examine a statue? ")
    if choice == "1":
        upper_chamber()
    elif choice == "2":
        hall_of_mirrors()
    elif choice == "3":
        statue_room()
    else:
        teleportation_accident()  # Handles invalid input

def secret_passage():
    print("\nYou squeeze through the hidden door into a narrow, dark passage.")
    print("The path splits: one way leads down, the other continues straight.")
    item_encounter("rubies", 2)  # Player encounters rubies
    # Player chooses their path
    choice = input("Do you go (1) down, (2) straight, or (3) turn back? ")
    if choice == "1":
        underground_cavern()
    elif choice == "2":
        hidden_library()
    elif choice == "3":
        start_game()  # Player returns to the start
    else:
        teleportation_accident()  # Handles invalid input

def upper_chamber():
    print("\nYou reach an upper chamber with a view of the surrounding jungle.")
    print("There's a rope bridge leading to a tower and a slide going back down.")
    item_encounter("sapphires", 3)  # Player encounters sapphires
    
    # Player chooses what to do in the upper chamber
    choice = input("Do you cross the (1) rope bridge, take the (2) slide, or (3) enjoy the view? ")
    
    if choice == "1":
        print("\nYou carefully cross the rope bridge and reach the tower.")
        print("Inside, you find ancient artifacts and a beautiful view of the jungle.")
        explore_after_upper_chamber()
    elif choice == "2":
        print("\nYou take the slide down and land safely on a pile of leaves.")
        print("You find yourself in a new area filled with strange plants and sounds.")
        explore_after_upper_chamber()
    elif choice == "3":
        print("\nYou take a moment to enjoy the view, feeling at peace with nature.")
        print("While enjoying the view, you spot something moving in the trees...")
        explore_after_upper_chamber()
    else:
        print("\nYou hesitate and decide to explore your surroundings further.")
        explore_after_upper_chamber()
     
def explore_after_upper_chamber():
    # This function simulates further exploration leading to Tony's encounter
    print("\nAs you explore further, you hear a cry for help!")
    help_npc()  # Call to help NPC function which introduces Tony

def hall_of_mirrors():
    display_mirror()  # Function to display ASCII art of mirrors
    print("\nYou're surrounded by mirrors, each showing a different reflection.")
    print("One mirror shows treasure, another shows a way out.")
    
    item_encounter("magical artifacts", 1)  # Player encounters a magical artifact
    
    # Player chooses what to do in the hall of mirrors
    choice = input("Do you step through the mirror showing (1) treasure, (2) exit, or (3) your future? ")
    
    if choice == "1":
        print("\nYou step through the mirror and find yourself in a treasure room filled with gold!")
        explore_after_hall_of_mirrors()
    elif choice == "2":
        print("\nYou step through the exit mirror and find yourself back in the main hall.")
        explore_after_hall_of_mirrors()
    elif choice == "3":
        print("\nYou see your future self as a great explorer. Inspired, you feel motivated to continue!")
        explore_after_hall_of_mirrors()
    else:
        print("\nYou hesitate and decide to examine another mirror more closely.")
        explore_after_hall_of_mirrors()

def explore_after_hall_of_mirrors():
    # This function simulates further exploration leading to Tony's encounter
    print("\nAs you look around, you hear a cry for help!")
    print("\nUnkown Figure: Help!! If anyone can hear me please help!!")
    help_npc()  # Call to help NPC function which introduces Tony

def underground_cavern():
    display_boat()  # Function to display ASCII art of a boat
    print("\nYou enter a vast underground cavern with an underground river.")
    print("There's a boat tied to the shore and a narrow path along the cavern wall.")
    print("Suddenly, you hear a rumbling sound. The cavern starts to shake!")
    
    # Player chooses how to react to the danger
    choice = input("Do you (1) run for the boat, (2) take the narrow path, or (3) look for others who might need help? ")
    
    print("\nAs you make your decision, you hear a cry for help!")
    print("You spot someone trapped under some fallen debris. It's another explorer!")
    
    # Regardless of choice, player ends up helping the trapped explorer
    if choice == "1":
        print("\nDespite your initial instinct to flee, you can't ignore the call for help.")
        print("You abandon the boat and rush towards the trapped explorer.")
    elif choice == "2":
        print("\nAs you start along the narrow path, you realize you can't leave someone behind.")
        print("You turn back to help the trapped explorer.")
    elif choice == "3":
        print("\nYour instinct to help others proves right as you spot the trapped explorer.")
    else:
        print("\nYour momentary indecision passes as you focus on the cry for help.")
    
    help_npc()  # Call to help NPC function which introduces Tony

def help_npc(): 
    global player_name
    print("\nYou rush over and help free the trapped explorer.")
    print("Together, you both make it to safety just as more debris falls behind you.")
    print("\nThe explorer turns to you, gratitude in their eyes.")
    print("'Thank you for saving me. I'm Tony Zhao. May I ask your name?'")
    
    print("\nYou tell Tony your name and explain to him your discoveries of the temple thus far.")
    
    print(f"\n'Well, {player_name}, I'm in your debt. I was about to give up hope.'")
    print("Tony looks towards the cavern exit, then back at you.")
    print("'I should probably head back and leave this dangerous place.'")
    
    # Player chooses whether to continue with Tony or not
    choice = input("Do you (1) say goodbye to Tony or (2) invite him to continue the adventure? ")
    
    if choice == "1":
        # Saying goodbye option selected by player 
        print("\nYou bid Tony farewell. He thanks you once more before heading towards the exit.")
        print("You continue your adventure alone, feeling good about helping someone in need.")
        
        # Continue exploration without Tony
        print("\nAs you walk away from the exit, you feel a sense of accomplishment.")
        print("You decide to explore more of the temple on your own.")
        
        continue_adventure_without_tony()  # Function to continue adventure without Tony
    else:
        Tony = True  # Set Tony's presence to True
        print("\n'Continue the adventure? Together?' Tony's eyes light up.")
        print("'You know what? Why not! Let's see what treasures we can find!'")
        print("\nWith your new companion by your side, you press deeper into the temple.")
        tony_adventure()  # Function to continue adventure with Tony

def continue_adventure_without_tony():
    Tony = False
    # Function to continue the adventure when the player decides not to invite Tony
    print("\nYou navigate through the temple's corridors, feeling a mix of excitement and apprehension.")
    
    # Player chooses their next action
    choice = input("Do you want to (1) explore deeper into the temple or (2) search for hidden treasures? ")
    
    if choice == "1":
        # Player chooses to explore deeper
        print("\nYou venture deeper into the temple, discovering ancient carvings on the walls.")
        item_encounter("ancient scrolls", 2)  # Player finds ancient scrolls
        
        # Player faces another choice
        choice = input("Do you want to (1) investigate a strange noise or (2) continue exploring? ")
        
        if choice == "1":
            # Player investigates the noise
            print("\nYou approach the source of the noise and find a hidden chamber!")
            secret_ruin_aura()  # Player encounters the pillars
        else:
            # Player continues exploring
            print("\nYou continue exploring and find a beautiful garden inside the temple.")
            item_encounter("gold coins", 10)  # Player finds gold coins
            secret_ruin_aura()  # Player still encounters the pillars after exploration
    
    elif choice == "2":
        # Player chooses to search for treasures
        print("\nYou search for hidden treasures and find an ornate chest!")
        #display_treasure_chest()  # Function to display ASCII art of a treasure chest (commented out)
        item_encounter("magical artifacts", 3)  # Player finds magical artifacts
        
        # Player faces another choice
        choice = input("Do you want to (1) open the chest or (2) leave it alone? ")
        
        if choice == "1":
            # Player opens the chest
            print("\nYou open the chest and find it filled with gold coins!")
            item_encounter("gold coins", 50)  # Player finds a large amount of gold coins
            secret_ruin_aura()  # Player encounters the pillars after finding treasure
        else:
            # Player leaves the chest alone
            print("\nYou decide it's best not to disturb whatever is inside and continue your journey.")
            secret_ruin_aura()  # Player still encounters the pillars after exploration

def tony_adventure():
    # Function to continue the adventure when the player invites Tony along
    Tony == True
    print("\nWith Tony by your side, you feel more confident exploring the temple's depths.")
    print("Tony: 'You know, I've always dreamed of an adventure like this. Thanks for letting me tag along!'")
    print("His knowledge of ancient languages helps decipher clues you might have missed.")
    
    # Player chooses to learn more about Tony or focus on exploring
    choice = input("Do you want to (1) ask Tony about his background or (2) focus on exploring? ")
    if choice == "1":
        # Player learns about Tony's background
        print("\nTony: 'Well, I'm actually a archeology PhD student at Stanford.'")
        print("Tony: 'I work on reasearching and discovering new information about temples like these, but ancient temples have always fascinated me.'")
        print("Tony: 'But I'm also here in search of a certain individual. Someone who hasn't yet realized their importance to this world.'")
    else:
        # Player focuses on exploring
        print("\nYou nod and continue exploring. Tony seems excited to be here.")
    
    # Players encounter a room with symbols
    print("\nAs you venture deeper, you come across a room with strange symbols on the walls.")
    print("Tony: 'Wait, I recognize these symbols! They're an ancient form of binary code.'")
    print("Tony: 'It says there's a hidden switch somewhere in this room.'")
    
    # Player chooses how to search for the switch
    choice = input("Do you want to (1) search for the switch yourself or (2) ask Tony for help? ")
    if choice == "1":
        # Player searches for the switch
        print("\nYou search the room carefully, but can't seem to find anything.")
        print("Tony: 'Hey, I think I found something! There's a small indentation here.'")
    else:
        # Tony searches for the switch
        print("\nTony: 'Alright, let me take a look. My robotics experience might come in handy.'")
        print("Tony carefully examines the walls and floor.")
        print("Tony: 'Aha! There's a small indentation here. I think it's the switch!'")
    
    # The switch is activated
    print("\nTony presses the switch, and a secret passage opens up.")
    print("Tony: 'Wow, that was exciting! I wonder what other secrets this temple holds.'")
    
    # Players find treasures
    item_encounter("ancient scrolls", 3)
    item_encounter("gold coins", 50)
    
    # Tony discovers an ancient device
    print("\nAs you collect the treasures, Tony notices something.")
    print("Tony: 'Hey, look at this strange device. It seems to be some sort of ancient computer.'")
    print("Tony: 'I might be able to interface with it using some of my AI knowledge.'")
    
    # Player chooses whether to use the device
    choice = input("Do you want to (1) let Tony try to use the device or (2) leave it alone? ")
    if choice == "1":
        # Tony uses the device
        print("\nTony fiddles with the device for a few minutes.")
        print("...")
        display_map()  # Function to display ASCII art of a map
        print("Suddenly, a map appears, showing a secret chamber!")
        print("Tony: 'This is incredible! We've just made a major archaeological discovery!'")
        item_encounter("magical artifacts", 2)  # Players find magical artifacts
    else:
        # Players decide not to use the device
        print("\nYou decide it's safer not to mess with ancient technology.")
        print("Tony looks a bit disappointed but nods in agreement.")
    
    # Players reach the final challenge
    print("\nAfter hours of exploration, you and Tony stand before a massive golden door.")
    print("Ancient symbols cover its surface, promising great riches beyond.")
    print("Tony: 'This is it. Another challenge. Are you ready?'")
    
    # Player chooses whether to open the door or leave
    choice = input("Do you (1) try to open the door or (2) decide it's time to leave with what you've found? ")
    
    if choice == "1":
        # Players open the door
        print("\nTony: 'Alright, let's do this together. On three...'")
        print("Together, you and Tony solve the door's puzzle and push it open.")
        print("A blinding light engulfs you both...")
        secret_ruin_aura()  # Players encounter the pillars
    else:
        # Players decide to leave
        ending_with_tony()  # Function for a ending after players decide to leave temple

def hidden_library():
    display_book()  # Function to display ASCII art of a book
    print("\nYou discover a hidden library filled with ancient scrolls.")
    print("One scroll glows with magical energy, another looks like a map.")
    item_encounter("ancient scrolls", 2)  # Player finds ancient scrolls
    
    # Player chooses what to do in the hidden library
    choice = input("Do you read the (1) glowing scroll, (2) map, or (3) dusty tome on the shelf? ")
    
    if choice == "1":
        # Player reads the glowing scroll
        print("\nYou read the glowing scroll and feel a surge of magical energy.")
        print("Suddenly, you gain insight into the ancient magic of the temple!")
        print("\nYou decide to explore deeper into the library.")
        explore_library()
    elif choice == "2":
        # Player examines the map
        display_holographic_map()  # Function to display ASCII art of a holographic map
        print("\nYou unfold the map and see markings that indicate hidden treasures within the temple.")
        print("This could lead you to great riches!")
        print("\nYou decide to follow the map's directions.")
        follow_map()
    elif choice == "3":
        # Player reads the dusty tome
        print("\nYou open the dusty tome and find it filled with knowledge about ancient rituals.")
        print("You feel wiser just by reading it!")
        print("\nWith newfound knowledge, you look for more secrets in the library.")
        explore_library()
    else:
        # Player leaves the library
        print("\nYou decide to leave the library and continue your adventure elsewhere.")
        continue_adventure()

def explore_library():
    # Function for further exploration in the library
    print("\nAs you explore deeper into the library, you find more scrolls and artifacts.")
    item_encounter("magical artifacts", 1)
    
    choice = input("Do you want to (1) search for more scrolls or (2) leave the library? ")
    
    if choice == "1":
        # Player searches for more scrolls
        print("\nYou search through more shelves and find an ancient artifact!")
        item_encounter("ancient artifact", 1)
        help_npc()
        #secret_ruin_aura()  # Eventually lead to pillars after exploring (commented out)
    else:
        # Player leaves the library
        print("\nYou decide it's time to leave the library and see what else the temple has to offer.")
        continue_adventure()

def follow_map():
    # Function for following the map's directions
    print("\nFollowing the map's directions, you navigate through hidden passages.")
    item_encounter("gold coins", 10)
    
    print("\nEventually, you arrive at a hidden chamber filled with treasures!")
    help_npc()
    # Eventually will lead to pillars after following map 

def continue_adventure():
    # Function to continue the main story after leaving library or making choices
    print("\nYou step out of the library and back into the main hall of the temple.")
    help_npc()
    # Eventually will lead to pillars after continuing adventure 

def jungle_path():
    # Function for exploring the jungle path
    print("\nYou find a hidden path leading into the dense jungle.")
    print("As you follow it, you discover a forgotten shrine.")
    item_encounter("magical artifacts", 1)
    
    print("\nThe shrine is covered in ancient vines and mysterious symbols.")
    choice = input("Do you want to (1) investigate the shrine, (2) explore the surrounding jungle, or (3) look for a way back to the temple? ")
    
    if choice == "1":
        investigate_shrine()
    elif choice == "2":
        explore_jungle()
    else:
        return_to_temple()

def investigate_shrine():
    # Function for investigating the shrine
    print("\nYou approach the shrine, carefully examining the symbols.")
    print("As you touch one of the symbols, it begins to glow!")
    item_encounter("ancient relic", 1)
    
    print("\nSuddenly, the ground beneath you starts to shake.")
    choice = input("Do you (1) stay and see what happens or (2) quickly back away? ")
    
    if choice == "1":
        # Player stays at the shrine
        print("\nThe shrine opens up, revealing a hidden passage!")
        secret_passage()
    else:
        # Player backs away from the shrine
        print("\nYou back away just as the shrine crumbles, revealing a hidden cave entrance.")
        hidden_cave()

def explore_jungle():
    # Function for exploring the jungle
    print("\nYou venture deeper into the lush jungle, pushing through thick vegetation.")
    print("After some time, you hear the sound of rushing water.")
    
    choice = input("Do you (1) head towards the water sound or (2) continue exploring the jungle? ")
    
    if choice == "1":
        # Player heads towards the water
        print("\nYou discover a beautiful waterfall concealing a cave entrance.")
        hidden_cave()
    else:
        # Player continues exploring the jungle
        print("\nAs you explore further, you stumble upon an ancient stone structure.")
        investigate_shrine()

def return_to_temple():
    # Function for returning to the temple
    print("\nYou decide to head back towards the temple.")
    print("As you make your way back, you notice something you missed before...")
    item_encounter("emeralds", 2)
    
    print("\nYou find yourself at a crossroads.")
    choice = input("Do you want to (1) re-enter the temple or (2) explore a bit more? ")
    
    if choice == "1":
        # Player re-enters the temple
        print("\nYou make your way back into the temple.")
        grand_hall()  # The player returns towards the grand hall of the temple
    else:
        # Player explores more
        print("\nYou decide to explore a bit more and find a hidden path.")
        explore_deeper()

def explore_deeper():
    # Function for exploring deeper into the temple
    print("\nYou enter a narrow, winding passage carved into the rock.")
    print("The air is thick with ancient magic.")
    item_encounter("magical artifacts", 2)
    
    print("\nAs you progress, you start to hear voices echoing from somewhere ahead.")
    help_npc()  # Calling the help_npc() function to introduce Tony

def hidden_cave():
    # Function for exploring the hidden cave
    print("\nYou enter the hidden cave, your footsteps echoing in the darkness.")
    print("As your eyes adjust, you see glowing symbols on the walls.")
    item_encounter("ancient scrolls", 2)
    
    print("\nThe cave seems to lead deeper into the earth.")
    choice = input("Do you (1) follow the cave deeper or (2) exit the cave? ")
    
    if choice == "1":
        # Player explores deeper into the cave
        print("\nYou venture deeper into the cave system.")
        print("\nSuddenly, you hear a voice echo off the temple walls, someone is calling for help!")
        help_npc()
    else:
        # Player exits the cave
        print("\nYou decide to exit the cave and find yourself back near the temple.")
        return_to_temple()
        
def post_aura_encounter():
    global Tony, player_power
    
    print("\nAs you enter the next room, you're met with a chaotic scene.")
    print("Two figures are locked in combat with numerous shadowy creatures.")
    print("On one side, a man is cornered by a mob. On the other, another fights off a herd of enemies.")
    
    # Scenario changes based on whether the player obtained an aura power
    if player_power:
        print(f"\nYour {player_power} power surges within you. Without hesitation, you leap into action!")
        print("You blast away the creatures threatening the cornered man with your newfound abilities.")
        print("\nAs the dust settles, you help the man to his feet.")
        print("'Thank you,' he says, catching his breath. 'I'm Ritvik Donga.'")
        
        if Tony == True:
            print("\nMeanwhile, Tony rushes to aid the other fighter.")
            print("'I've got your back!' Tony shouts, joining the fray.")
        
        choice = input("\nDo you want to (1) focus on fighting the mobs or (2) ask about their adventure while fighting? ")
        
        if choice == "1":
            print("\nYou and Ritvik charge towards the herd of mobs, weapons and powers at the ready.")
        else:
            print("\nAs you fight, you ask Ritvik about his journey through the temple.")
            print("Ritvik: 'Kayden and I came here together, but we never saw anything like your powers!'")
    
    else:
        print("\nDespite not having special powers, your martial arts training kicks in.")
        print("You swiftly dispatch the creatures threatening the cornered man.")
        print("\n'Thank you,' he says, catching his breath. 'I'm Ritvik Donga. Please, take this sword.'")
        print("Ritvik hands you a gleaming blade.")
        
        if Tony == True:
            print("\nTony is struggling against the horde on the other side of the room.")
            choice = input("\nDo you want to (1) keep the sword and fight or (2) give Tony the sword and use martial arts? ")
            
            if choice == "1":
                print("\nYou grip the sword tightly and charge into battle alongside Ritvik.")
            else:
                print("\nYou toss the sword to Tony. 'Tony, catch!' You ready your fists for combat.")
        else:
            print("\nYou and Ritvik rush to aid the other fighters against the horde.")
        
        choice = input("\nDo you want to (1) focus on fighting the mobs or (2) ask about their adventure while fighting? ")
        
        if choice == "1":
            print("\nYou and your new allies concentrate on defeating the temple guardians.")
        else:
            print("\nWhile fending off the guardians, you learn about Ritvik and Kayden's adventure.")
            print("They came to the temple together but didn't find the secret aura room.")

    combined_ending()
    
    
       




def ending_with_tony(): # Ending where player leaves with Tony and their treasures, without pursuing the true end
    print("\nTony: 'You're right. We've already found so much. Better not push our luck.'")
    print("You and Tony agree that you've pushed your luck far enough.")
    print("You make your way back to the temple entrance, your bags heavy with treasure.")
    print("\nGame Over.")


def statue_room():
    # Introduce the player to the statue room
    print("\nYou approach one of the golden statues.")
    print("It comes to life, offering you a challenge.")
    
    # Offer the player a chance to find gold coins
    item_encounter("gold coins", 10)
    
    # Ask the player if they want to accept the challenge
    challenge = input("Do you want to accept the statue's challenge? (yes/no): ").lower()
    
    if challenge == "yes":
        # Player accepts the challenge
        print("Statue: Very well....")
        
        # Ask the player the challenge question
        answer = input("\nWhat is the powerhouse of the cell? (answer in all lowercase letters): ").lower()
        
        if answer == "mitochondria":
            # Player answers correctly
            print("Well done explorer... You may progress")
            print("\nYou leave the statue room slightly confused, but victorious.")
            
            # Reward the player with 3 rubies
            add_to_inventory("rubies", 3)
            print("You've been rewarded with 3 rubies!")
            print("Suddenly, you hear a echo from a distance, it sounds like a cry for help!")
            help_npc()
        else:
            # Player answers incorrectly
            print("Statue: Incorrect! Your journey ends here, unworthy one!")
            print("\nThe statue's eyes glow, and you feel a powerful force.")
            
            # Remove 3 random items from the player's inventory
            lose_random_items(3)
            
            # End the game or transition to another ending
            statue_ending()
    
    elif challenge == "no":
        # Player declines the challenge
        print("Explorer... your laziness will burden you in your journey...")
    
    else:
        # Handle invalid input for the challenge response
        print("The statue doesn't understand your response and remains silent.")
        
        # Give the player another chance to choose
        statue_room()  
def lose_random_items(count):
    global inventory
    
    # Determine how many items can be lost (minimum of count and total inventory items)
    items_to_lose = min(count, sum(inventory.values()))
    lost_items = []
    
    # Loop to remove random items
    for _ in range(items_to_lose):
        # Get a list of items that have a quantity greater than 0
        non_empty_items = [item for item, amount in inventory.items() if amount > 0]
        
        if non_empty_items:
            # Choose a random item from the non-empty items
            item = random.choice(non_empty_items)
            # Decrease the quantity of the chosen item by 1
            inventory[item] -= 1
            # Add the item to the list of lost items
            lost_items.append(item)
    
    # Inform the player about the lost items
    if lost_items:
        print(f"\nYou've lost the following items: {', '.join(lost_items)}")
    else:
        print("\nYou had no items to lose!")

        



def statue_ending():
# Player answers incorrectly
    print("Statue: Incorrect! Your journey ends here, unworthy one!")
    print("\nThe statue's eyes glow, and you feel a powerful force.")
            
    # Remove 3 random items from the player's inventory
    lose_random_items(3)
            
    # End the game
    print("\nYou're violently ejected from the temple!")
    print("Game Over!")
    display_inventory()
    exit()  # This ends the game
    
    
def teleportation_accident():
    global player_name
    # Player inputs an invalid input in some of the multichoice segments of the game
    print("\nYour indecision triggers an ancient magic.")
    print("You're teleported to a distant, unknown location.")
    print(f"{player_name}: We go again...")
    print("Game Over..for now...")
    exit()


def combined_ending():
    global player_name
    # Set the scene for the final confrontation
    print("\nAs you continue fighting, you feel a sudden mist float around")
    print("Suddenly, you feel a surge of energy. The room trembles with an ancient power.")
    print(f"\n{player_name}: Alheitus!")
    
    # Time freezes as the player's power activates
    print("\nAs the word leaves your lips, time seems to freeze. The world around you becomes still.")
    print("In this moment of suspended reality, seven shimmering portals materialize before you.")
    print("Each portal pulses with a unique energy, calling to you in different ways.")
    
    # Present the player with portal choices
    print("\nWhich portal draws your attention?")
    print("1. A portal radiating brilliant, blinding light")
    print("2. A portal that seems to ripple and shift, showing glimpses of familiar scenes")
    print("3. A portal crackling with chaotic energy, revealing flashes of a war-torn world")
    print("4. A portal that pulses with a rhythm that matches your heartbeat")
    print("5. A portal that feels ancient and wise, as if it has existed for eons")
    print("6. A portal that exudes a sense of noble sacrifice and heroism")
    print("7. A portal that seems ordinary at first glance, but you sense a hidden depth")
    
    # Player makes their choice
    choice = input("As time stands still, you must choose. Enter the number of the portal (1-7): ")
    
    # Time resumes and the effects of the player's power are shown
    print("\nAs you make your choice, time resumes. The word 'Alheitus' echoes through the chamber.")
    print("The guardians get crushed by a compression force, causing them to collapse.")
    print("The portal you chose flares brightly, its energy merging with your newfound power.")
    
    # Determine the ending variation based on the player's choice
    if choice == "1":
        ending_variation = "enlightened"
    elif choice == "2":
        ending_variation = "time_loop"
    elif choice == "3":
        ending_variation = "alternate_reality"
    elif choice == "4":
        ending_variation = "fusion"
    elif choice == "5":
        ending_variation = "reincarnation"
    elif choice == "6":
        ending_variation = "sacrifice"
    elif choice == "7":
        ending_variation = "tony"
    else:
        print("As the moment of choice passes, the portals merge into one.")
        ending_variation = "default"
    
    # Transition to meeting Ritvik and Kayden
    print("\nAs the dust settles, you find yourself face to face with Ritvik and Kayden.")
    
    # Different dialogue and events based on the chosen ending variation
    if ending_variation == "enlightened":
        print("\nCosmic knowledge floods your mind, and you understand your true purpose.")
        print("Ritvik and Kayden find you, realizing you've already awakened to your powers.")
        print("\nRitvik: 'The chosen one has awakened on their own!'")
    elif ending_variation == "time_loop":
        print("\nYou recognize Ritvik and Kayden, memories of past loops flooding back.")
        print("\nKayden: 'You've completed the loop. Now, you're ready for your true mission.'")
    elif ending_variation == "alternate_reality":
        print("\nThe world around you is in chaos. Ritvik and Kayden appear, leading a resistance.")
        print("\nRitvik: 'You've arrived! Our world needs the chosen one more than ever.'")
    elif ending_variation == "fusion":
        print("\nYou feel the temple's magic fusing with your being, transforming you.")
        print("Ritvik and Kayden arrive, astonished by your transformation.")
        print("\nKayden: 'The prophecy didn't prepare us for this. You're more than the chosen one.'")
    elif ending_variation == "reincarnation":
        print("\nMemories of past lives flood your mind as you face Ritvik and Kayden.")
        print("\nRitvik: 'You remember now, don't you? This cycle, we'll finally succeed.'")
    elif ending_variation == "sacrifice":
        print("\nExhausted from the energy surge, you collapse as Ritvik and Kayden rush to your aid.")
        print("Kayden: 'The chosen one has sacrificed so much already. We must support them.'")
        print("Ritvik: 'If you let us, we can take you to get healed.'")
        print(f"\n{player_name}: Take me..? But where?")
    elif ending_variation == "tony":
        print("\nAs Ritvik and Kayden approach, a familiar figure emerges from the shadows.")
        print("Tony: 'I knew you had it in you, kid. Sorry for the cryptic messages earlier.'")
        print("Ritvik and Kayden exchange surprised glances.")
        print("\nRitvik: 'Tony? You've been guiding the chosen one all along?'")
    else:
        print("\nRitvik and Kayden appear, looking relieved to have found you.")
    
    # Common dialogue for all endings
    print("\nRitvik: (Looks like we've found him...Earth's hidden prophecy..)")
    print(f"\nKayden approaches you. 'Listen, {player_name}, we've been searching for you. Come with us.'")
    print(f"{player_name}: Hold on, what do you mean you've been searching for me? And where are we going? What is all this?")
    print("\nRitvik: You are the chosen one...")
    
    # Additional dialogue for Tony's ending
    if ending_variation == "tony":
        print("\nTony steps forward: 'I know it's a lot to take in, but trust me, it's all true.'")
        print("'I've been watching over you, preparing you for this moment.'")
    
    print("\nKayden: There's no time to explain everything now, you're just gonna have to trust us, the world depends on it.")
    
    # Final choice for the player
    final_choice = input("\nDo you choose to (1) go with Ritvik and Kayden, or (2) seek answers on your own? ")
    
    # Outcome based on the player's final choice
    if final_choice == "1":
        # Player chooses to go with Ritvik and Kayden
        print("\nYou decide to trust Ritvik and Kayden, embarking on a new adventure to save the world.")
        if ending_variation == "tony":
            print("Tony nods approvingly, ready to join your quest.")
        print("\nAs you leave with your new allies, you feel a mix of excitement and apprehension.")
        print("The weight of your destiny as the chosen one begins to sink in.")
        print("Whatever challenges lie ahead, you know you won't face them alone.")
        print("\nYour journey to save the world has only just begun...")
    elif final_choice == "2":
        # Player chooses to seek answers on their own
        print("\nYou decide to find answers on your own, declining to go with Ritvik and Kayden.")
        print("Their faces show a mix of disappointment and understanding.")
        print("\nRitvik: 'We understand, but please be careful. You may not realize this now, but the fate of the world still rests on your shoulders. '")
        print("Kayden: 'The day you realize this is the day you come searching for us again. We will be waiting for your arrival...'")
        if ending_variation == "tony":
            print("\nTony steps forward: 'Kid, I know it's overwhelming, but don't shut everyone out.'")
            print("'I'll be around if you need me. Just remember, sometimes it's okay to lean on others.'")
        print("\nAs you turn to leave, you feel the weight of your decision.")
        print("The path ahead is uncertain, but you're determined to uncover the truth about your powers and your destiny.")
        print("Your journey of self-discovery and world-saving has only just begun, but on your own terms...")
    else:
        # Player makes an invalid choice
        print("\nUnable to make a decision, you stand frozen in place.")
        print("Ritvik and Kayden exchange worried glances.")
        print("\nKayden: 'I know it's a lot to take in. Why don't you come with us for now, and you can decide your path later?'")
        print("Reluctantly, you nod and follow them, your mind swirling with unanswered questions.")
        print("\nYour journey begins with uncertainty, but perhaps clarity will come in time...")

    # End of the game
    print("\nTHE END")

    
# Calls the function to start the game    
start_game()
