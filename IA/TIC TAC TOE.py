# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 09:48:21 2020

@author: Matthis Villeneuve
"""
from math import inf as infinity
from random import choice
import platform
import time
from os import system

joueur = -1
ordi = +1
board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
]


def evaluate(state):
    """
    renvoi: +1 si le pc gagne; -1 si le joueur gagne; 0 en cas d'égalité
    """
    if wins(state, ordi):
        score = +1
    elif wins(state, joueur):
        score = -1
    else:
        score = 0

    return score


def wins(state, player):
    """
    Test si un joueur gagne Possibilitées:
    * Trois Lignes[X X X] ou [O O O]
    * Trois cols    [X X X] ou [O O O]
    * Deux diagonales [X X X] ou [O O O]
    :param state: L'état du jeu
    :param player: Le joueur, ou l'ordi
    :return: True si le player gagne
    """
    win_state = [
        [state[0][0], state[0][1], state[0][2]],
        [state[1][0], state[1][1], state[1][2]],
        [state[2][0], state[2][1], state[2][2]],
        [state[0][0], state[1][0], state[2][0]],
        [state[0][1], state[1][1], state[2][1]],
        [state[0][2], state[1][2], state[2][2]],
        [state[0][0], state[1][1], state[2][2]],
        [state[2][0], state[1][1], state[0][2]],
    ]
    if [player, player, player] in win_state:
        return True
    else:
        return False


def game_over(state):
    """
    Test si un participant gagne
    """
    return wins(state, joueur) or wins(state, ordi)

def empty_cells(state):
    """
    Retourne une liste de cellule vide (uniquement composé des cellules non jouées)
    """
    cells = []

    for x, row in enumerate(state):
        for y, cell in enumerate(row):
            if cell == 0:
                cells.append([x, y])

    return cells



def valid_move(x, y):
    """
    Un mouvement est valide si la cellule est vide
    """
    if [x, y] in empty_cells(board):
        return True
    else:
        return False


def set_move(x, y, player):
    """
    Permet de prendre en compte un mouvement, s'il est valide
    """
    if valid_move(x, y):
        board[x][y] = player
        return True
    else:
        return False


def minimax(state, depth, player):
    if player == ordi:
        maxi = [-1, -1, -infinity]
    else:
        maxi = [-1, -1, +infinity]

    if depth == 0 or game_over(state):
        score = evaluate(state)
        return [-1, -1, score]

    for cell in empty_cells(state):
        x, y = cell[0], cell[1]
        state[x][y] = player
        score = minimax(state, depth - 1, -player)
        state[x][y] = 0
        score[0], score[1] = x, y

        if player == ordi:
            if score[2] > maxi[2]:
                maxi = score  # max value
        else:
            if score[2] < maxi[2]:
                maxi = score  # min value

    return maxi



def clean():
    """
    Clears the console
    """
    os_name = platform.system().lower()
    if 'windows' in os_name:
        system('cls')
    else:
        system('clear')


def afficher(state, c_choice, h_choice):

    chars = {
        -1: h_choice,
        +1: c_choice,
        0: ' '
    }
    str_line = '---------------'

    print('\n' + str_line)
    for row in state:
        for cell in row:
            symbol = chars[cell]
            print(f'| {symbol} |', end='')
        print('\n' + str_line)


def ai_turn(c_choice, h_choice):
    """
    Si toutes les cellules sont vides, joue au hasard
    """
    depth = len(empty_cells(board))
    if depth == 0 or game_over(board):
        return

    clean()
    print(f'Tour de l ordinateur [{c_choice}]')
    afficher(board, c_choice, h_choice)

    if depth == 9:
        x = choice([0, 1, 2])
        y = choice([0, 1, 2])
    else:
        move = minimax(board, depth, ordi)
        x, y = move[0], move[1]

    set_move(x, y, ordi)
    time.sleep(1)


def human_turn(c_choice, h_choice):
    """
    :param c_choice: X ou O pour l'ordi
    :param h_choice: Idem pour le joueur
    """
    depth = len(empty_cells(board))
    if depth == 0 or game_over(board):
        return

    # Dictionary of valid moves
    move = -1
    moves = {
        7: [0, 0], 8: [0, 1], 9: [0, 2],
        4: [1, 0], 5: [1, 1], 6: [1, 2],
        1: [2, 0], 2: [2, 1], 3: [2, 2],
    }

    clean()
    print(f'A vous [{h_choice}]')
    afficher(board, c_choice, h_choice)

    while move < 1 or move > 9:
        try:
            move = int(input('Utilisez votre pavé numérique '))
            coord = moves[move]
            can_move = set_move(coord[0], coord[1], joueur)

            if not can_move:
                print('Mouvement invalide')
                move = -1
        
        except (KeyError, ValueError):
            print('Invalide')


def main():
    """
    Fonction principale du jeu
    """
    clean()
    h_choice = ''  # X ou O
    c_choice = ''  # X ou O
    first = ''  # Si le joueur commence

    # Choix du joueur
    while h_choice != 'O' and h_choice != 'X':
        try:
            print('')
            h_choice = input('Choisissez X ou O\nChoisi : ').upper()
        
        except (KeyError, ValueError):
            print('Mauvais choix, réessayez')

    # Choix de l'ordinateur
    if h_choice == 'X':
        c_choice = 'O'
    else:
        c_choice = 'X'

    
    clean()
    while first != 'O' and first != 'N':
        try:
            first = input('Souhaitez vous débuter? UNIQUEMENT O ou N ').upper()
        
        except (KeyError, ValueError):
            print('Mauvaise entrée...')

    # Déroulement du jeu
    while len(empty_cells(board)) > 0 and not game_over(board):
        if first == 'N':
            ai_turn(c_choice, h_choice)
            first = ''

        human_turn(c_choice, h_choice)
        ai_turn(c_choice, h_choice)

    # Game over message
    if wins(board, joueur):
        clean()
        print(f'Tour du joueur [{h_choice}]')
        afficher(board, c_choice, h_choice)
        print('Victoire!')
    elif wins(board, ordi):
        clean()
        print(f'Tour de l ordinateur [{c_choice}]')
        afficher(board, c_choice, h_choice)
        print('Défaite...')
    else:
        clean()
        afficher(board, c_choice, h_choice)
        print('égalité!')




if __name__ == '__main__':
    main()
