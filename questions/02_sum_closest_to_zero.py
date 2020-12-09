# Qusetion

# O(nlog(n)+mlog(m)) Time | O(1) Space

def sum_closest_to_zero(arr1,arr2):
    arr1.sort()
    arr2.sort()
    current= float('inf')
    smallest = float('inf')
    firstIdx = 0
    secondIdx = 0
    smallest_pair =[]
    while firstIdx < len(arr1) and secondIdx < len(arr2):
        first_num =arr1[firstIdx]
        second_num =arr2[secondIdx]
        print(first_num,second_num)
        if first_num > second_num :
           current = first_num - second_num
           secondIdx+=1
        elif second_num > first_num:
           current = second_num - first_num
           firstIdx+=1
        else:
            return [first_num,second_num]
        if current < smallest:
            smallest =current
            smallest_pair = [first_num,second_num]              
    return smallest_pair
print(sum_closest_to_zero([-1, 5, 10, 20, 28, 3],[26, 134, 135, 15, 17]))