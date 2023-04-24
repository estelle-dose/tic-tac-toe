import random

def make_move(board):
    # Cette fonction génère un mouvement aléatoire pour l'IA
    # Elle prend en entrée le plateau de jeu sous forme d'une liste de listes

    available_moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == "":
                available_moves.append((i, j))

    if available_moves:
        # S'il y a encore des mouvements disponibles
        # L'IA choisit un mouvement aléatoire parmi les mouvements disponibles
        move = random.choice(available_moves)
        return move
    else:
        return None