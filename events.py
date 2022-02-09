import controller
import dialog
import random
import classes


def character_creation():
    print(dialog.message_welcome)
    name = input(dialog.choose_name)

    print(dialog.choose_class)
    controller.cycle_wait(1)
    print(dialog.choose_class_instructions)
    controller.cycle_wait(2)
    while True:
        command = str(input(dialog.choose_class_input)).lower()
        if command == "warrior" or command == "w":
            p_class = "warrior"
            break
        elif command == "juggernaut" or command == "j":
            p_class = "juggernaut"
            break
        elif command == "ninja" or command == "n":
            p_class = "ninja"
            break
        elif command == "mage" or command == "m":
            p_class = "mage"
            break
        elif command == "help" or command == "h":
            print(dialog.choose_class_help)
            controller.cycle_wait(2)
        else:
            print(dialog.invalid_command)
            controller.cycle_wait(1)
    print(dialog.choose_class_done + p_class)
    controller.cycle_wait(1)

    print(dialog.roll_stats)
    health = random.randint(16, 22)
    current_health = health
    attack = random.randint(2, 4)
    defence = random.randint(1, 2)
    accuracy = random.randint(22, 32)
    evasion = random.randint(6, 8)
    level = 1
    exp = 0
    m_name = "goblin"
    m_current_health = 6

    data_list = [name, p_class, health, current_health, attack, defence, accuracy, evasion, level, exp, m_name, m_current_health]

    controller.save_game(*data_list)
    print(dialog.character_created)
    controller.cycle_wait(1)

    return data_list

def game(data_list, menu_callback):
    data_player = controller.slice_save_data(data_list, 0)
    data_enemy = controller.slice_save_data(data_list, 1)
    enemy_loaded = None
    player = classes.Player(*data_player)
    if menu_callback == "load":
            enemy = classes.Enemy(data_enemy[0])
            enemy.summon(data_enemy[1])
            enemy_loaded = True

    print(dialog.runtrough)
    controller.cycle_wait(1)
    print(dialog.commands_description)
    controller.cycle_wait(2)

    
    while True:
        #generating or loading enemy
        if enemy_loaded == True:
            enemy_loaded = False
        else:
            enemy_name = classes.enemy_generator(player.level)
            enemy = classes.Enemy(enemy_name)
            enemy.summon(0)

        print(f"\nYou encountered a vicious {enemy.name}")

        while True:
            while True:
                action = str(input(dialog.choose_command)).lower()
                if action == "save" or action == "save game":
                    controller.save_game(player.name, player.p_class, player.health, player.current_health, player.attack, player.defence, player.accuracy, player.evasion, player.level, player.exp, enemy.name, enemy.current_health)
                    print(dialog.save_successful)
                elif action == "menu":
                    return
                elif action == "exit" or action == "quit":
                    command = str(input(dialog.quit_game_confirmation)).lower()
                    if command == "y" or command == "ye" or command == "yes":
                        quit()
                    elif command == "no" or command == "nah" or command == "n":
                        controller.cycle_wait(1)
                    else:
                        print(dialog.invalid_command)
                        controller.cycle_wait(1)
                elif action == "attack" or action == "fight":
                    enemy.health = player.fight(enemy.defence, enemy.current_health)
                    break
                elif action == "defend":
                    player.defend()
                    break
                elif action == "run":
                    player.run(enemy.name)
                    controller.cycle_wait(.5)
                    break
                elif action == "status":
                    player.info()
                elif action == "e status" or action == "enemy status":
                    enemy.info()
                elif action == "commands" or action == "help":
                    print(dialog.commands_description)
                    controller.cycle_wait(1)

                #Some commands for testing
                elif action == "admin levelup":
                    player.level_up()
                elif action == "admin set attack":
                    val = int(input(dialog.input_value))
                    player.attack = val
                    print(f"{dialog.val_attack} {player.attack}")
                elif action == "admin set defence":
                    val = int(input(dialog.input_value))
                    player.defence = val
                    print(f"{dialog.val_defence} {player.defence}")
                elif action == "admin set health":
                    val = int(input(dialog.input_value))
                    player.health = val
                    print(f"{dialog.val_health} {player.health}")
                elif action == "admin fullheal":
                    player.current_health = player.health
                    print(dialog.fully_healed)
                elif action == "admin set accuracy":
                    val = int(input(dialog.input_value))
                    player.accuracy = val
                    print(f"{dialog.val_accuracy} {player.accuracy}%")
                elif action == "admin set evasion":
                    val = int(input(dialog.input_value))
                    player.evasion = val
                    print(f"{dialog.val_evasion} {player.evasion}%")
                elif action == "admin kill enemy":
                    enemy.current_health = 0
                    print(dialog.enemy_ded)
                    break
                else:
                    print(dialog.invalid_command)
                    controller.cycle_wait(1)
                
            if enemy.name == "dragon" and enemy.health <= 0:
                print(dialog.dragon_killed)
                controller.cycle_wait(2)
                print(dialog.dragon_question)
                controller.cycle_wait(1)
                print(dialog.thanks)
                controller.cycle_wait(4)
                return
            
            if action == "run": break   

            if enemy.health <= 0 or enemy.current_health <= 0:
                player.exp_listener(enemy.exp)
                if player.level_up_signal is True: player.level_up()
                #autosave
                print(dialog.enemy_killed + enemy.name)
                controller.save_game(player.name, player.p_class, player.health, player.current_health, player.attack, player.defence, player.accuracy, player.evasion, player.level, player.exp, enemy.name, enemy.current_health)
                break
            else:
                player.current_health = enemy.fight(player.evasion, player.current_health, player.level, player.defence, player.temp_def)
                if player.current_health <= 0:
                    print(dialog.you_died + enemy.name)
                    controller.cycle_wait(2)
                    return
                else:
                    pass
                    #autosave
                    #controller.save_game(player.name, player.p_class, player.health, player.current_health, player.attack, player.defence, player.accuracy, player.evasion, player.level, player.exp, enemy.name, enemy.current_health)

                
                

        


