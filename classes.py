import random
from controller import cycle_wait
import data
import dialog

class Character:
    def __init__(self, name, health, current_health, attack, defence, level) -> None:
        self.name = name
        self.health = health
        self. current_health = current_health
        self.attack = attack
        self.defence = defence
        self.level = level

    

class Player(Character):
    def __init__(self, name, p_class, health, current_health, attack, defence, accuracy, evasion, level=1, exp=0, level_up_signal=False, temp_def=0) -> None:
        super().__init__(name, health, current_health, attack, defence, level)
        self.p_class = p_class
        self.accuracy = accuracy
        self.evasion = evasion
        self.exp = exp
        self.level_up_signal = level_up_signal
        self.temp_def = temp_def

    def info(self):
        print(f"You are {self.name}, a great {self.p_class} roaming the lands.\n"\
            f"Your attack is {self.attack}\n"\
            f"Your defence is {self.defence}\n")
        if self.accuracy <= 20:
            print("You can barely hit a tree that's standing still")
        elif self.accuracy <= 60:
            print("You're fairly accurate.")
        elif self.accuracy <= 90:
            print("You can almost guarantee a hit on a target.")
        else:
            print("Even if you close your eyes and swing in the other direction, you'll probably hit.")

        if self.evasion <= 20:
            print("You better hope the enemy is blind.")
        elif self.evasion <= 60:
            print("Sometimes you dodge, sometimes you don't.")
        elif self.evasion <= 90:
            print("You move like a majestic butterfly. Enemies can barely land a hit.'")
        else:
            print("You always wondered if somebody could hit you even if you didn't move.")
        print(f"You currently have {self.current_health} HP.\n"\
            f"You are currently level {self.level}\n")
        cycle_wait(2)

    def fight(self, defence, enemy_hp):
        self.temp_def = 0

        hit = random.randint(0, 100)
        if hit > int(self.accuracy):
            print(dialog.miss)
            cycle_wait(.5)
        else:
            dmg_min = data.DaV[self.level][0]
            dmg_max = data.DaV[self.level][1]
            damage_dealt = (int(self.attack) + random.randint(dmg_min, dmg_max)) - int(defence)
            if damage_dealt < 0: damage_dealt = 0
            print(f"You dealt {damage_dealt} damage.")
            enemy_hp = enemy_hp - damage_dealt
            if enemy_hp < 0: enemy_hp = 0
            cycle_wait(.5)
        return enemy_hp

    def defend(self):
        print(dialog.defend)
        self.temp_def = random.randint(data.DeV[self.level][0], data.DeV[self.level][1])
        cycle_wait(.5)

    def level_up(self):
        if int(self.level) < 20: #Level cap of 20
            if self.p_class == "warrior":
                class_values = list(data.stats_warrior.values())
            elif self.p_class == "juggernaut":
                class_values = list(data.stats_juggernaut.values())
            elif self.p_class == "ninja":
                class_values = list(data.stats_ninja.values())
            elif self.p_class == "mage":
                class_values = list(data.stats_mage.values())
            
            self.attack += random.randint(int(class_values[0]), int(class_values[1]))
            self.defence += random.randint(int(class_values[2]), int(class_values[3]))
            self.health += random.randint(int(class_values[4]), int(class_values[5]))
            self.accuracy += random.randint(int(class_values[6]), int(class_values[7]))
            self.evasion += random.randint(int(class_values[8]), int(class_values[9]))

            self.current_health = self.health
            self.level += 1
            self.level_up_signal = False
            print(f"{dialog.level_up} {self.level}")

    def exp_listener(self, exp_get):
        self.exp = int(self.exp + exp_get)
        if self.exp >= data.exp_table[self.level]:
            self.level_up_signal = True

    def run(self, enemy):
        self.temp_def = 0

        value = random.randint(1, 100)
        if enemy == "goblin":
            escape_chance = list(data.EsP[0])
        elif enemy == "bandit":
            escape_chance = list(data.EsP[1])
        elif enemy == "bandit chief":
            escape_chance = list(data.EsP[2])
        elif enemy == "exiled warrior":
            escape_chance = list(data.EsP[3])
        elif enemy == "zombie":
            escape_chance = list(data.EsP[4])
        elif enemy == "undead knight":
            escape_chance = list(data.EsP[5])
        elif enemy == "elf assassin":
            escape_chance = list(data.EsP[6])
        elif enemy == "mad juggernaut":
            escape_chance = list(data.EsP[7])
        elif enemy == "lesser demon":
            escape_chance = list(data.EsP[8])
        elif enemy == "dragon":
            escape_chance = list(data.EsP[9])
        
        if value >= escape_chance[0] and value <= escape_chance[1]:
            print(dialog.escape_yes)
        else:
            print(dialog.escape_no)




class Enemy():
    def __init__(self, name) -> None:
        self.name = name
        
    def summon(self, c_health):
        if self.name == "goblin":
            monster_stats = list(data.stats_goblin.values())
        elif self.name == "bandit":
            monster_stats = list(data.stats_bandit.values())
        elif self.name == "bandit chief":
            monster_stats = list(data.stats_bandit_chief.values())
        elif self.name == "exiled warrior":
            monster_stats = list(data.stats_exiled_warrior.values())
        elif self.name == "zombie":
            monster_stats = list(data.stats_zombie.values())
        elif self.name == "undead knight":
            monster_stats = list(data.stats_undead_knight.values())
        elif self.name == "elf assassin":
            monster_stats = list(data.stats_elf_assassin.values())
        elif self.name == "mad juggernaut":
            monster_stats = list(data.stats_mad_juggernaut.values())
        elif self.name == "lesser demon":
            monster_stats = list(data.stats_lesser_demon.values())
        elif self.name == "dragon":
            monster_stats = list(data.stats_dragon.values())

        self.attack = int(monster_stats[1])
        self.defence = int(monster_stats[2])
        self.health = int(monster_stats[3])
        self.exp = int(monster_stats[4])
        self.current_health = 0
        if c_health <= 0:
            self.current_health = self.health
        elif c_health != self.health:
            self.current_health = c_health

    def info(self):
        if self.name == "goblin":
            print(data.descr_goblin)
        elif self.name == "bandit":
            print(data.descr_bandit)
        elif self.name == "bandit chief":
            print(data.descr_bandit_chief)
        elif self.name == "exiled warrior":
            print(data.descr_exiled_warrior)
        elif self.name == "zombie":
            print(data.descr_zombie)
        elif self.name == "undead knight":
            print(data.descr_undead_knight)
        elif self.name == "elf assassin":
            print(data.descr_elf_assassin)
        elif self.name == "mad juggernaut":
            print(data.descr_mad_juggernaut)
        elif self.name == "lesser demon":
            print(data.descr_lesser_demon)
        elif self.name == "dragon":
            print(data.descr_dragon)
        cycle_wait(2)

    def fight(self, evasion, player_hp, lvl, defence, temp_defence):
        print(dialog.enemy_attacks)
        cycle_wait(.5)
        hit = random.randint(0, 100)
        if hit <= evasion:
            print(dialog.player_dodge)
            cycle_wait(.5)
        else:
            dmg_min = data.DaV[lvl][0]
            dmg_max = data.DaV[lvl][1]
            damage_dealt = (self.attack + random.randint(dmg_min, dmg_max)) - (defence + temp_defence)
            if damage_dealt < 0: damage_dealt = 0
            print(f"The {self.name} hit you for {damage_dealt} damage.")
            player_hp = player_hp - damage_dealt
            if player_hp < 0: player_hp = 0
            cycle_wait(.5)
        return player_hp


def enemy_generator(level):
    value = random.randint(1, 100)
    if value > data.EP[level][0][0] and value <= data.EP[level][0][1]: return "goblin"
    if value > data.EP[level][1][0] and value <= data.EP[level][1][1]: return "bandit"
    if value > data.EP[level][2][0] and value <= data.EP[level][2][1]: return "bandit chief"
    if value > data.EP[level][3][0] and value <= data.EP[level][3][1]: return "exiled warrior"
    if value > data.EP[level][4][0] and value <= data.EP[level][4][1]: return "zombie"
    if value > data.EP[level][5][0] and value <= data.EP[level][5][1]: return "undead knight"
    if value > data.EP[level][6][0] and value <= data.EP[level][6][1]: return "elf assassin"
    if value > data.EP[level][7][0] and value <= data.EP[level][7][1]: return "mad juggernaut"
    if value > data.EP[level][8][0] and value <= data.EP[level][8][1]: return "lesser demon"
    if value > data.EP[level][9][0] and value <= data.EP[level][9][1]: return "dragon"

