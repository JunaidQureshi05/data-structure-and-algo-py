

# Using recursion method
# O(2^n) Time | O(n) Space
def fib(n):
  if n==1:
    return 0
  elif n==2:
  	return 1    
  else:
      return fib(n-1) + fib(n-2)


# O(n) Time | O(n) Space
def getNthFib(n,memoize ={1:0,2:1}):
    if n in memoize:
        return memoize[n]
    else:
        memoize[n]= getNthFib(n-1,memoize) + getNthFib(n-2,memoize)
    return memoize[n]       
print(getNthFib(5))


# Using iterative method
# O(n) Time | O(1) Space
def fibonacii(n):
	last_two = [0,1]

	counter =3

	while counter<=n:
		last_two[0],last_two[1] =last_two[1],last_two[0]+last_two[1]
		counter+=1
	return last_two[1]	


print(fibonacii(5))