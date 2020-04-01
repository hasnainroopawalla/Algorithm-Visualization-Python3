def sortnum(arr, maxnum):
    snum = []
    m = maxnum + 1
    count = [0] * m                
    
    for a in arr:

        count[a] += 1             
    i = 0
    for a in range(m):            
        for c in range(count[a]):  
            arr[i] = a
            i += 1
        snum.append(list(arr))
    return snum