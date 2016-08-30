def quick_sort(arr):

    def qsort(begin, end):
        if begin < end:
            key = arr[end]
            i = begin - 1
            for j in range(begin, end):
                if arr[j] <= key:
                    i += 1
                    arr[j], arr[i] = arr[i], arr[j]
            arr[i + 1], arr[end] = arr[end], arr[i + 1]

            qsort(begin, i)
            qsort(i + 2, end)
    qsort(0, len(arr) - 1)

t = [1,2,943,4,9,4,2,3,1032,34,-4,23,984,122,52]
quick_sort(t)
print(t)