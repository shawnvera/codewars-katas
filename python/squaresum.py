# Begin
# Input are numbers can be positive or negative
# Loop through the list
# Square each character in the list
# Add each character
# Return answer
# End

def square_sum(numbers):
    # create variable holding the sum of each character squared
    answer = sum([char**2 for char in numbers])
    return answer