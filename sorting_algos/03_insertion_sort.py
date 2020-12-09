# Insertion sort algorithm

# O(n^2) Time | O(1) Space
def insertion_sort(array):
	for i in range(1,len(array)):
		j=i

		while j>0 and array[j] < array[j-1]:
			array[j],array[j-1] = array[j-1],array[j]
			j-=1
	return array
	
print(insertion_sort([5,4,3,2,1]))	
