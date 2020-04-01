def sortnum(arr): 
    snum = []
    n = len(arr) 
    swapped = True
    start = 0
    end = n-1
    while (swapped == True): 
        snum.append(list(arr))
        swapped = False

        for i in range (start, end): 
            if (arr[i] > arr[i + 1]) : 
                arr[i], arr[i + 1]= arr[i + 1], arr[i] 
                swapped = True
  
        if (swapped == False): 
            break

        swapped = False 
        end = end-1
  

        for i in range(end-1, start-1, -1): 
            if (arr[i] > arr[i + 1]): 
                arr[i], arr[i + 1] = arr[i + 1], arr[i] 
                swapped = True

        start = start + 1
    return snum
