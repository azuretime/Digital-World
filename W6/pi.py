import math
import random
import time
random.seed(round(time.time()/3,-1)) #do not seed elsewhere in your code

def pi_approx_by_monte_carlo(numThrows):
    hits = 0
    for i in range (0,numThrows):
        x = random.random()
        y = random.random()
        dist = math.sqrt(math.pow(x,2) + math.pow(y,2))
        if dist <= 1.0:
            hits = hits + 1.0
    pi = 4.0 * (float(hits) / numThrows)
    return round(pi,2)

'''Return x raised to the power y. Exceptional cases follow Annex ‘F’ of the C99 standard as far as possible. 
In particular, pow(1.0, x) and pow(x, 0.0) always return 1.0, even when x is a zero or a NaN. 
If both x and y are finite, x is negative, and y is not an integer then pow(x, y) is undefined, and raises ValueError.
Unlike the built-in ** operator, math.pow() converts both its arguments to type float. 
Use ** or the built-in pow() function for computing exact integer powers.'''