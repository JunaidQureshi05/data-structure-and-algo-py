
# O(2^n) Time | O(n) Space
# recursion methods
def nth_fobonacii(n):
    if n==1:
        return 0
    if n==2:
        return 1
    return nth_fobonacii(n-1) + nth_fobonacii(n-2)


print(nth_fobonacii(4))

# Optimized recursion
# O(n) Time | O(n) Space
def nth_fibonacii_2(n,memoize= {1:0,2:1}):
    if n in memoize:
        return memoize[n]
    else:
        memoize[n] =  nth_fobonacii(n-1) + nth_fobonacii(n-2)
        return memoize[n]

print(nth_fibonacii_2(4))

# Using loop
# O(n) Time | O(1) Space
def nth_fibonacii_3(n):
    lastTwo = [0,1]
    if n <=2:
        return lastTwo[n-1]
    i = 3
    while i <= n:
        Sum = lastTwo[0] + lastTwo [1]
        lastTwo[0] = lastTwo[1]
        lastTwo[1] =Sum
        i+=1
    return lastTwo[1]     
print(nth_fibonacii_3(4))   