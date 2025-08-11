from engine import select_move, get_player_move, select_winner
from scoreboard import main_print, update_score, reset_score, get_score
from utils import clear_screen

def main():
    print("========================================")
    print("Bem vindo ao jogo Pedra, Papel e Tesoura")

    again = True
    reset_score()

    while again:
        main_print()
        player_move = get_player_move()
        computer_move = select_move()
        winner = select_winner(player_move, computer_move)
        update_score(winner)

        print("\n========================================")
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
            try:
                print("Jogar novamente? 0 - SIM | 1 - NÃO")
                choice = int(input())
                if choice == 0:
                    break
                elif choice == 1:
                    again = False
                    break
                else:
                    print("Digite 0 ou 1.")
            except ValueError:
                print("Entrada inválida.")
        
        clear_screen()

if __name__ == "__main__":
    main()
