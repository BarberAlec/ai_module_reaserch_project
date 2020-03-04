"""
This is the file that all evaluations will take place, ideally we should
not have to access Othello.py again :)
"""
from Othello import othello
from othello_ai import human_ai, decisionRule_ai, minimax_ai, NN_ai

game = othello()
score = game.startgame(human_ai('X'))
