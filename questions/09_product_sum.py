
# O(n) Time | O(d) Space   where d is depth of arrays
def product_sum(array,multiplier=1):
    sum = 0 

    for element in array:
        if type(element) == list:
            sum += product_sum(element,multiplier+1)
        else:
            sum +=element 
    return multiplier*sum


print(product_sum([5, 2, [7, -1], 3, [6, [-13, 8], 4]]))  