"""
This problem was asked by Google.

The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a Monte Carlo method.

Hint: The basic equation of a circle is x2 + y2 = r2.
"""

import random

def monteCarloToEstimatePi():

    # consider a unit circle, its area is pi/4
    # consider unit square, area is 1
    # while generating random points from (0,0) to (1,1)
    # those that fall in circle are desirable has a ratio
    # of pi/4 to total generated points.
    iterations = 10000000
    desired = 0
    i = 0
    for i in range(iterations):
        x, y = random.random(), random.random()
        if x**2 + y**2 <= 1:
            desired += 1

    return desired/iterations * 4

if __name__ == '__main__':
    pi = monteCarloToEstimatePi()
    print(pi)