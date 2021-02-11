# Quick Sort algorithm
# O(nlog(n)) Time -Best
# O(n^2) Time -Worst
# O(log(n)) -Space -call Stack
def quickSort(array):
    quickSortHelper(array,0,len(array)-1)
    return array

def quickSortHelper(array,startIdx,endIdx):
    if startIdx>=endIdx:
        return
    pivotIdx =startIdx
    leftIdx=startIdx+1
    rightIdx =endIdx
            
    while leftIdx <= rightIdx:
        if array[leftIdx] > array[pivotIdx] and array[rightIdx]< array[pivotIdx]:
            swap(array,leftIdx,rightIdx)
        if array[leftIdx]<= array[pivotIdx]:
            leftIdx+=1
        if array[rightIdx] >= array[pivotIdx]:
            rightIdx-=1
    swap(array,rightIdx,pivotIdx)

    leftSubArrayIsSmall = rightIdx -1 -startIdx < endIdx -(rightIdx+1)

    if leftSubArrayIsSmall:
        quickSortHelper(array,startIdx,rightIdx-1)       
        quickSortHelper(array,rightIdx+1,endIdx)    
    else:
        quickSortHelper(array,rightIdx+1,endIdx)            
        quickSortHelper(array,startIdx,rightIdx-1)       




# swap function
def swap(array,a,b):
    array[a],array[b] =array[b],array[a]


print(quickSort([8, 5, 2, 9, 5, 6, 3]))    
