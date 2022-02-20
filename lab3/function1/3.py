def solve(numheads, numlegs):
    for rabbits in range(1, numheads+1):
        for chickens in range(1, numheads+1):
            if rabbits+chickens == numheads and 4*rabbits+2*chickens == numlegs:
                print('rabbits:', rabbits)
                print('chickens:',chickens)
solve(35,94)