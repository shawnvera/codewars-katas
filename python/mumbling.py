# Begin
# Input is a string
# Return a string with each letter capitalized
# That letter in lower case should follow the number of time that matches its index in the string
# For example: "abcd" -> "ABbCccDddd"
# End

def accum(s):
    # creating answer variable to store sequence in a list
    answer = []
    
    # Looping through with the enumerate function
    for i, char in enumerate(s):
        # declare sequence where first character is capitalized
        # then followed by the same lowercase letter repeated by number of iterations
        seq = char.upper() + char.lower() * i
        answer.append(seq)
    
    # return the answer joined with a "-". This converts back to a string
    return "-".join(answer)