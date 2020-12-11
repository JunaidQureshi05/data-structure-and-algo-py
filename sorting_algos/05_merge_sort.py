# O(nlogn) Time -divide and conquer
# O(n+log(n)) => O(n) Space

def merge_sort(array):
    if len(array) ==1:
        return array

    mid = len(array) // 2

    left = array[:mid]
    right = array[mid:]
    return merge_sorted_array(merge_sort(left),merge_sort(right))   


def merge_sorted_array(left,right):
    array = []
    leftIdx = 0
    rightIdx = 0

    while leftIdx < len(left) and rightIdx <len(right):
        if left[leftIdx] < right[rightIdx]:
            array.append(left[leftIdx])
            leftIdx+=1
        else:
            array.append(right[rightIdx])
            rightIdx+=1
    
    while leftIdx < len(left):
        array.append(left[leftIdx])
        leftIdx+=1

    while rightIdx < len(right):
        array.append(right[rightIdx])               
        rightIdx+=1
    return array


arr = [99,44,6,2,1,5,63,87,283,4,0]
x = merge_sort(arr)
print(x)


