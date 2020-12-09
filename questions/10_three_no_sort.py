
#O(n) Time | O(1) Space

# def three_no_sort(array,order):
#     counts= [0,0,0]
#     for num in array:
#         index = order.index(num)
#         counts[index] +=1
#     for i in range(3):
#         nos_before = sum(counts[:i])
#         no_of_times =counts[i]
#         number  =order[i]
#         for j in range(no_of_times):
#             array[nos_before+j] = number      
#     return array            


# print(three_no_sort([7, 8, 9, 7, 8, 9, 9, 9, 9, 9, 9, 9],[8, 7, 9]))

# Alternate method

def three_no_sort_2(array,order):
    firstIdx = 0
    first_number = order[0]
    thirdIdx = len(array)-1
    third_number = order [2]

    for i in range(len(array)):
        if array[i] == first_number:
            array[i] ,array[firstIdx] =array[firstIdx],array[i]
            firstIdx+=1          
    for i in range(len(array)-1,-1,-1):
        if array[i] ==third_number:
            array[i],array[thirdIdx] =array[thirdIdx],array[i]
            thirdIdx -=1

    return array        

print(three_no_sort_2([7, 8, 9, 7, 8, 9, 9, 9, 9, 9, 9, 9],[8, 7, 9]))