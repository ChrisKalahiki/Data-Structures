def BinarySearch(target, inputlist):
    first = 0                   `           
    last = len(inputlist) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if inputlist[midpoint] == target:
            found = True
        else:
            if target < inputlist[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

    return found