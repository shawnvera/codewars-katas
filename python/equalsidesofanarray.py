# Begin
# Argument passed is an array of integers
# Find the index of each element (N) of the array
# Sum the integers
# Sum the integers to the left of N
# Subtract what is left of N from the total to get right of N
# IF left sum equals right sum return the index
# Else return -1

def find_even_index(arr):
    # initialize total variable sum of arr
    total = sum(arr)
    # initialize left variable original value is 0
    left = 0
    # for loop through the range of length of arr list
    for i in range(len(arr)):    
        # conditional checking if left sum is equal to right sum
        if left == (total - left - arr[i]):
            return i
        # adding current element to left sum before continuing the loop
        left += arr[i]
    return -1
    