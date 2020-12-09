# 1--> First approach
# O(nlog(n)) Time | O(1) Space
def has_pair_with_sum(array,sum):
    array.sort()
    leftIdx = 0 
    rightIdx =len(array)-1

    while leftIdx < rightIdx:
        current_sum = array[leftIdx] + array[rightIdx]
        if current_sum == sum:
            return True
        elif current_sum > sum:
            rightIdx -=1
        else:
            leftIdx+=1
    return False

print(has_pair_with_sum([1,2,3,4,1],8))                       

# 2--> Second approach
# O(nlog(n)) Time | O(n) Space
def has_pair_with_sum2(array,sum):
    memoize = {}

    for num in array:
        potentialMatch = sum -num
        if potentialMatch in memoize:
            return True
        else:
            memoize[num] =True
    return False         

print(has_pair_with_sum2([1,2,3,4,1,5],8))       