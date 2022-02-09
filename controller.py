import dialog
import data

import os
import time

#Input the name of the save file
savefile = "savefile.py"

savefile_exist = os.path.isfile(savefile)
if savefile_exist is True:
    savefile_empty = os.stat(savefile).st_size == 0
else:
    savefile_empty = True



def start():
    while True:
        command = str(input(dialog.main_menu)).lower()
        if command == "new" or command == "n":
            if new_game() == True:
                return "new"
        elif command == "load" or command == "l":
            v = load_game()
            if v == "new" or v == "load":
                return v
            else:
                cycle_wait(.5)
        else:
            print(dialog.invalid_command)
            cycle_wait(1)

def new_game():
    if savefile_exist == False:
        clear_savefile()
        return True
    else:
        if savefile_empty == True:
            return True
        else:
            print(dialog.new_game_warning)
            cycle_wait(1)
            command = str(input(dialog.new_game_confirmation)).lower()
            if command == "yes" or command == "ye" or command == "y":
                clear_savefile()
                return True
            elif command == "no" or command == "nah" or command == "n":
                pass
            else:
                print(dialog.invalid_command)
                cycle_wait(1)

def load_game():
    if savefile_exist == False:
        return load_to_new()
    else:
        if savefile_empty == True:
            return load_to_new()
        else:
            return "load"

def load_to_new():
    while True:
        print(dialog.load_no_data)
        cycle_wait(1)
        command = str(input(dialog.load_start_new)).lower()
        if command == "yes" or command == "ye" or command == "y":
            clear_savefile()
            return "new"
        elif command == "no" or command == "nah" or command == "n":
            break
        else:
            print(dialog.invalid_command)
            cycle_wait(1)

def corrupted_data_check():
    try:
        import savefile

        p_class = savefile.p_class
        l1 = data.list_of_classes
        m_name = savefile.m_name
        l2 = data.list_of_enemies

        if p_class != l1[0] and p_class != l1[1] and p_class != l1[2] and p_class != l1[3]:
            terminate()
        if m_name != l2[0] and m_name != l2[1] and m_name != l2[2] and m_name != l2[3] and m_name != l2[4] and m_name != l2[5] and m_name != l2[6] and m_name != l2[7] and m_name != l2[8] and m_name != l2[9]:
            terminate()

        data_list = [str(savefile.p_name), p_class, int(savefile.p_health), int(savefile.p_current_health), int(savefile.p_attack), int(savefile.p_defence), int(savefile.p_accuracy), int(savefile.p_evasion), int(savefile.p_level), int(savefile.p_exp), str(savefile.m_name), int(savefile.m_current_health)]  
    except AttributeError: terminate()
    except ValueError: terminate()
    except SyntaxError: terminate()
    return data_list

def terminate():
    print(dialog.corrupted_data)
    quit()

def save_game(name, p_class, health, current_health, attack, defence, accuracy, evasion, level, exp, m_name, m_health):
    name_list = ["p_name", "p_class", "p_health", "p_current_health", "p_attack", "p_defence", "p_accuracy", "p_evasion", "p_level", "p_exp", "m_name", "m_current_health"]
    data_list = [name, p_class, health, current_health, attack, defence, accuracy, evasion, level, exp, m_name, m_health]
    f = open(f"{savefile}", "w")
    i = 0
    string = ""
    for itterations in data_list:
        if i == 0 or i == 1 or i == 10:
            string = string + str(name_list[i]) + " = " + f"'{str(data_list[i])}'\n"
        else:
            string = string + str(name_list[i]) + " = " + str(data_list[i]) + "\n"
        i += 1

    f.write(string)
    f.close()

def autosave():
    save_game()
    cycle_wait(300)
    autosave()

def clear_savefile():
    f = open(f"{savefile}", "w")
    f.write("")
    f.close()

def cycle_wait(wait_time):
    time.sleep(wait_time)

#'list' is the savefile list you want sliced
#'type' is the type of list you want returned (0 is for player data and 1 is for enemy data)
def slice_save_data(list, type):
    list_p = list[:10]
    list_e = [list[-2], list[-1]]
    if type == 0:   return list_p
    elif type == 1: return list_e



