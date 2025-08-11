import os

def clear_screen():
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
    except:
        pass
