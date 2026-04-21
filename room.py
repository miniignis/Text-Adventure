class Room:
    def __init__(self, description = "Oops!", items = []): # Ideally they don't see a default room...
        self.description = description
        self.items = items.copy()
    
    def getDescription(self):
        description = self.description + "\nLooking around, you see the following: \n"
        for x in self.items:
            description += "a " + x.name + ", "
        return description