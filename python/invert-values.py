def invert(lst):
    # initialize answer variable to hold the solution list
    answer = []
    # loop through lst 
    for num in lst:
        # multiply each elemet by -1 to get the additive inverse
        num *= -1
        # append the num iteration to the answer list
        answer.append(num)
    return answer

# Best practices solution:
# def invert(lst):
#     return [-x for x in lst]