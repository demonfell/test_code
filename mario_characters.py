class SuperMario:
    """
    What a Super Mario character can do.
    """
    size = 'small'
    has_fire = False
    x_coordinate = 0
    y_coordinate = 0
    lives = 3
    
    def __init__(self):
        self.sprite = "mario"
        self.speed = 4
        self.jump_height = 4
        self.power = 4

    def jump(self):
        """
        would need to implement gravity for the character to come back down
        """
        self.distance = self.power // 2
        self.height = self.jump_height
        self.y_coordinate += self.distance
        self.x_coordinate += self.height

    def walk(self):
        self.x_coordinate += self.speed // 2

    def run(self):
        self.x_coordinate += ((self.speed * 2) // 2)

    def eat_mushroom(self):
        self.size = 'big'

    def eat_flower(self):
        if self.size == 'big':
            self.has_fire = True

    def shoot_fire(self):
        if self.has_fire:
            print("Pow, pow!")

    def take_damage(self):
        if self.size == 'big':
           self.size = 'small'
        elif self.size == 'small':
           self.lives -= 1
           print("Flies off the screen")


class Luigi(SuperMario):
    """
    What Luigi can do.
    """
    
    def __init__(self):
        self.sprite = "luigi"
        self.speed = 3
        self.jump_height = 4
        self.power = 3

class Toad(SuperMario):
    """
    What Toad can do.
    """
    
    def __init__(self):
        self.sprite = "toad"
        self.speed = 5
        self.jump_height = 2
        self.power = 5

class PrincessPeach(SuperMario):
    def __init__(self):
        self.sprite = "peach"
        self.speed = 2
        self.jump_height = 3
        self.power = 2

    # could not figure out how to work super() into this...   
    def jump(self):
        """
        would need to implement gravity for the character to come back down
        """
        self.distance = self.power * 4
        self.height = self.jump_height
        self.x_coordinate += self.distance
        self.y_coordinate += self.height
