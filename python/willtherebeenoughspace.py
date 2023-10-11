def enough(cap, on, wait):
    # Initialize variable for available seats
    availableSeats = cap - on
    # Conditional
    if availableSeats >= wait:
        return 0
    elif availableSeats <= wait:
        return wait - availableSeats
