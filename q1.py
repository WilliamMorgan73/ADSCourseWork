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
    # Remove the number of elements from the string
    if (int(string[1]) - numberOfColour) < 1:
        return string[2:]
    else:
        return string[:1] + str(int(string[1]) - numberOfColour) + string[2:]

def encodedMask(M_e, T_e):
    output = []
    numberOfColour = 0
    currentColour = 0
    length = max(len(M_e), len(T_e))

    # Base case, if either of the strings are empty, return an empty list
    if length < 2:
        return output

    # Check the current letter of each string
    if M_e[0] == "B" or T_e[0] == "B":
        currentColour = "B"

    elif M_e[0] == "W" and T_e[0] == "W":
        currentColour = "W"

    else:
        currentColour = "B"

    numberOfColour = min(int(M_e[1]), int(T_e[1]))
    output.extend([str(currentColour)] * numberOfColour)
    temp_M_e = removeElement(M_e, numberOfColour)
    temp_T_e = removeElement(T_e, numberOfColour)
    # Recursively call the function and extend the output
    output.extend(encodedMask(temp_M_e, temp_T_e))

    return output

def apply_mask_encoded(M_e, T_e):

    list = encodedMask(M_e, T_e)
    count = 1
    output = ""
    i = 0

    while i < len(list) - 1:
        if list[i] == list[i+1]:
            count += 1
        else:
            output += list[i] + str(count)
            count = 1
        i += 1
    output += list[-1] + str(count)
    return output




