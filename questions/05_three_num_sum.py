# O(n ^ 2) Time | O(1) Space


def three_num_sum(array,target_sum):
	array.sort()
	triplets = []

	for i in range(len(array)-2):
		leftIdx = i+1
		rightIdx =len(array) - 1
		while leftIdx < rightIdx:
			first,second,third = array[i],array[leftIdx],array[rightIdx]
			Sum = first + second + third
			if Sum == target_sum:
				triplets.append([first,second,third])
				leftIdx+=1
				rightIdx-=1
			elif Sum < target_sum:
			    leftIdx+=1
			else:
			    rightIdx-=1    	

	return triplets

print(three_num_sum([12,3,1,2,-6,5,-8,6],0))
