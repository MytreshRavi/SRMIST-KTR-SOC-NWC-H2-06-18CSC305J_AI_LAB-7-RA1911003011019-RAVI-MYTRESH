import random
from random import seed, randint
import numpy

def game(winningdoor, selecteddoor, change=False):
    assert winningdoor < 3
    assert winningdoor >= 0

    
    removeddoor = next(i for i in range(3) if i != selecteddoor and i != winningdoor)

  
    if change:
        selecteddoor = next(i for i in range(3) if i != selecteddoor and i != removeddoor)

   
    return selecteddoor == winningdoor


if __name__ == '__main__':
    playerdoors = numpy.random.random_integers(0,2,(1000*1000*1))

    winningdoors = [d for d in playerdoors if game(1, d)]
    print("Winning percentage without changing choice: ", len(winningdoors) / len(playerdoors))

    winningdoors = [d for d in playerdoors if game(1, d, change=True)]
    print("Winning percentage while changing choice: ", len(winningdoors) / len(playerdoors))