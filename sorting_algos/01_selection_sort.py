# Selection sort algorithm

# O(n^2) Time |O(1) Space

def selection_sort(array):
    for i in range(len(array)):
        smallest_idx =i
        for j in range(i+1,len(array)):
            if array[j] <array[smallest_idx]:
                smallest_idx =j
                print(j)
        if smallest_idx != i:
           array[i],array[smallest_idx] =array[smallest_idx],array[i]
    return array                

print(selection_sort([5,4,3,2,1]))    