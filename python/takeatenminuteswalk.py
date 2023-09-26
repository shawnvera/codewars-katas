# Begin
# Argument passed = a list of string elements
# Evaluate the directions that are given in the argument
# Each letter represents a direction 
# Each letter will account for 1 block of distance
# Each letter will acount for 1 minute of time
# 10 minute time limit
# Argument directions have to return to the starting point
# Return True if the walk can be made, else return False
# End

def is_valid_walk(walk):
    # for loop for iterator of walk
    for i in walk:
        # declaring a variable to hold each direction
        stepsN = walk.count("n")
        stepsE = walk.count("e")
        stepsS = walk.count("s")
        stepsW = walk.count("w")
        
        # Conditional if length of walk equals 10 and steps north equal south and steps west equal east
        if(len(walk) == 10) and (stepsN == stepsS) and (stepsE == stepsW):
            return True
        else:
            return False