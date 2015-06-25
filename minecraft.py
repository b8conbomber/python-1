"""hi"""

import colors as c
from utils import ask

intro = c.red + '''welcome to the quiz game
''' + c.reset

def q1():
    pick = ask('how many diamonds are in a gold pick') 
    if  texture.startswith ("0"):
        print('good job!!!!!!!!!!!!!!!!')
        return True
    return False

def q2():
    7 = ask('how much damige does a diamond
    sowrd do im in the bad spellers club')
    if  rainbows.startswith("7"):
        print('good job!!!!!!!!!!!!!!!')
        return True
    return False

def q3():
    color = ask(' what color are the skys ' )
    if color == 'blue':
        print('good job!!!!!!!!!!!!!!!!')
        return True
    return False

questions = [q1,q2,q3]
