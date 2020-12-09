

# O (n) Time | O(1) Space
def validate_sub_squence(array,sequnce):
	arrayIdx = 0
	sequenceIdx = 0 

	while arrayIdx < len(array) and sequenceIdx < len(sequnce):
		if array[arrayIdx] == sequnce[sequenceIdx]:
			sequenceIdx+=1
		arrayIdx +=1
	return  sequenceIdx == len(sequnce)
	
print([validate_sub_squence([5, 1, 22, 25, 6, -1, 8, 10],[1, 6, 10])])	

