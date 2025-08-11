# Variáveis globais de pontuação
player_count = 0
computer_count = 0

def reset_score():
    global player_count, computer_count
    player_count = 0
    computer_count = 0

def update_score(winner):
    global player_count, computer_count
    if winner == "p":
        player_count += 1
    elif winner == "c":
        computer_count += 1

def get_score():
    return player_count, computer_count

def main_print():
    p, c = get_score()
    print("========================================")
    print("\nPlacar:")
    print(f"Você: {p}")
    print(f"Computador: {c}")
    print("\n")
    print("Escolha seu lance:")
    print("0 - Papel | 1 - Pedra | 2 - Tesoura")
