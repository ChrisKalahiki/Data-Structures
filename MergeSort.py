def MergeSort(inputlist):
    if len(inputlist) > 1:
        mid = len(inputlist)//2
        left = inputlist[:mid]
        right = inputlist[mid:]

        MergeSort(left)
        MergeSort(right)

        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                inputlist[k] = left[i]
                i = i + 1
            else:
                inputlist[k] = right[j]
                j = j + 1
            k = k + 1

        while i < len(left):
            inputlist[k] = left[i]
            i = i + 1
            k = k + 1

        while j < len(right):
            inputlist[k] = right[j]
            j = j + 1
            k = k + 1