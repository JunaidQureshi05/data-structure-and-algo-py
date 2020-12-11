
# O(n) Time | O(n) Space

def fibonacii(n,memoize={1:0,2:1}):
	if n in memoize:
		return memoize[n]
	else:
		memoize[n] = fibonacii(n-1,memoize) + fibonacii(n-2,memoize)	
	return memoize[n]	

print(fibonacii(5))
