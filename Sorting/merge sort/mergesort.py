snum = [] 
def merge(a, l, m, r): 
    n1 = m - l + 1
    n2 = r- m 
    
    LEFT = [0] * (n1) 
    RIGHT = [0] * (n2) 
  
    # Copy data to temp arrays LEFT[] and RIGHT[] 
    for i in range(0 , n1): 
        LEFT[i] = a[l + i] 
  
    for j in range(0 , n2): 
        RIGHT[j] = a[m + 1 + j] 
  
    i = 0  
    j = 0      
    k = l     
  
    while i < n1 and j < n2 : 
        if LEFT[i] <= RIGHT[j]: 
            a[k] = LEFT[i] 
            i += 1
        else: 
            a[k] = RIGHT[j] 
            j += 1
        k += 1
  
    while i < n1: 
        a[k] = LEFT[i] 
        i += 1
        k += 1
  
    while j < n2: 
        a[k] = RIGHT[j] 
        j += 1
        k += 1
    snum.append(list(a))

def mergeSort(a, l, r): 
    if l < r: 
        m = (l+(r-1))//2
        mergeSort(a, l, m) 
        mergeSort(a, m+1, r) 
        merge(a, l, m, r) 
  
def sortnum(a):
    mergeSort(a,0,len(a)-1) 
    return snum
