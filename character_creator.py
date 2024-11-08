from random import *
from entity import *
from math import *
from time import *
from config import *
from Abilities import *
from Items import *

def character_creator():
    classes = {
        "Knight":
    }
    name = input("Enter your character's name: ")
    while True:
        slow_text("Choose a class:", delay=0.5)
        slow_text("1: Knight", delay=0.5)
        k_max_health, k_current_health, K_damage, k_defense, k_dodge_chance, k_crit_chance, k_max_mana, k_current_mana = 350, 350, 80, 50, 20.0, 35.0, 80, 80 
        slow_text("2: Mage", delay=0.5)
        m_max_health, m_current_health, m_damage, m_defense, m_dodge_chance, m_crit_chance, m_max_mana, m_current_mana = 350, 350, 80, 50, 20.0, 35.0, 80, 80
        slow_text("3: Archer", delay=0.5)
        class_choice = input('Choose the number of the class you wish to obtain.')
        if class_choice == 1:
            pclass = "Knight"
        elif class_choice == 2:
            pclass = "Mage"
        elif class_choice == 3:
            pclass = "Archer"
        slow_text(f"You have chose {pclass}. Is that okay?")
        print("1. Yes")
        print("2. No")
        yesorno = input("  ")
        if yesorno == 2: 
            pass
        else:
            pass





