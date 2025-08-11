import random

move_list = ["papel", "pedra", "tesoura"]

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

def select_winner(p_move, c_move):
    if p_move == 'papel':
        if c_move == "pedra":
            return "p"
        elif c_move == "tesoura":
            return "c"
        else:
            return "d"
    elif p_move == 'pedra':
        if c_move == "tesoura":
            return "p"
        elif c_move == "papel":
            return "c"
        else:
            return "d"
    elif p_move == 'tesoura':
        if c_move == "papel":
            return "p"
        elif c_move == "pedra":
            return "c"
        else:
            return "d"
