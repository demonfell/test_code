import random
import turtle
t = turtle.Pen()
directions = ['left', 'right', 'forward', 'back']
random_stop = random.randrange(50,256)
for i in range(0,random_stop):
    if i < random_stop:
        chosen_direction = random.choice(directions)
        random_write = random.randrange(10,32)
        getattr(t,chosen_direction)(random_write)