import random

def bubbleSort(arr):
    n = len(arr)
    snum = [[]]
    for i in range(n):
       
        for j in range(0, n-i-1):

            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
                
        print(arr)
        snum.append(list(arr))
        for m in snum:
            print('snum',m)
        print()
 

arr = []
for i in range(11):
    arr.append(i)
random.shuffle(arr)

arr = [10,9,8,7,6,5,4,3,2,1]



bubbleSort(arr)
 
print ("Sorted array is:")
for i in range(len(arr)):
    print ("%d" %arr[i]), 
