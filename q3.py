class HashTable():
    """Implements a simple hash table of size k, with all 
    empty entries denoted as '-' at initialisation.


    Set up your hashtable as follows, with some sensible integer value for k:
        h = HashTable(k)
    
    For a HashTable h:
        h.lookup(pos) returns the data in position pos.
        h.add(pos, data) adds data in position pos. 
        h.check(pos, table) checks that the current entries are equal to 
            table, which is represented as a list. This is only used for 
            testing that the hash table contains what we expect.
        h.print_table prints h.
    """
    def __init__(self, k):
        self.__table = ["-"] * k  
    def lookup(self, pos):
        return self.__table[pos]
    def add(self, pos, data):
        self.__table[pos] = data
    def check(self, table_of_data):
        return self.__table == table_of_data
    def print_table(self):
        print(self.__table)


def hash_quadratic(d):

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

    """
    Inserts keys from the list d into a hash table and returns the HashTable which contains the state of the hash table after these insertions.
    Uses quadratic probing (see question for details) to resolve collisions.
    """

def hash_double(d):
    """Inserts keys from the list d into a hash table and
    returns the HashTable which contains the state of the 
    hash table after these insertions.

    Use just one HashTable instance inside this function.
    
    Uses secondary hashing (see question for details) to resolve
    collisions.
    """

#Test casese
def test_hash_quadratic():
    assert hash_quadratic([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]).check([10, '-', 11, '-', 12, '-', 13, '-', 14, '-', 15, '-', 16, 1, 17, 2, 18, 3, 19, 4, '-', 5, '-', 6, '-', 7, '-', 8, '-', 9, '-'])
    assert hash_quadratic([31, 62, 93, 124, 155, 186, 217, 248, 279]).check(['-', '-', '-', '-', '-', 186, '-', '-', '-', '-', '-', 31, 62, 279, '-', 93, 217, '-', '-', '-', 124, '-', '-', '-', '-', '-', '-', 155, '-', 248, '-'])
    
    assert hash_quadratic([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113]).check(
        [41, 103, 11, 73, 43, 59, 13, 29, 107, 61, '-', 31, 47, 109, 17, 2, 83, 3, 19, 89, 97, 5, 67, 37, 53, 7, 23, 101, 113, 71, 79]
    )

def test_hash_double():
    assert hash_double([1]).check(['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', 1, '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'])
    assert hash_double([1, 2]).check(['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', 1, '-', 2, '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'])
    assert hash_double(list(range(31))).check([10,26,11,27,12,28,13,29,14,30,15,0,16,1,17,2,18,3,19,4,20,5,21,6,22,7,23,8,24,9,25])
