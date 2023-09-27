# Begin
# Argument passed is a string that is the current state of the light
# Return the next stage of the traffic light
# End

def update_light(current):
    # Conditional if statement based on current argument
    if(current == "green"):
        return "yellow"
    elif(current == "yellow"):
        return "red"
    else:
        return "green"