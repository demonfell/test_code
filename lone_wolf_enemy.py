import random

class LoneWolfEnemy:
    enemy_properties = {
                    'giak': {'pretty_race':'Giak', 'cs_lower':10, 'cs_upper':12, 'end_lower': 10, 'end_upper': 15, 'immunity':''},
                    'dark_human': {'pretty_race':'Dark Human', 'cs_lower':12, 'cs_upper':14, 'end_lower': 13, 'end_upper': 18, 'immunity':''},
                    'gourgaz': {'pretty_race':'Gourgaz', 'cs_lower':12, 'cs_upper':17, 'end_lower': 28, 'end_upper': 30, 'immunity':'mindblast'}
    }

    def __init__(self, race):
        if race in self.enemy_properties:
            self.race = race
            self.pretty_race = self.enemy_properties[race]['pretty_race']
            self.immunity = self.enemy_properties[race]['immunity']
            self.cs_lower = self.enemy_properties[race]['cs_lower']
            self.cs_upper = self.enemy_properties[race]['cs_upper']
            self.end_lower = self.enemy_properties[race]['end_lower']
            self.end_upper = self.enemy_properties[race]['end_upper']
            self.endurance = random.choice([x for x in range(self.end_lower,self.end_upper)])
            self.combat_skill = random.choice([x for x in range(self.cs_lower,self.cs_upper)])
            self.isalive = True
        else:
            raise IndexError('Enemy race must be predefined.')

    def take_damage(self, amount):
        self.endurance -= amount
        if self.endurance <= 0:
            self.dies()
        
    def dies(self):
        print("The {} is dead.".format(self.pretty_race))
        self.isalive = False

def describe_enemy(enemy_type):
    print("You are fighting a {} with Combat Skill {} and {} Endurance points.".format(enemy_type.pretty_race, enemy_type.combat_skill, enemy_type.endurance))
    if enemy_type.immunity:
        print("The {} is immune to {}.".format(enemy_type.pretty_race,enemy_type.immunity))

