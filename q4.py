def isValid(bruckner, row, col, num):
    """
    Checks if current placement of 'num' in the Bruckner list is valid.
    """
    # Check if 'num' is not present in the current row and column
    for i in range(len(bruckner)):
        if num in bruckner[row] or bruckner[i][col] == num:
            return False
    return True
   

def completeBruckner(bruckner, row, col, allBruckners):
    """
    Solves the bruckner square using backtracking and recursion.
    """
    #Get the length of the bruckner
    length= len(bruckner)

    # If all rows are filled, add the bruckner to the list
    if row == length:
        allBruckners.append([row[:] for row in bruckner])
        return

    # Try placing numbers in the current row
    for num in range(1, length + 1):
        if isValid(bruckner, row, col, num):
            bruckner[row][col] = num

            # Move to the next column or next row if the column is at the end
            if (col+1) == length:
                next_row = row + 1
            else:
                next_row = row
            
            next_col = (col + 1) % length

            completeBruckner(bruckner, next_row, next_col, allBruckners)

            # Backtrack when the above call returns to try other possibilities
            bruckner[row][col] = 0  
            
def generateAllBruckners(input):
    #base case, if input is less than 2, return empty list
    if input < 2:
        return []
    
    #Create a list of lists of 0s with row and column length of input (square)
    bruckner = [[0] * input for _ in range(input)]
    #Create a list to store all the bruckners
    bruckners = []
    
    completeBruckner(bruckner, 0, 0, bruckners)

    return bruckners