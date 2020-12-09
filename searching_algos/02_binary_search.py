# Binary search algorithm

# Note: input array should be sorted

# O(log(n)) | O(1) Space

def binary_search(array,element):
    start = 0
    end   = len(array)-1
    mid   = (start+end) //2

    while start <= end:
        if array[mid] ==  element:
            return f'element found at {mid}'
        elif element < array[mid]:
            end =mid-1
        else:
            start =mid+1
        mid   = (start+end) //2
    return 'element not found'    


print(binary_search([1,2,3,4,5,6],1))