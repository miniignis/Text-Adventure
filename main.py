game = {
    "alive" : True,
    "name" : "",
    "inventory" : [],
}

def getAction(prompt):
    response = input(prompt + "\n")
    while response.isdigit():
        print("Invalid input... try again.\n")
        response = input(prompt + "\n")
    return response.lower() # Return response is lowercase to make things easier.

def setup():
    game["name"] = getAction("Before the game starts, what is your name?")
    prison_cell()

def sleep():
    print("\n\nAll things considered, you'd much rather go back to bed.\nYou relax in the same mold-invested bed you woke up in and fall sleep.\nTHE END!")

def prison_cell():
    print("\n\nYou wake up in a prison cell.\nYour name is " + game["name"] + ", and you have no recollection of how you arrived here.")

    action = getAction("What now? You can LOOK, SLEEP, or INVENTORY.")

    match(action):
        case "look":
            pass
        case "sleep":
            sleep()
        case "inventory":
            pass
        case _:
            print("That's not an option. Try again.\n")
            prison_cell()

setup()