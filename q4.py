from itertools import permutations

def is_valid_placement(matrix, row, permutation):
    for i in range(len(permutation)):
        if permutation[i] in matrix[row]:
            return False
        for j in range(row):
            if permutation[i] == matrix[j][i]:
                return False
    return True
    
def permutationUsedBefore(matrix, row, permutation, brucknerMatrix):
    for permutations in brucknerMatrix:
        if permutations[0] == matrix[0]:
            if permutations[row] == permutation:
                return True
    return False

def generateRow(matrix, row, n, brucknerMatrix):
    if row == n:
        return True  # All rows filled, buckner matrix generated

    for permutation in permutations(range(1, n + 1)):
        if is_valid_placement(matrix, row, list(permutation)) and not permutationUsedBefore(matrix, row, list(permutation), brucknerMatrix):
            matrix[row] = list(permutation)
            # Recursively attempt to fill the next row
            if generateRow(matrix, row + 1, n, brucknerMatrix):
                # If a solution is found, append a copy of the matrix to the result
                brucknerMatrix.append([row[:] for row in matrix])
            # Reset the current placement
            matrix[row] = [0] * n
            
    return False

def generateIndividualBruckner(n, permutation, brucknerMatrix):
    output = [[0] * n for _ in range(n)]
    output[0] = permutation
    # Generate each row from the 2nd row onwards
    generateRow(output, 1, n, brucknerMatrix)

def generate_bruckner(n):
    result = []
    for permutation in permutations(range(1, n + 1)):
        generateIndividualBruckner(n, permutation, result)
    return result

# Example: Generate all Bruckner matrices of size 3
bruckner_matrices_3 = generate_bruckner(3)
for brucknerMatrix in bruckner_matrices_3:
    print(brucknerMatrix)

#Print length of bruckner_matrices_3
print(len(bruckner_matrices_3))

# Example: Generate all Bruckner matrices of size 4
bruckner_matrices_4 = generate_bruckner(4)
for brucknerMatrix in bruckner_matrices_4:
    print(brucknerMatrix)

#Print length of bruckner_matrices_4
print(len(bruckner_matrices_4))

# Example: Generate all Bruckner matrices of size 5
bruckner_matrices_5 = generate_bruckner(5)
for brucknerMatrix in bruckner_matrices_5:
    print(brucknerMatrix)
    
#Print length of bruckner_matrices_5
print(len(bruckner_matrices_5))