# Linear search algorithms

# O(n) Time | O(1) Space
def linear_search(array,element):
	for i in range(len(array)):
		if (array[i]==element):
			return f'{element} found at index :{i}'
	return 'element not found'		


print(linear_search([1,2,4,5,6,7,10],100))
