def SelectionSort(inputlist):       
    for a in range(len(inputlist) - 1, 0, -1):
        max = 0
        for point in range(1, a + 1):
            if inputlist[point] > inputlist [max]:
                max = point

        temp = inputlist[a]
        inputlist[a] = inputlist[max]
        inputlist[max] = temp