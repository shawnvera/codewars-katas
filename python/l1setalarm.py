# Begin
# Arguments passed are boolean
# Return False if employed = true and vacation = true

def set_alarm(employed, vacation):
    # Conditional statements 
    if(employed == True and vacation == True) or (employed == False and vacation == True) or (employed == False and vacation == False):
        return False
    elif(vacation == True):
        return False
    return True