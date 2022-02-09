#   PLAYER ------------------------------------------
list_of_classes = ["warrior", "juggernaut", "ninja", "mage"]

# Stats table for leveling
stats_warrior = {
    "attack_min": 2,
    "attack_max": 4,
    "defence_min": 1,
    "defence_max": 2,
    "health_min": 4,
    "health_max": 6,
    "accuracy_min": 4,
    "accuracy_max": 8,
    "evasion_min": 0,
    "evasion_max": 3}
stats_juggernaut = {
    "attack_min": 2,
    "attack_max": 6,
    "defence_min": 2,
    "defence_max": 3,
    "health_min": 4,
    "health_max": 8,
    "accuracy_min": 2,
    "accuracy_max": 5,
    "evasion_min": 0,
    "evasion_max": 2}
stats_ninja = {
    "attack_min": 3,
    "attack_max": 6,
    "defence_min": 0,
    "defence_max": 2,
    "health_min": 2,
    "health_max": 5,
    "accuracy_min": 8,
    "accuracy_max": 12,
    "evasion_min": 2,
    "evasion_max": 3}
stats_mage = {
    "attack_min": 1,
    "attack_max": 2,
    "defence_min": 1,
    "defence_max": 2,
    "health_min": 2,
    "health_max": 4,
    "accuracy_min": 6,
    "accuracy_max": 8,
    "evasion_min": 2,
    "evasion_max": 4}

# EXP table
exp_table = [None, 6, 10, 16, 22, 30, 42, 54, 70, 86, 100, 120, 140, 160, 180, 200, 220, 240, 270, 300, 10000]

# Damage variable (per level)
DaV = [ [None, None],
        [-1, 1], [-1, 1], [-1, 2], [-2, 2], [-2, 2], [-2, 3], [-3, 3], [-3, 3], [-3, 4], [-3, 4],
        [-3, 4], [-3, 4], [-3, 4], [-4, 5], [-4, 5], [-4, 5], [-4, 5], [-4, 6], [-4, 6], [-4, 7] ]

# Defence variable (per level)
DeV = [ [None, None],
        [0, 1], [0, 1], [0, 2], [0, 2], [0, 2], [0, 2], [0, 2], [0, 2], [1, 2], [1, 2],
        [1, 2], [1, 2], [1, 2], [1, 3], [1, 3], [1, 3], [1, 4], [2, 4], [2, 4], [3, 5] ]



#   MONSTERS ----------------------------------------
list_of_enemies = ["goblin", "bandit", "bandit chief", "exiled warrior", "zombie", "undead knight", "elf assassin", "mad juggernaut", "lesser demon", "dragon"]

# Stat tables
stats_goblin = {
    "name": "goblin",
    "attack": 2,
    "defence": 0,
    "health": 5,
    "exp": 2}
stats_bandit = {
    "name": "bandit",
    "attack": 2,
    "defence": 2,
    "health": 12,
    "exp": 4}
stats_bandit_chief = {
    "name": "bandit chief",
    "attack": 2,
    "defence": 4,
    "health": 18,
    "exp": 6}
stats_exiled_warrior = {
    "name": "exiled warrior",
    "attack": 4,
    "defence": 4,
    "health": 24,
    "exp": 10}
stats_zombie = {
    "name": "zombie",
    "attack": 3,
    "defence": 0,
    "health": 38,
    "exp": 10}
stats_undead_knight = {
    "name": "undead knight",
    "attack": 4,
    "defence": 8,
    "health": 22,
    "exp": 18}
stats_elf_assassin = {
    "name": "elf assassin",
    "attack": 8,
    "defence": 2,
    "health": 12,
    "exp": 18}
stats_mad_juggernaut = {
    "name": "mad juggernaut",
    "attack": 6,
    "defence": 6,
    "health": 62,
    "exp": 24}
stats_lesser_demon = {
    "name": "lesser demon",
    "attack": 12,
    "defence": 6,
    "health": 58,
    "exp": 32}
stats_dragon = {
    "name": "dragon",
    "attack": 22,
    "defence": 18,
    "health": 202,
    "exp": 0}

# Encounter Probabilities
no = 200
EP = [
    [ [no, no], [no, no], [no, no], [no, no], [no, no], [no, no], [no, no], [no, no], [no, no], [no, no] ],
    [ [0, 100], [no, no], [no, no], [no, no], [no, no], [no, no], [no, no], [no, no], [no, no], [no, no] ],
    [ [0, 80], [80, 100], [no, no], [no, no], [no, no], [no, no], [no, no], [no, no], [no, no], [no, no] ],
    [ [0, 40], [40, 100], [no, no], [no, no], [no, no], [no, no], [no, no], [no, no], [no, no], [no, no] ],
    [ [0, 20], [20, 80], [80, 100], [no, no], [no, no], [no, no], [no, no], [no, no], [no, no], [no, no] ],
    [ [0, 10], [10, 50], [50, 100], [no, no], [no, no], [no, no], [no, no], [no, no], [no, no], [no, no] ],
    [ [0, 5], [5, 20], [20, 80], [80, 100], [no, no], [no, no], [no, no], [no, no], [no, no], [no, no] ],
    [ [no, no], [0, 15], [15, 60], [60, 100], [no, no], [no, no], [no, no], [no, no], [no, no], [no, no] ],
    [ [no, no], [0, 5], [5, 30], [30, 80], [80, 100], [no, no], [no, no], [no, no], [no, no], [no, no] ],
    [ [no, no], [no, no], [0, 15], [15, 60], [60, 100], [no, no], [no, no], [no, no], [no, no], [no, no] ],
    [ [no, no], [no, no], [0, 5], [5, 30], [30, 80], [80, 100], [no, no], [no, no], [no, no], [no, no] ],
    [ [no, no], [no, no], [no, no], [0, 15], [15, 60], [60, 100], [no, no], [no, no], [no, no], [no, no] ],
    [ [no, no], [no, no], [no, no], [0, 5], [5, 30], [30, 70], [70, 95], [95, 100], [no, no], [no, no] ],
    [ [no, no], [no, no], [no, no], [no, no], [0, 15], [15, 60], [60, 80], [80, 100], [no, no], [no, no] ],
    [ [no, no], [no, no], [no, no], [no, no], [0, 5], [5, 30], [30, 70], [70, 95], [95, 100], [no, no] ],
    [ [no, no], [no, no], [no, no], [no, no], [no, no], [0, 15], [15, 60], [60, 80], [80, 100], [no, no] ],
    [ [no, no], [no, no], [no, no], [no, no], [no, no], [0, 5], [5, 30], [30, 70], [70, 100], [no, no] ],
    [ [no, no], [no, no], [no, no], [no, no], [no, no], [no, no], [0, 15], [15, 60], [60, 100], [no, no] ],
    [ [no, no], [no, no], [no, no], [no, no], [no, no], [no, no], [0, 5], [5, 40], [40, 99], [99, 100] ],
    [ [no, no], [no, no], [no, no], [no, no], [no, no], [no, no], [no, no], [0, 40], [40, 80], [80, 100] ],
    [ [no, no], [no, no], [no, no], [no, no], [no, no], [no, no], [no, no], [no, no], [no, no], [0, 100] ]
]

# Descriptions
descr_goblin = "It's a small, green very weak looking creature. It's only remarkable in its bad looks.\n"
descr_bandit = "Just a grunt with a butter knife who likes to steal candy from babies.\n"
descr_bandit_chief = "He has an enormous belly (probably full of stolen candy) and a needlessly large butter knife.\n"
descr_exiled_warrior = "An ex-soldier who did not obey his superior's orders and thus got exiled.\n"
descr_zombie = "This mass of human remains is slow but sturdy. Also smells pretty bad.\n"
descr_undead_knight = "A knight who painted his armor black so he could look cooler.\n"
descr_elf_assassin = "You haven't heard of any elf assassing in your life. That probably means they're doing their job perfectly.\n"
descr_mad_juggernaut = "This guy is big. You don't want to get on his bad side.\n"
descr_lesser_demon = "A hellish abomination looking like a mix of some random animals. Better slay it before it disturbs more people.\n"
descr_dragon = "Holy s**t it's a ***** ****** ******* **** ******* dragon! Run!\n"

# Escape probability
EsP = [ [0, 90], [0, 80], [0, 70], [0, 50], [0, 70], [0, 50], [0, 10], [0, 30], [0, 20], [0, 0] ]






