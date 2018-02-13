import random
import time
random.seed(round(time.time()/3,-1))   #do not seed elsewhere in your code

def throw_dice(n,nExp):
    count = 0.
    for i in range(nExp):
        success = 0
        for m in range(n):
            a = random.randint(1,6)
            if a == 6:
                success =1
        if success ==1:
            count += 1
    p = count/nExp
    return round(p,2)
##
import random
import time
random.seed(round(time.time()/3,-1))   #update the seed every 30 seconds

def n6(n):
    nSix = 0  # no of 6
    for i in range(n):
        eyes = random.randint(1, 6)
        if eyes == 6:
            nSix += 1
    return nSix

def throw_dice(n, nExp):
    M = 0
    for i in range(nExp):
        if n6(n) >= 1:
            M += 1
    probability = float(M)/nExp
    return round(probability,2)
    