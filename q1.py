#!/usr/bin/env python
# coding: utf-8

# In[20]:


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


# In[21]:


def q1_simple_tests():
    assert(apply_mask(I, J) == R)
    assert(encode(I) == 'B1W1B2W5')
    assert(encode(J) == 'B2W1B1W1B1W1B2')
    assert(decode('B1W1B2W5') == I)
    assert(apply_mask_encoded(encode(I), encode(J)) == encode(R))

