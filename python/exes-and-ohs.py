# Begin
# given a string
# check count of X's in string
# check count of O's in string
# compare X's to O's
# if equal return true, if not return false
# END


def xo(s):
    # format string to all lower case
    formatS = s.lower()
    # store number of lower case "x" in variable numOfX
    numOfX = formatS.count("x")
    # store number of lower case "o" in variable numOfO
    numOfO = formatS.count("o")
    
    # compare number of "x" to number of "o"
    if (numOfX == numOfO):
        # if they are equal return true
        return True
    else:
        # if not equal return false
        return False