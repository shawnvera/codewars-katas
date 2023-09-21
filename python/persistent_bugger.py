# Begin
# n is a positive
# multiply the digits in num
# keep multiplying the result digits until a single digit is reached
# return the single digit
# End

def persistence(n):
    # create variable to store iteration count
    numberIterations = 0
    
    # while loop until n is a single digit
    while n >= 10:
        
        # converting n to a string in order to loop through
        numberString = str(n)
        
        # create a variable to store the iteration of digit
        product = 1
        
        # loop through each iteration multiplying each digit until reaching single digit
        for digit in numberString:
            # product(1) * digit
            product *= int(digit)
            
        # setting value of n to product   
        n = product
        
        # incrementing the iteration
        numberIterations += 1
        
    return numberIterations