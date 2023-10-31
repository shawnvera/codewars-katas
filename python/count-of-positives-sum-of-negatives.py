def count_positives_sum_negatives(arr):
    # Initialize variable to hold count of positive numbers
    countPos = 0
    # Initialize empty array to append negative numbers
    listNeg = []
    
    # Conditional statment if input is None or empty return []
    if(arr == None):
        return []
    elif(arr == []):
        return []
    
    # For loop if i > 0 increment positive count.
    # Else append to the negative list
    for i in arr:
        if(i > 0):
            countPos+=1
        else:
            listNeg.append(i)
    
    # Return count of the positive numbers and the sum of th negative numbers in an list/array.
    return [countPos, sum(listNeg)]