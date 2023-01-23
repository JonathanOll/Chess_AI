from random import choice
from random import uniform
from time import time
from options import *
from neural_network import NeuralNetwork

class Random_Bot:
    def __init__(self, color):
        self.color = color
        self.wait = -1

    def play(self, grid):
        if self.wait == -1:
            self.wait = time() + uniform(ai_play_time[0], ai_play_time[1])
        if self.wait > time():
            return
        while True:
            pawn = choice(grid.pawns)
            if pawn.color == self.color:
                moves = pawn.get_moves()
                if moves:
                    move = choice(moves)
                    pawn.move(move, grid)
                    self.wait = -1
                    return

class Max_Gain_Bot:
    score = { "pawn": 1, "bishop": 3, "knight": 3, "rook": 5, "queen": 9, "king": 9 }

    def __init__(self, color):
        self.color = color
        self.wait = -1

    def play(self, grid):
        if self.wait == -1:
            self.wait = time() + uniform(ai_play_time[0], ai_play_time[1])
        if self.wait > time():
            return
        
        best_pawn = None
        best_pawn_score = -1
        best_move_pos = None

        for pawn in grid.pawns:
            if pawn.color != self.color : continue
            for move in pawn.get_moves():
                if grid.get_pawn(move) == None:
                    score = 0
                else:
                    score = Max_Gain_Bot.score[grid.get_pawn(move).name]
                if score > best_pawn_score:
                    best_pawn_score = score
                    best_pawn = pawn
                    best_move_pos = move

        best_pawn.move(best_move_pos, grid)
        self.wait = -1
        return

class Network_Bot:
    score = { "pawn": 1, "bishop": 3, "knight": 3, "rook": 5, "queen": 9, "king": 9 }

    def __init__(self, color):
        self.color = color
        self.wait = -1
        self.network = NeuralNetwork([64, 72, 32, 1])

    def play(self, grid):
        if self.wait == -1:
            self.wait = time() + uniform(ai_play_time[0], ai_play_time[1])
        if self.wait > time():
            return
        
        best_pawn = None
        best_pawn_score = -1
        best_move_pos = None

        for pawn in grid.pawns:
            if pawn.color != self.color : continue
            for move in pawn.get_moves():
                score = self.network.forward(grid.get_network_inputs())
                if score > best_pawn_score:
                    best_pawn_score = score
                    best_pawn = pawn
                    best_move_pos = move

        best_pawn.move(best_move_pos, grid)
        self.wait = -1
        return

class Max_Gain_Bot_Depth:

    depth = 3
    score = { "pawn": 1, "bishop": 3, "knight": 3, "rook": 5, "queen": 9, "king": 9 }

    def __init__(self, color):
        self.color = color
        self.wait = -1

    def play(self, grid, turn=None, depth=None):
        
        if turn == None:
            turn = self.color
        if depth == None:
            depth = Max_Gain_Bot.depth

        if self.wait == -1:
            self.wait = time() + uniform(ai_play_time[0], ai_play_time[1])
        if self.wait > time():
            return
        
        best_pawn = None
        best_pawn_score = -1
        best_move_pos = None

        for pawn in grid.pawns:
            if pawn.color != self.color : continue
            for move in pawn.get_moves():
                if grid.get_pawn(move) == None:
                    score = 0
                else:
                    score = Max_Gain_Bot.score[grid.get_pawn(move).name]
                if score > best_pawn_score:
                    best_pawn_score = score
                    best_pawn = pawn
                    best_move_pos = move

            
        best_pawn.move(best_move_pos, grid)
        self.wait = -1
        return





