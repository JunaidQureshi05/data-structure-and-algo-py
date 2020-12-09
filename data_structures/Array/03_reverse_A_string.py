# O(n) Time | O(n) Space

def reverse_string(string):
	if type(string) != str or len(string) < 2:
		return string
	array =[]	
	for i in range(len(string)):
		array.append(string[i])

	array.reverse()
	return ''.join(array)

print(reverse_string('Heyy ! My name is Junaid'))