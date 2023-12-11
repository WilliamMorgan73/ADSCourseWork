#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def Merge3Way(L1,L2,L3):
    """ Merge the three lists L1, L2, L3 that are sorted
    in non-increasing order into a new list L that is
    sorted in non-increasing order, and return L """
    
def Merge3Sort(L):
    """ If L has at most three elements, sort L into
    non-increasing order without recursive calls.
    Otherwise, make three recursive calls on sub-lists
    whose sizes differ by at most 1, and call Merge3Way
    to merge them. In either case, return a list
    that is a sorted version of L """
    
# Test for Merge3Way
L1 = [8,6,6,4]
L2 = [10,7,2,1]
L3 = [9,5,2]
assert(Merge3Way(L1,L2,L3)==[10,9,8,7,6,6,5,4,2,2,1])
print("Merge3Way test passed")

# Test for Merge3Sort
L = [5,19,14,13,2,8,5,19,6]
assert(Merge3Sort(L)==[19,19,14,13,8,6,5,5,2])
print("Merge3Sort test passed")

