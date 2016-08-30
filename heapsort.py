def heapsort(arr):

    def lchild(i):
        return (i << 1) + 1
    
    def rchild(i):
        return (i + 1) << 1

    def max_heapify(begin, end):
        dad, son, key = begin, lchild(begin), arr[begin]
        while son <= end:
            if son + 1 <= end and arr[son] < arr[son + 1]:
                son += 1
            if key < arr[son]:
                arr[dad], dad, son = arr[son], son, lchild(son)
            else:
                break
        arr[dad] = key

    for i in range(len(arr) >> 1, -1, -1):
        max_heapify(i, len(arr) - 1)

    for i in range(len(arr) - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        max_heapify(0, i - 1)

t = [1,2,943,4,9,4,2,3,1032,34,-4,23,984,122,52]
heapsort(t)
print(t)
