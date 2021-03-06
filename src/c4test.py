import connectFour
import individual
import sys
import fitness
import numpy as np
import minimax
import population
import random

pop0 = population.load_population("pop_gen0.txt")
pop100 = population.load_population("pop_gen27.txt")
net100 = pop100.population[0]
pop100 = population.load_population("pop_gen240.txt")
net100 = pop100.population[0]

w = 0
t = 0
l = 0
for k in range(50):
    board = np.zeros((6,7))
    net100 = pop100.population[random.randint(0,19)]
    net0 = pop0.population[random.randint(0,19)]
    win = fitness.compete(net100, net0)
    print ("WINNER:" + str(win))
    if win == 1:
        w+=1
    elif win == 0:
        t+=1
    else:
        l+=1
    # move = input("make a move: ")


print("WINS: %d  TIES: %d  LOSS: %d"%(w,t,l))

while True:
    board = np.zeros((6,7))
    connectFour.print_board(board)
    while(connectFour.checkWinner(board) ==2):
        move = input("make a move: ")
        if not connectFour.check_valid(board, move):
            continue
        #connectFour.play(board, 1, minimax.pickMove(board, 1, 3, net0))
        connectFour.play(board, 1, move)
        connectFour.print_board(board)
        # raw_input("press")
        print
        if not connectFour.checkWinner(board)==2:
            break
        connectFour.play(board, -1, minimax.pickMove(board, -1, 3, net100))
        connectFour.print_board(board)
    print ("WINNER:" + str(connectFour.checkWinner(board)))
