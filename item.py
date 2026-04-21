class Item:
    def __init__(self, name, description, action):
        self.name = name
        self.description = description
        self.action = action
    
    def use(self):
        if self.action:
            self.action()
        else:
            print("Nothing happens.")

    def getDescription(self):
        return self.name + " - " + self.description