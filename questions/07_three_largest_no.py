
# O(n) Time | O(1) Space

def three_largest_no(array):
    threeLargest = [None,None,None]

    for num in array:
        if threeLargest[2] == None or threeLargest[2] < num:
            shift_and_update(threeLargest,num,2)
        elif threeLargest[1] ==None or threeLargest[1]<num:
            shift_and_update(threeLargest,num,1)   
        elif threeLargest[0] == None or threeLargest[0] < num:
            shift_and_update(threeLargest,num,0)
    return threeLargest            




# Helper function for shifting and updating three_largest_no array
def shift_and_update(array,num,idx):
    i = 0

    while i != idx:
        array[i] = array[i+1]
        i+=1
    array[idx] = num    


print(three_largest_no([55, 7, 8]))