from board import mark_dict, game_board, placeholder_game_board, winning_combos


print("\n     TIC-TAC-TOE\n")
print(placeholder_game_board)
taken_positions = []


def choose_mark(player_mark):
    chosen_spot = input(f"\nWhere do you want to place your '{player_mark}'\n").lower()
    while chosen_spot not in mark_dict or chosen_spot in taken_positions:
        print("Position already taken or not valid")
        chosen_spot = input(f"\nWhere do you want to place your `{player_mark}`\n").lower()
    mark_dict[chosen_spot] = player_mark
    taken_positions.append(chosen_spot)
    print(game_board.format(a1=mark_dict["a1"],
                            a2=mark_dict["a2"],
                            a3=mark_dict["a3"],
                            b1=mark_dict["b1"],
                            b2=mark_dict["b2"],
                            b3=mark_dict["b3"],
                            c1=mark_dict["c1"],
                            c2=mark_dict["c2"],
                            c3=mark_dict["c3"]))


def check_winner():
    for combo in winning_combos:
        if (mark_dict[combo[0]] == mark_dict[combo[1]]
                and mark_dict[combo[0]] == mark_dict[combo[2]]
                and mark_dict[combo[1]] == mark_dict[combo[2]])\
                and mark_dict[combo[0]] != " ":
            return True


def game_loop():
    while True:
        choose_mark("X")
        x_win = check_winner()
        if x_win is True:
            return "X"
        elif " " not in list(mark_dict.values()):
            return "draw"
        choose_mark("O")
        o_win = check_winner()
        if o_win is True:
            return "O"


winner = game_loop()
if winner == "draw":
    print("\nThe game is a draw!")
else:
    print(f"\nThe '{winner}' player wins!")
