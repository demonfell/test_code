class Refrigerator:
    """
    Class of an appliance - Chapter 21, exercise 4
    """
    door_closed = True
    fridge_contents = []
  
    def __init__(self, model, color, manufacturer):
        self.color = color
        self.manufacturer = manufacturer
        self.model = model
    
    def close_door(self):
        if self.door_closed == False:
            self.door_closed = True
        else:
            print("Door is already closed.") 

    def open_door(self):
        if self.door_closed == True:
            self.door_closed = False
        else:
            print("Door is already open.")

    def look_fridge(self):
        if self.door_closed == True:
            print("Door is closed.")
        else:
            print("Door is open.")
            if not self.fridge_contents:
                print("Fridge is empty")
            else:
                for my_item in self.fridge_contents:
                    print(my_item)

    def take_item(self, item):
        if self.door_closed == False:
            if item in self.fridge_contents:
                self.fridge_contents.remove(item)
                print("You took {}".format(item))
        else: 
            print("You must open the door first.")

    def put_item(self, item):
        if self.door_closed == False:
                self.fridge_contents.append(item)
                print("You put {} in the fridge.".format(item))
        else: 
            print("You must open the door first.")






