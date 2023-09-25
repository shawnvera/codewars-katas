# Begin
# Parameters can be alphanumeric, float, negative strings
# Conditional - if parameter is 4 or 6 digits return True, else return False
# Conditional - if parameter contains any letter, float, or negative return False
# End

def validate_pin(pin):
    # conditional if pin is equal to 4 or 6
    if len(pin) == 4 or len(pin) == 6:
        # conditional if pin is numeric
        if pin.isnumeric():
            return True
    return False
        