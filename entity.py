class Entitys:
    def __init__(self, name, level, max_health, current_health, damage, defense, dodge_chance,
                 crit_chance,):
        self.name = name
        self.level = level
        self.max_health = max_health 
        self.current_health = current_health
        self.can_act = True
        self.is_turn = False
        self.in_battle = False
        self.damage = damage
        self.defense = defense
        self.dodge_chance = dodge_chance
        self.crit_chance = crit_chance

class Player(Entitys):
    def __init__(self, name, level, max_health, current_health, max_mana, current_mana, starting_class, current_equipped_weapon, damage, defense, dodge_chance,
                 crit_chance,):
        super().__init__(name, level, max_health, current_health, damage, defense, dodge_chance,
                 crit_chance,)
        self.max_mana = max_mana
        self.current_mana = current_mana
        self.starting_class = starting_class
        current_exp=0,
        exp_requirement=100,
        self.inventory = []
        self.status_ailments = []
        self.current_equipped_weapon = current_equipped_weapon
        
        self.existance = 1
        
        

class Normal_Enemy(Entitys):
    def __init__(self, name, level, max_health, current_health, enemy_type, base_ailment, current_equipped_weapon):
        super().__init__(name, level, max_health, current_health)
        self.drops = []
        self.enemy_type = enemy_type
        self.base_ailment = base_ailment
        self.status_ailments = []
        self.current_equipped_weapon = current_equipped_weapon
        


        