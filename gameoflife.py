################################################################################
#Conway's Game of Life (Python 3.6 implementation)                             #
################################################################################
#(creative commons) Jon Patton May 11, 2017                                    #
################################################################################
#This is an implementation of Dr. John H. Conway's game of life in Python 3.   #
#It has some random generation elements to ensure that there are fewer steady  #
#states and dynamic sizing. The bones are also there if you want to let the    #
#user change the speed of generation.                                          #
#See https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life for rules etc.      #
################################################################################

import time, numpy, random, os

#numpy.set_printoptions(formatter={"|{:2}|"}.format)

def main():
    boardSize = 0
    print("Welcome to the game of life! We will make some creatures and see how long they survive!\n")
    try:
        boardSize = int(input("First enter the size of the board: \n\
(enter n where the grid size will be n x n*2 - at least 10.)"))
    except:
        ValueError("Numbers only!\n")
        main()
    if boardSize < 10:
        print("That's too small!\n")
        main()
    print("\n")
    generations = int(input("Now enter how many generations you want the game to run: "))
    board = seed(numpy.zeros((boardSize, boardSize*2), dtype=numpy.str))

    #Hypothetically could make the speed variable, so check the time.
    t = time.time()

    #Using primes for the generational random -- makes it more random.
    sieve = primeSieve(2, 50)
    highestRandom = len(sieve)

    while generations > 0:
        if time.time() - t >= 0.1:
            if generations % sieve[random.randint(4, highestRandom-1)] == 0:
                seed(board)
            board = gen(board)
            t = time.time()
            #random generation -- sometimes just we get a few beacons and the fun stops!
            generations -= 1
    print()

def drawBoard(board):
    os.system("clear")
    print("\n"
                .join(["".join(['{:1}'.format(i) for i in row]) for row in board]))
    for i in range (0, len(board)):
        for j in range (0, len(board)*2):
            if j == 0 or j == len(board)*2 - 1:
                board[i][j] = "|"
            elif i == 0 or i == len(board) - 1:
                board[i][j] = "-"

def seed(board):
    #Since we aren't inputting starting positions, we generate a semi-random number
    #of blocks around a spot on the board. And sometimes you get extra seeds.
    #But it's never explosive growth (per the rules of the game)
    x, y = random.randint(4, len(board)-4), random.randint(4, len(board)*2 - 4)
    for i in range (-2, 2):
        for j in range (-2, 2):
            spawn = random.randint(0, 2)
            if spawn == 1 or spawn == 2:
                board[x-i][y-j] = u'\u2588'
    board[x][y] = " "
    if spawn == 0 or spawn == 1:
        seed

    drawBoard
    return board

def gen(board):
    for x in range (1, len(board)-1):
        for y in range (1, len(board)*2-1):
            neighbors = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if board[x+i][y+j] == u'\u2588' or board[x+i][y+j] == "k":
                        neighbors += 1

            #Randomly kills cells against the wall of the board. (This helps keep it going longer.)
                    if (board[x+i][y+j] == '-' or board[x+i][y+j] == "|") and board[x+i][y+j] == u'\u2588':
                        neighbors += (random.randint(-1, 1))

            #Per the rules of the game: populated cells with >4 or <2 neighbors will die...
            if (neighbors >= 5 or neighbors <= 2) and board[x][y] == u'\u2588':
                board[x][y] = "k"
            #and empt cells with exactly 3 neighbors will reproduce.
            elif neighbors == 3 and board[x][y] != u'\u2588':
                board[x][y] = "g"

    #Now replace any kill or generate cell so all changes happen simulataneously.
    killedsomething = 0
    for x in range (1, len(board)-1):
        for y in range (1, len(board)*2-1):
            if board[x][y] == "k":
                board[x][y] = " "
                killedsomething += 1
            if board[x][y] == "g":
                board[x][y] = u'\u2588'

    #Another method of keeping the fun going just a little longer.
    if killedsomething < 4:
        board = seed(board)

    drawBoard(board)
    return board

#Quickly generates a set of primes for the random generation.
def primeSieve(a, b):
    fullRange, sieve = [True]*b, []
    if a < 3:
        sieve.append(2)

    for i in range (3, int(b**0.5 + 1), 2):
        if fullRange[i] is not 0 and fullRange[i] is not 1:
            for j in range (i**2, b, i):
                fullRange[j] = 0

    for i in range (3, b, 2):
        if fullRange[i] and i > a:
            sieve.append(i)

    return sieve

main()
