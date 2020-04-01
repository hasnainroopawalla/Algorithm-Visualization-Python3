snum = []
def partition(a,low,high): 
    small = (low - 1)   
    pivot = a[high]     
  
    for j in range(low , high): 
        if   a[j] <= pivot: 
            small = small+1 
            a[small],a[j] = a[j],a[small] 
        snum.append(list(a))
    a[small+1], a[high] = a[high], a[small+1] 
    
    return (small+1) 

def quickSort(a, low, high): 
    if low < high: 
        partition_index = partition(a,low,high) 
        quickSort(a, low, partition_index-1) 
        quickSort(a, partition_index+1, high) 

def sortnum(a):
    quickSort(a,0,len(a)-1) 
    return snum
  