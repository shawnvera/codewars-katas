# Begin
# Given arguments are beast (name of the animal) and dish (name of the dinner)
# Arguments are always lower case strings
# Each argument has at least 2 letters
# Arguments can contain hyphens or spaces but won't be at the beginning or end
# Arguments will NOT contain numbers
# Conditional - if the first letter of the dish is equal to the first letter of the beast
# Conditional - if the last letter of the dish is equal to the last letter of the beast
# Return True if conditionals pass else return False
# End

def feast(beast, dish):
    # conditional if first index of beast is equal to first index of dish AND last index of
    # beast and last index of dish are equal return True, else return False
            if(beast[0] == dish[0] and beast[-1] == dish[-1]):
                return True
            else:
                return False