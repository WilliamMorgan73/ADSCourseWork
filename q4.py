from itertools import permutations

def is_valid_placement(matrix, row, col, permutation):
    # Check if each value of the permutation is unique in the current row and column
    
    for i in range(row):
        #Check if the current value is unique in the current row
        
        if matrix[row][i] == permutation[col]:
            return False
        #Check if the current value is unique in the current column
        if matrix[i][col] == permutation[col]:
            return False
    return True

def generateRow(matrix, row, n):
    if row == n:
        return True  # All rows filled, buckner matrix generated

    #Generate all permutations of the numbers from 1 to n
    for permutation in permutations(range(1, n + 1)):
        #Attempt to fill the current row with the current permutation
        for i in range(n):
            # Check if the current permutation is a valid placement
            if is_valid_placement(matrix, row, i, list(permutation)):
                # Valid placement, fill the current row with the current permutation
                matrix[row] = list(permutation)

                break
            
            #If the current permutation is not a valid placement, try the next permutation
            else:
                continue
            
            #If all permutations have been tried and no valid placement is found, backtrack, unless the current row is the second row
            
    

def generateIndividualBruckner(n, permutation):
    # Initialize an empty list of lists with n rows and n columns
    output = [[0] * n for _ in range(n)]

    # First row is based on the given permutation
    output[0] = permutation

    # Generate each row from the 2nd row onwards
    for row in range(1, n):
        # Recursively attempt to fill row
        if generateRow(output, row, n):
            # Row filled, continue to the next row
            continue

        else:
            # Backtrack if no valid value found for the current row
            for i in range(row, n):
                output[i][i] = 0

    return output

def generate_bruckner(n):
    result = []

    # Loop through all permutations of the numbers from 1 to n
    for permutation in permutations(range(1, n + 1)):
        # Generate the Bruckner matrix for the current permutation and add it to the result
        brucknerMatrix = generateIndividualBruckner(n, permutation)
        result.append(brucknerMatrix)

    return result

# Example: Generate all Bruckner matrices of size 4
bruckner_matrices_4 = generate_bruckner(4)
for brucknerMatrix in bruckner_matrices_4:
    print(brucknerMatrix)
