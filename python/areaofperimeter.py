# Begin
# Argument passed is the length and width
# Conditional if length = width it's a square
# Return l * w
# Else it's a rectangle
# Return perimeter
# End

def area_or_perimeter(l , w):
    # Conditional checking if it's a square
    if(l == w):
        return l*w
    else:
        return l + l + w + w