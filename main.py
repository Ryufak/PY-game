import controller
import events

while True:
    menu_callback = controller.start()
    if menu_callback == "load":
        data_list = controller.corrupted_data_check()
    elif menu_callback == "new":
        data_list = events.character_creation()

    events.game(data_list, menu_callback)

