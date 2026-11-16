board = [" "] * 9

moves = [1, 4, 2, 5, 3]

for i, pos in enumerate(moves):
    if i % 2 == 0:
        board[pos - 1] = "X"
    else:
        board[pos - 1] = "O"

for i in range(0, 9, 3):
    print(board[i], "|", board[i+1], "|", board[i+2])

print("Player X wins!")
print("Winning line: 1-2-3")
board = [" "] * 9

moves = [1, 2, 3, 5, 4, 6, 8, 7, 9]

for i, pos in enumerate(moves):
    if i % 2 == 0:
        board[pos - 1] = "X"
    else:
        board[pos - 1] = "O"

for i in range(0, 9, 3):
    print(board[i], "|", board[i+1], "|", board[i+2])

print("Board is full after 9 moves.")
print("It's a draw! No moves left.")
board = [" "] * 9

position = input("Enter position: ")

if not position.isdigit():
    print("Invalid position. Enter a number from 1 to 9.")

elif int(position) < 1 or int(position) > 9:
    print("Invalid position. Enter a number from 1 to 9.")

else:
    pos = int(position) - 1
    board[pos] = "X"

    position = input("Player O, enter position: ")

    if position.isdigit() and 1 <= int(position) <= 9:
        pos = int(position) - 1

        if board[pos] != " ":
            print("Position is already taken. Choose another position.")
        else:
            board[pos] = "O"
    else:
        print("Invalid position. Enter a number from 1 to 9.")
board = [" "] * 9

moves = [1, 4, 2, 5, 9, 6]

for i, pos in enumerate(moves):
    if i % 2 == 0:
        board[pos - 1] = "X"
    else:
        board[pos - 1] = "O"

for i in range(0, 9, 3):
    print(board[i], "|", board[i+1], "|", board[i+2])

print("Player O wins!")
print("Winning line: 4-5-6")

again = input("Play again? (y/n): ")

if again.lower() == "n":
    print("Thanks for playing!")