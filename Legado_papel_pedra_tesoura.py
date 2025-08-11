import random 
import os

move_list  = ["papel","pedra", "tesoura"]
player_count = 0
computer_count = 0

def clear_screen():
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
    except:
        pass

print("========================================")
print("Bem vindo ao jogo Pedra, Papel e Tesoura")

def main_print():
    print("========================================")
    print("\nPlacar:")
    print("Você: {}".format(player_count))
    print("Computador: {}".format(computer_count))
    print("\n")
    print("Escolha seu lance:")
    print("0 - Papel | 1 - Pedra | 2 - Tesoura")

def select_move():
    return random.choice(move_list)

def get_player_move():
    while True:
        try:
            player_move = int(input())
            if player_move not in [0, 1, 2]:
                raise ValueError("Escolha inválida. Digite 0, 1 ou 2.")
            return move_list[player_move]
        except Exception as e:
            print(e)

def select_winnner(p_move, c_move):
    global player_count, computer_count 

    if p_move == 'papel':
        if c_move == "pedra":
             player_count += 1
             return "p"
        elif c_move == "tesoura":
             computer_count += 1
             return "c"
        else:
             return "d"
         
    if p_move == 'pedra':
        if c_move == "tesoura":
             player_count += 1
             return "p"
        elif c_move == "papel":
             computer_count += 1
             return "c"
        else:
             return "d"
         
    if p_move == 'tesoura':
        if c_move == "papel":
             player_count += 1
             return "p"
        elif c_move == "pedra":
             computer_count += 1
             return "c"
        else:
             return "d"
         
again = 1
while again == 1:
    main_print()
    player_move = get_player_move()
    computer_move = select_move()
    winner = select_winnner(player_move, computer_move)

    print("")
    print("========================================")
    print("Sua jogada: {}".format(player_move.upper()))
    print("Jogada do computador: {}".format(computer_move.upper()))

    if winner == "p":
        print("Você venceu!")
    elif winner == "c":
        print("Você perdeu!")
    else:
        print("Empate!")
    print("========================================")

    while True:
        print("Jogar novamente? 0 - SIM | 1 - NÃO")
        next = int(input())
        if next == 0:
            break
        elif next == 1:
            again = 0
            break
    #os.system("cls")
    clear_screen()
