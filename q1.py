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
    current_color = 'B' if I[0][0] == 0 else 'W'
    count = 0

    for row in I:
        for pixel in row:
            if pixel == 0:
                pixel_color = 'B'
            else:
                pixel_color = 'W'

            if pixel_color == current_color:
                count += 1
            else:
                encoding += f"{current_color}{count}"
                current_color = pixel_color
                count = 1

    encoding += f"{current_color}{count}"

    return encoding
    
def decode(S):
    

def apply_mask_encoded(M_e, T_e):
    

def q1_simple_tests():
    assert(apply_mask(I, J) == R)
    assert(encode(I) == 'B1W1B2W5')
    assert(encode(J) == 'B2W1B1W1B1W1B2')
    assert(decode('B1W1B2W5') == I)
    assert(apply_mask_encoded(encode(I), encode(J)) == encode(R))

