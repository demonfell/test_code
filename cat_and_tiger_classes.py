class Cat:
    x_coordinate = 0
    y_coordinate = 0
    lives = 9
    size = "small"
    animal_name = "cat"

    def __init__(self, breed, color):
        self.breed = breed
        self.color = color

    def walk(self):
        self.x_coordinate +=1

    def run(self):
        self.x_coordinate +=2
    
    def pounce(self):
        """
        would need to implement gravity for the cat to come back down
        """
        self.y_coordinate +=1
        self.x_coordinate +=1
    
    def eat(self, food):
        print("The {} ate {}.".format(self.animal_name, food))


class Tiger(Cat):
    size = "large"
    animal_name = "tiger"

    def __init__(self, breed, color):
        super().__init__(breed, breed)
        super().__init__(color, color)

    def walk(self):
        self.x_coordinate +=2

    def run(self):
        self.x_coordinate += 4

    def pounce(self):
        """
        would need to implement gravity for the cat to come back down
        Tigers jump longer, not higher
        """
        self.x_coordinate +=2
        self.y_coordinate +=1
    

    
    



