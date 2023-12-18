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

#P is a test atht starts with 1
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
    matrixSize = int((sum(int(char) for char in S[1:] if char.isdigit())) ** 0.5) #If able to, rewrite this line to make look nicer.
    matrix = [[0] * matrixSize for _ in range(matrixSize)]   #And this line
    currentColour = S[0]
    count = 0
    rowIndex, colIndex = 0, 0

    for char in S[1:]:
        if char == 'B' or char == 'W':
            currentColour = char
            count = 0  # Reset count when colour changes
        elif char.isdigit():
            count = count * 10 + int(char)  # Update count based on the digit
            #*10 as Could be B12, therefore would get 1 * 10 + 2.
            for _ in range(int(char)):
                matrix[rowIndex][colIndex] = 1 if currentColour == 'W' else 0     #Rewrite this to be less compact version
                colIndex += 1
                if colIndex == matrixSize:
                    colIndex = 0
                    rowIndex += 1
                    if rowIndex == matrixSize:
                        rowIndex = 0

    return matrix

def apply_mask_encoded(M_e, T_e):
    matrixSize = int((sum(int(char) for char in M_e[1:] if char.isdigit())))
    i = 1
    while i < matrixSize:
      #Check if B or W, copy code from decode for char = B or W and the count * 10 to get the number of pixels for each colour
      




def q1_simple_tests():
    assert(apply_mask(I, J) == R)
    assert(encode(I) == 'B1W1B2W5')
    assert(encode(J) == 'B2W1B1W1B1W1B2')
    assert(decode('B1W1B2W5') == I)
    assert(apply_mask_encoded(encode(I), encode(J)) == encode(R))

print(apply_mask_encoded(encode(I), encode(J)) == encode(R))
print(apply_mask_encoded(encode(I),encode(J)))

print(encode(R))