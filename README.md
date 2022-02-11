# PY-game

There is a Virtual Environment (venv) included in the source files.
The (venv) contains all dependencies needed.

1. Download the project and unzip it
2. Unzip "venv.rar" in the project directory (you can delete the .rar file afterwards)
3. Open the Command Prompt and use 'cd' to go to the directory of the project
    (The path should look something like this:  C:\Users\username\Downloads\PY-game)
4. Activate the (venv) using:   venv\scripts\activate.bat
    (Now the path should look something like this:  (venv) C:\Users\username\Downloads\PY-game)
5. Use pyinstaller to bundle the scripts into an executable:    pyinstaller --onefile main.py
6. In the newly created "dist" folder you will have an executable file that you can test




* If the dependencies are not working correctly you could run this:     pip install -r requirements.txt







# Console commands
These are some commands to help with testing certain functions
[admin levelup]         Calls the level_up function
[admin set attack]      Sets attack to input int value
[admin set defence]     Sets defence to input int value
[admin set health]      Sets max health to input int value (does not heal)
[admin fullheal]        Heals you to current max health
[admin set accuracy]    Sets accuracy to input int value
[admin set evasion]     Sets evasion to input int value
[admin kill enemy]      Sets enemy health to 0