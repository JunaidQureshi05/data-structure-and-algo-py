
# write a function that takes in a non emty string and returns its length encoding 

def run_length_encoding(string):
	encodingChars = []
	currentRunLength = 1

	for i in range(1,len(string)):
		previousChar = string[i-1]
		currentChar = string[i]

		if currentChar != previousChar or currentRunLength ==9:
			encodingChars.append(str(currentRunLength))
			encodingChars.append(previousChar)
			currentRunLength = 0
		currentRunLength+=1	
	encodingChars.append(str(currentRunLength))
	encodingChars.append(string[len(string)-1])
	return "".join(encodingChars)

print(run_length_encoding('AAAAAAAAAAAABBCCCDDEEEE'))		


