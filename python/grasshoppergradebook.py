# Begin
# Arguments passed are integers
# Calculate avg of arguments
# Conditional if avg is between given ranges
# Return letter grade
# End

def get_grade(s1, s2, s3):
    # Initialize avg variable 
    avg = (s1 + s2 + s3)/ 3
    # Conditional if for ranges of letter grades
    if(avg >= 90):
        return "A"
    elif(avg >= 80 and avg < 90):
        return "B"
    elif(avg >= 70 and avg < 80):
        return "C"
    elif(avg >= 60 and avg < 70):
        return "D"
    else:
        return "F"
    