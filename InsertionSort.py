def InsertionSort(inputlist):
    for index in range(1, len(inputlist)):
        current = inputlist[index]
        pos = index
        while pos > 0 and inputlist[pos -1] > current:
            inputlist[pos] = inputlist[pos - 1]
            pos = pos -1
        inputlist[pos] = current