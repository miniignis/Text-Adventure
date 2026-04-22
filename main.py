import random

# SETUP GAME LOGIC
def resetGameData():
    return {
        "alive" : True,
        "health" : 3,
        "inventory" : [
            "pocket lint"
        ],
        "sights" : [] # Locations or things the player has seen.
    }

game = resetGameData()
name = ""
endingProgress = { # These are changed to True when the ending is achieved.
    "Sleep" : False,
    "Sheltered" : False,
    "Death" : False,
    "King" : False,
    "Draw" : False,
    "Frozen" : False
}

def getAction(prompt):
    response = input(prompt + "\n")
    while response.isdigit():
        print("Invalid input... try again.\n")
        response = input(prompt + "\n")
    return response.lower() # Return response is lowercase to make things easier.

# GAMEPLAY
def setup():
    resetGameData()
    print("\t== ENDING PROGRESS ==")
    for key, value in endingProgress.items():
        print(key + " Ending : " + str(value))
    print("\t=====================")
    print("\n\nYou wake up in a prison cell.\nYour name is " + name + ", and you have no recollection of how you arrived here.")
    prison_cell()

# PRISON CELL CHOICES
def display_inventory():
    print("\n\nYour current inventory:")
    for item in game["inventory"]:
        print(item)

def prison_cell_look():
    print("\n\nYou look around the room.\nThere's dirt and grime all along the walls and floors, spiderwebs are tucked into nearly every little corner of the room. Gross.\nThe only exit is a steel door. It's locked.")
    prison_cell()

def prison_cell_sleep():
    print("\n\nAll things considered, you'd much rather go back to bed.\nYou relax in the same mold-invested bed you woke up in and fall sleep.\nTHE END!")
    endingProgress["Sleep"] = True

def prison_cell_scavenge():
    if "cell key" in game["inventory"]: #If they already have the key, don't do anything.
        print("\n\nThere's nothing else to look for.\nThe room is torn up by your previous search.")
        prison_cell()

    print("\n\nYou search for anything of use.\nBy the end of your search, you found a key and an old lighter")
    game["inventory"].append("cell key")
    game["inventory"].append("lighter")
    prison_cell()

def prison_cell():
    action = getAction("What now? You can LOOK, LEAVE, SCAVENGE, SLEEP, or check your INVENTORY.")
    match(action):
        case "look":
            prison_cell_look()
        case "leave":
            if "cell key" in game["inventory"]:
                print("\n\nAfter unlocking the door, you step outside to see... nothing.\nIt's completely dark!\nYou use the lighter from earlier to find your way around.")
                hallway()
            else:
                print("\n\nThe door keeping you inside is locked...")
                prison_cell()
        case "sleep":
            prison_cell_sleep()
        case "scavenge":
            prison_cell_scavenge()
        case "inventory":
            display_inventory()
            prison_cell()
        case _:
            print("That's not an option. Try again.\n")
            prison_cell()

def hallway():
    action = getAction("What now? You can GO LEFT or GO RIGHT.")
    match(action):
        case "go left":
            print("\n\nThe air grows colder as you go further to the left.\nYou almost turned back because of the freezing temperature, but a light at the end of it kept you going. An exit!\n Going through it, you learn that you are in the middle of a vast, snowing tundra.")
            tundra()
        case "go right":
            print("\n\nThe air grows hotter as you go further to the right.\nYou almost turned back because of the scorching heat, but a light at the end of it kept you going. An exit?\nIt was not.\nWhen you reach the end you find the source of the light was a campfire, one lit by what you can assume are several other prisoners.\nThey don't look friendly.")
            game["sights"].append("bandits")
            bandits()
        case _:
            print("That's not an option. Try again.\n")
            hallway()

def tundra():
    action = getAction("What now? You can LOOK or LEAVE.")
    match(action):
        case "look":
            print("\n\nThe only thing you can see through the heavy snowfall is a small cabin a short distance away. \nIt's almost entirely buried in snow, but it'd be suitable shelter from the temperature.")
            game["sights"].append("cabin")
            tundra()
        case "leave":
            if "cabin" in game["sights"]:
                print("\n\nSeeing nothing else in the frozen landscape, you make a run for the cabin.\nYou manage to reach it and take shelter before hypothermia sets in.\nIt's incredibly cozy inside the cabin, unlike your rotting cell from before.\nThere's a phone nearby.")
                cabin()
            else:
                print("\n\nYour newfound sense of freedom clearly got the best of you, and you ran out into the snowstorm without a second thought!\nYou freeze to death an hour later.\nTHE END.")
                endingProgress["Frozen"] = True

        case _:
            print("That's not an option. Try again.\n")
            tundra()

def cabin():
    action = getAction("What now? You can finally REST.")
    match(action):
        case "rest":
            print("After such a long trip in the cold, you decide resting is the best option.\nYou crawl into bed and fall asleep, planning on using the phone to call for help later.\nTHE END.")
            endingProgress["Sheltered"] = True

        case _:
            print("That's not an option. Try again.\n")
            cabin() 

def bandits():
    action = getAction("What now? You can FIGHT or RUN.")
    match(action):
        case "fight":
            print("\n\nYou weren't raised a coward. You stay in place as one of them gets up to deal with you.")
            fight()
        case "run":
            print("\n\nYou don't stick around for long, and quickly flee the scene back to the dark hallway.\nYou go left this time.")
            print("\n\nThe air grows colder as you go further to the left.\nYou almost turned back because of the freezing temperature, but a light at the end of it kept you going (plus, those bandits would've probably killed you). An exit!\n Going through it, you learn that you are in the middle of a vast, snowing tundra.")
            tundra()
        case _:
            print("That's not an option. Try again.\n")
            bandits()

def fight():
    print("\n\nThe fight begins!")
    foeHealth = 3 # Only have to hit them 3 times.
    while foeHealth > 0 and game["health"] > 0:
        foeRoll = random.random() # Determines what the enemy will do.
        braced = False # If the player is bracing themselves or not.

        if foeRoll > 0.5: # > 0.5 = HURT.
            print("The bandit is winding up a nasty punch...")
        else:
            print("The bandit is taking a breather...")


        action = getAction("Quick, what do you do? You can ATTACK or BRACE.")
        match(action):
            case "attack":
                print("\n\nYou strike a mean blow to them!")
                foeHealth -= 1
            case "brace":
                print("\n\nYou brace yourself for their next attack.")
                braced = True
            case _:
                print("Not an option. Turn wasted.\n")

        if foeRoll > 0.5: # > 0.5 = HURT.
            print("The bandit attempts to hit you...")
            if braced:
                print("but with your guard up, it did nothing!")
            else:
                print("You get hit hard and bleed a little.")
                game["health"] -= 1
        else:
            print("The bandit gets ready.")
            if braced:
                print("Bracing did nothing.")

    if game["health"] <= 0:
        print("\n\nUnfortunately, you were no match for them.\nYou die on the ground, wounded.\nTHE END.")
        endingProgress["Death"] = True

    elif foeHealth <= 0:
        print("\n\nYou won! The bandit staggers backwards and collapses onto the ground.\nThey're dead.\nThe rest of the bandits look at you in shock and quickly surrender. You gain enough supplies from them to live like a king for a long, long time.\nTHE END.")
        endingProgress["King"] = True
    
    if game["health"] <= 0 and foeHealth <= 0:
        print("\n\nYou were both evenly matched! Both you and the bandit collapse, exhausted from the fight.\nWhile it was a tie, you showed off your capabilities and that was enough for you to join their ranks.\nTHE END.")
        endingProgress["Draw"] = True


# Game loop (allows for replaying & ending tracking.)
name = getAction("Before the game starts, what is your name?")
setup()
while True:
    running = getAction("Play again?: (Y/N)")
    if running != "y":
        break
    setup()