# Begin
# Input argument is a string
# Check string to see if it contains all letters a-z
# if it does Return True
# else Return False
# End

def is_pangram(s):
    # make all input lowercase
    s = s.lower()
    # create a set - unordered, no duplicates allowed
    alphabet = set()
    # Loop through s
    for i in s:
        # conditional if iteration is alpha
        if i.isalpha():
           # add to set 
            alphabet.add(i)
    # if the length of alphabet equals 26 then all letters are used and it's a pangram.        
    return (len(alphabet) == 26)