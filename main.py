import room
import item

def getAction(prompt):
    response = input(prompt + "\n")
    return response.lower() # Return response is lowercase to make things easier.

# Item management (Inventory)
inventory = [None] * 3 # Only three slots for inventory space, for now.

# No idea how this works, but it's a 4x4 array for room storage.
w, h = 4, 4
layout = [[0 for x in range(w)] for y in range(h)] # ???

currentRoom = (0, 0) # Starting room
layout[0][0] = room.Room("You stand inside a concrete prison cell.", [item.Item("rotten apple", "It's a disgusting moldy apple.", None)])

# Game Loop
print(layout[currentRoom[0]][currentRoom[1]].getDescription())