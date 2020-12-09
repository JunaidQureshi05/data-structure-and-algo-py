# Given two arrays , create a function that lets user know (true/false) whether two arrays contains any common item


#un - optimized way

# O(a*b) Time | O(1)Space 
def contains_common_item_1(arr1,arr2):
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            if arr1[i]==arr2[j]:
                return True
    return False            


# Optimized way
# O(a+b) Time | O(a) space

def contains_common_item_2(arr1,arr2):
    memoize ={ item:True for item in arr1}
    # for item in arr1:
    #     if item not in memoize:
    #         memoize[item] =True
    for item in arr2:
        if item in memoize.keys():
            return True
    return False            


def contains_common_item_3(arr1,arr2):
    memoize ={ item:True for item in arr1}
    for item in arr2:
        if item in memoize.keys():
            return True
    return False  
print(contains_common_item_3(['a','b','c','x'],['z','y','a']) )
print(contains_common_item_3(['g','b','c','x'],['z','y','a']) )