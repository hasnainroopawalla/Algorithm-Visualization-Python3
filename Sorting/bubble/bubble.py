
def sortnum(arr):
    
    n = len(arr)
    snum = []
    #snum.append(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
        
        snum.append(list(arr))
        

    return snum