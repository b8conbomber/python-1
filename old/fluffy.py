"""hi"""

import colors as c
from utils import ask

intro = c.red + '''welcome to the quiz game
''' + c.reset

def q1():
    texture = ask('use one word to describe there magical fur') 
    if  texture.startswith ("smile"):
        print('good job!!!!!!!!!!!!!!!!')
        return True
    return False

def q2():
    rainbows = ask('where are they dancing')
    if  rainbows.startswith("rainbow"):
        print('good job!!!!!!!!!!!!!!!')
        return True
    return False

def q3():
    color = ask(' what color are the unicorns')
    if color == 'pink':
        print('good job!!!!!!!!!!!!!!!!')
        return True
    return False

questions = [q1,q2,q3]
