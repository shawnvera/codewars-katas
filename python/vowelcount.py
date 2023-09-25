# Begin
# Input wil only be in lower case letters or spaces
# Count how many vowels are in the input
# vowels = a,e,i,o,u
# Return Count
# End

def get_count(sentence):
    # create variable to hold vowel count
    count = 0
    
    # create list of all the vowels
    vowels = ["a", "e", "i", "o", "u"]
    
    # Loop through sentence
    for char in sentence:
        
        # if char is in sentence is equal to any value in the vowels list
        if char in vowels:
            
            # increment count variable by 1
            count += 1
            
    return count