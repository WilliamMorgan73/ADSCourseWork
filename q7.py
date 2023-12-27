
def Merge3Way(L1,L2,L3):
    """ Merge the three lists L1, L2, L3 that are sorted
    in non-increasing order into a new list L that is
    sorted in non-increasing order, and return L """

    L = []

    while L1 or L2 or L3:
        # Get the minimum value among the current elements from L1, L2, and L3
        min_val = min(L1[-1] if L1 else float('inf'),
                      L2[-1] if L2 else float('inf'),
                      L3[-1] if L3 else float('inf'))

        # Append the minimum value to the L list
        L.append(min_val)

        # Pop the element from the list where the minimum value was found
        if L1 and min_val == L1[-1]:
            L1.pop()
        elif L2 and min_val == L2[-1]:
            L2.pop()
        elif L3 and min_val == L3[-1]:
            L3.pop()

    return L[::-1]



    
def Merge3Sort(L):
    """ If L has at most three elements, sort L into
    non-increasing order without recursive calls.
    Otherwise, make three recursive calls on sub-lists
    whose sizes differ by at most 1, and call Merge3Way
    to merge them. In either case, return a list
    that is a sorted version of L """
    
    
    if len(L) <= 3:
        # Base case: if L has at most three elements, sort it directly
        for i in range(1, len(L)):
            currentElement = L[i]
            j = i - 1
            while j >= 0 and currentElement > L[j]:
                L[j + 1] = L[j]
                j -= 1
            L[j + 1] = currentElement
        return L
    else:
        # Recursive case: split the list into three sub-lists
        length = len(L)
        marker1 = length // 3 # one third of the length
        marker2 = (2 * length) // 3 # two thirds of the length

        # Make three recursive calls on sub-lists
        L1 = Merge3Sort(L[:marker1]) # from 0 to marker1
        L2 = Merge3Sort(L[marker1:marker2]) # from marker1 to marker2
        L3 = Merge3Sort(L[marker2:]) # from marker2 to the end

        # Merge the three sorted sub-lists using Merge3Way
        return Merge3Way(L1, L2, L3)
    
