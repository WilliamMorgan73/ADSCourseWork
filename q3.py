def hash_quadratic(d):

    """
    Inserts keys from the list d into a hash table and returns the HashTable which contains the state of the hash table after these insertions.
    Uses quadratic probing (see question for details) to resolve collisions.
    """

    k = 31
    h = HashTable(k)

    for input in d:
        i = 0
        hashFunction = ((2 * input + 11) % k)

        if h.lookup(hashFunction) == "-":
            h.add(hashFunction, input)
        else:
            while h.lookup(hashFunction) != "-":
                hashFunction = (((2 * input + 11) + i**2) % k)
                i +=1
            h.add(hashFunction, input)

    return h


def hash_double(d):
    """
    Inserts keys from the list d into a hash table and returns the HashTable which contains the state of the hash table after these insertions.
    Uses secondary hashing to resolve collisions.
    """

    k = 31
    h = HashTable(k)

    for input in d:
        hashFunction = ((2 * input + 11) % k)
        
        if h.lookup(hashFunction) == "-":
            h.add(hashFunction, input)
        else:
            i = 1
            offset = (19 - (input % 19))
            while h.lookup(hashFunction) != "-":
                hashFunction = ((((2 * input + 11) % k) + i * offset) % 19)
                i += 1
            h.add(hashFunction, input)

    return h
