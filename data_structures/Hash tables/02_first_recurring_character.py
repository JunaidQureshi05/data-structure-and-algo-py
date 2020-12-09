# Google question
# O(n) Time | O(1) Space
def first_recurring_char(array):
    memoize ={}

    for i in range(len(array)):
        if array[i] in memoize:
            return array[i]
        else:
            memoize[array[i]] = True
    
    return None


print(first_recurring_char([1,5,5,1,2,3,4,5,6]))                    