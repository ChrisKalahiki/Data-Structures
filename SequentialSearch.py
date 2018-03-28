def SequentialSearch(target, inputlist):
    for element in inputlist:
        if target == element: return True
    return False