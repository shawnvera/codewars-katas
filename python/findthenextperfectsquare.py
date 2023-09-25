# Begin
# Input is a non-negative
# Find the square root of the input
# if the square root is an integer then add 1 then square
# if not an integer return -1
# return new square root
# End

import math

def find_next_square(sq):
    # create variable to hold the square root of the input (sq)
    sqRoot = math.sqrt(sq)
    
    # if the square root is an integer then add 1 and square
    if sqRoot.is_integer():
        nxtSq = (int(sqRoot) + 1) ** 2
        return nxtSq
    # if not an integer return -1
    else:
        return -1
