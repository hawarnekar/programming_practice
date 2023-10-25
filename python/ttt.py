import random as r

global positions_filled
positions_filled = 0

empty_pos = ["a1", "b1", "c1", "a2", "b2", "c2", "a3", "b3", "c3"]
game_pos = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

#               0123456789012
layout =      ["   a   b   c \n",       # 0th row
          list("1    |   |   "),        # 1st row
          list("  ---+---+---"),        # 2nd row
          list("2    |   |   "),        # 3rd row
          list("  ---+---+---"),        # 4th row
          list("3    |   |   "),        # 5th row
          "\n\n"]

conv_row = {"1": 0, "2": 1, "3": 2}
conv_col = {"a": 0, "b": 1, "c": 2}

def print_game_pos():
    print("".join(layout[0]))
    for i in range(3):
        line = layout[2*i+1]
        line[3]  = game_pos[i][0]
        line[7]  = game_pos[i][1]
        line[11] = game_pos[i][2]
        print("".join(line))
        if(i < 2):
            print("".join(layout[2]))
    print("")

def win_check():
    if( (game_pos[0][0] == game_pos[0][1] and game_pos[0][1] == game_pos[0][2] and game_pos[0][0] != ' ') or
        (game_pos[1][0] == game_pos[1][1] and game_pos[1][1] == game_pos[1][2] and game_pos[1][0] != ' ') or
        (game_pos[2][0] == game_pos[2][1] and game_pos[2][1] == game_pos[2][2] and game_pos[2][0] != ' ') or
        (game_pos[0][0] == game_pos[1][0] and game_pos[1][0] == game_pos[2][0] and game_pos[0][0] != ' ') or
        (game_pos[0][1] == game_pos[1][1] and game_pos[1][1] == game_pos[2][1] and game_pos[0][1] != ' ') or
        (game_pos[0][2] == game_pos[1][2] and game_pos[1][2] == game_pos[2][2] and game_pos[0][2] != ' ') or
        (game_pos[0][0] == game_pos[1][1] and game_pos[1][1] == game_pos[2][2] and game_pos[0][0] != ' ') or
        (game_pos[2][0] == game_pos[1][1] and game_pos[1][1] == game_pos[0][2] and game_pos[2][0] != ' ')
    ):
        return True

    return False

def user_play(inp):
    global positions_filled

    if inp[0] not in conv_col or inp[1] not in conv_row or len(inp) != 2:
        print("Invalid input. Please try again.")
        return False

    col = conv_col[inp[0]]
    row = conv_row[inp[1]]
    if game_pos[row][col] != " ":
        print("Position already filled. Please try again.")
        return False

    game_pos[row][col] = 'o'
    positions_filled += 1
    empty_pos.remove(inp)

    return True

def computer_play(pos):
    global positions_filled

    c_pos = empty_pos[r.randrange(0, len(empty_pos))]
    row = conv_row[c_pos[1]]
    col = conv_col[c_pos[0]]
    game_pos[row][col] = 'x'
    positions_filled += 1
    empty_pos.remove(c_pos)

print_game_pos()

print("You are playing against the computer. The computer plays\nrandom postions and does not play to win (yet).")
v = input("Enter position (ex. a2): ")
while True:
    valid = user_play(v)
    if not valid:
        v = input("Enter position (ex. a2): ")
        continue

    print_game_pos()
    if win_check():
        print("You win!")
        break

    if positions_filled > 8:
        print("Game ended without result.")
        break

    computer_play(v)
    if win_check():
        print("Computer wins.")
        break

    print_game_pos()
    if positions_filled > 8:
        print("Game ended without result.")
        break

    print("You are playing against the computer. The computer plays\nrandom postions and does not play to win (yet).")
    v = input("Enter position (ex. a2): ")

