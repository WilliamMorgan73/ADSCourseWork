# I is a list-of-lists representation of a 3x3 black-and-white image
I = [
  [0, 1, 0], 
  [0, 1, 1],
  [1, 1, 1]
]

# J is a list-of-lists representation of a 3x3 black-and-white image
J = [
  [0, 0, 1], 
  [0, 1, 0],
  [1, 0, 0]
]

# R is the result of applying the AND-mask I to the image J
R = [
  [0 & 0, 0 & 1, 1 & 0], 
  [0 & 0, 1 & 1, 0 & 1],
  [1 & 1, 0 & 1, 0 & 1]
]

#P is a test that starts with 1
P = [
  [1, 0, 1], 
  [0, 1, 0],
  [1, 0, 0]
]

def apply_mask(M, T):
    i = 0
    R = []

    for i in range(len(M)):
        result_row = []
        for j in range(len(M[0])):
            result_row.append(M[i][j] & T[i][j])
        R.append(result_row)

    return R

def encode(I):
    encoding = ''
    currentColour = 'B' if I[0][0] == 0 else 'W'
    count = 0

    for row in I:
        for pixel in row:
            if pixel == 0:
                pixelColour = 'B'
            else:
                pixelColour = 'W'

            if pixelColour == currentColour:
                count += 1
            else:
                encoding += f"{currentColour}{count}"
                currentColour = pixelColour
                count = 1

    encoding += f"{currentColour}{count}"

    return encoding
    
def decode(S):
    matrixSize = int((sum(int(char) for char in S[1:] if char.isdigit())) ** 0.5)
    matrix = [[0] * matrixSize for _ in range(matrixSize)]
    currentColour = S[0]
    count = 0
    rowIndex, colIndex = 0, 0

    for char in S[1:]:
        if char == 'B' or char == 'W':
            currentColour = char
            count = 1  # Reset count when colour changes, assuming single-digit count
        elif char.isdigit():
            count = int(char)  # Update count based on the digit, assuming single-digit count (Only being tested up to 3x3 matricies)
            for _ in range(count):
                matrix[rowIndex][colIndex] = 1 if currentColour == 'W' else 0
                colIndex += 1
                if colIndex == matrixSize:
                    colIndex = 0
                    rowIndex += 1
                    if rowIndex == matrixSize:
                        rowIndex = 0

    return matrix

def removeElement(string, numberOfColour):
    # Check if the index is within the bounds of the string
    
    # Remove the number of elements from the string
    if (int(string[1]) - numberOfColour) < 1:
        return string[2:]
    else:
        return string[:1] + str(int(string[1]) - numberOfColour) + string[2:]


def apply_mask_encoded(M_e, T_e):
    output = []
    
    numberOfColour = 0
    currentColour = 0
    length = max(len(M_e), len(T_e))

    # Base case, if either of the strings are empty, return an empty list
    if length < 2:
        return output
    
    # Check the current letter of each string
    if M_e[0] == "B" or T_e[0] == "B":
        currentColour = 0      
                
    elif M_e[0] == "W" and T_e[0] == "W":
        currentColour = 1       

    else:
        currentColour = 0 
            
    numberOfColour = min(int(M_e[1]), int(T_e[1]))
    output.append([currentColour] * numberOfColour)
    temp_M_e = removeElement(M_e, numberOfColour)
    temp_T_e = removeElement(T_e, numberOfColour)
    # Recursively call the function and extend the output
    print(temp_M_e, temp_T_e)
    print(output)
    output.extend(apply_mask_encoded(temp_M_e, temp_T_e))      

    return (','.join(output))
   
print (apply_mask_encoded("B1W1B2W5", "B2W1B1W1B1W1B2"))




def q1_simple_tests():
    assert(apply_mask(I, J) == R)
    assert(encode(I) == 'B1W1B2W5')
    assert(encode(J) == 'B2W1B1W1B1W1B2')
    assert(decode('B1W1B2W5') == I)
    assert(apply_mask_encoded(encode(I), encode(J)) == encode(R))


