snum = []
def shellSort(a, n):
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = a[i]
            j = i
            while j >= gap and a[j - gap] > temp:
                a[j] = a[j - gap]
                j -= gap

            a[j] = temp
            snum.append(list(a))
        gap //= 2
        
def sortnum(a):
    size = len(a)
    shellSort(a, size)
    return snum