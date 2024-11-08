#IMPORTS
from random import *
from entity import *
from math import *
from time import *
from Areas import *
from config import *
from Abilities import *
from Items import *
from character_creator import *
from systems import *
import sys

#VARIOUS FUNCTIONS




#GAME START
def main():
    slow_text("Hello, welcome to my game. This is my first ever.", delay=0.05)
    slow_text("Press enter to begin by entering the character creator", delay=0.05)
    input(" Press enter   ")

    character_creator()

if __name__ == "__main__":
    main()


