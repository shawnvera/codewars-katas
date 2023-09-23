def array_diff(a, b):
    # filter out elements in a that are in b
    # return a without the matching elements
    # using a list comprehension to filer through the list and apply a conditional
    return [x for x in a if x not in b]