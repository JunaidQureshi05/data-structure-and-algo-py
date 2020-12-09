
# O(n^2) Time | O(n) Space
def array_of_sum(array):
    new_array = []
    for i in range(len(array)):
        sum = 1
        for j in range(len(array)):
            if i !=j:
                sum *= array[j]
        new_array.append(sum)                 
    return new_array


# O(n) Time | O(n) Space
def arrayOfProducts(array):
    products = [1 for _ in range(len(array))]
    leftProducts = [1 for _ in range(len(array))]
    rightProducts = [1 for _ in range(len(array))]
    
    leftRunningProduct = 1
    
    for i in range(len(array)):
        leftProducts[i]= leftRunningProduct
        leftRunningProduct *= array[i]
    rightRunningProduct =1  
    for i in reversed(range(len(array))):
        rightProducts[i] = rightRunningProduct
        rightRunningProduct *= array[i]
    for i in range(len(array)):
        products[i] =leftProducts[i] * rightProducts[i]
        
    return products     

        
print(arrayOfProducts([5,1,4,2]))

