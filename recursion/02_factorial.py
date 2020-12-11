# Recursion method
# O(n) Time | O(n) Space
def factorial(n):
    if n<=1:
        return 1

    return n*factorial(n-1)
        


# Iterative method

def factorial_iterative(n):
    if n<=1:
        return 1

    
    else:
        result =1   
        counter =2  
        while counter<=n:
            result *=counter
            counter+=1
    return result       
print(factorial_iterative(5))