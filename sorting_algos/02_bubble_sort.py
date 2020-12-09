# Bubble sort algorithm 

# O(n^2) Time |O(1) Space 


# Optimized
def bubble_sort(array):
    is_sorted =False
    counter =0
    while is_sorted==False:
        for i in range(len(array)-1-counter):
            is_sorted = True
            if (array[i]>array[i+1]):
                print('Before ->',array)
                is_sorted =False
                array[i],array[i+1] =array[i+1],array[i]
                print(array)
        counter+=1        
    return array            




# bubble sort 

# O(n^2) Time |O(1) Space 

# Un - optimized
def bubble_sort2(array):
    for i in range(len(array)):
        for j in range(len(array)-1-i):
            if (array[j]>array[j+1]):
                array[j],array[j+1] =array[j+1],array[j]
    return array            


print(bubble_sort2([4,3,2,1]))        