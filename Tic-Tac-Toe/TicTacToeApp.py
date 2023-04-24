import tkinter as tk
from tkinter import messagebox
import ia  # Importer l'IA du fichier ia.py

window = tk.Tk()
window.iconbitmap('tic tac toe.ico')
window.title("Tic Tac Toe")

def check_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != "":
            messagebox.showinfo("Fin de la partie", "Le joueur {} a gagné !".format(board[i][0]))
            return board[i][0]

    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != "":
            return board[0][i]

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != "":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != "":
        return board[0][2]

    return None

def check_draw(board):
    for row in board:
        for cell in row:
            if cell == "":
                return False
    return True

def cell_click(row, col):
    global player_turn, game_over, board

    if board[row][col] == "" and not game_over:
        if player_turn == "X":
            buttons[row][col].config(text="X", state="disabled")
            board[row][col] = "X"
            player_turn = "O"
        else:
            buttons[row][col].config(text="O", state="disabled")
            board[row][col] = "O"
            player_turn = "X"

        winner = check_winner(board)
        if winner:
            messagebox.showinfo("Fin de la partie", "Le joueur {} a gagné !".format(winner))
            game_over = True
        elif check_draw(board):
            messagebox.showinfo("Fin de la partie", "Match nul.")
            game_over = True

        if not game_over and player_turn == "O":
            # Si ce n'est pas la fin de la partie et c'est le tour de l'IA
            # Laisser l'IA jouer
            move = ia.make_move(board)
            if move:
                row, col = move
                cell_click(row, col)  # Appeler récursivement la fonction cell_click pour jouer le coup de l'IA

def reset_game():
    global player_turn, game_over, board

    player_turn = "X"
    game_over = False
    board = [["" for _ in range(3)] for _ in range(3)]

    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text="", state="normal")

buttons = [[None for _ in range(3)] for _ in range(3)]
for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(window, text="", width=10, height=3,
                               font=("Helvetica", 24), relief='ridge', background='#cc66ff',
                               command=lambda row=i, col=j: cell_click(row, col))
        buttons[i][j].grid(row=i, column=j)

reset_button = tk.Button(window, text="Rejouer", width=20, height=2, relief='ridge', background='#dd99ff',
                        font=("Helvetica", 14), command=reset_game)
reset_button.grid(row=3, column=0, columnspan=3)

player_turn = "X"
game_over = False
board = [["" for _ in range(3)] for _ in range(3)]

def play_tic_tac_toe():
    global window
    window.mainloop()

play_tic_tac_toe()