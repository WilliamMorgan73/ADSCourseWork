class LLStack:
    """
    Implements a stack using a singly-linked list.
    """

    class _Node:
        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        """
        Returns the length of the stack
        """
        return self._size

    def is_empty(self):
        """
        Returns whether the stack is empty
        """
        return self._size == 0

    def push(self, e):
        """
        Adds a new value to the stack
        """
        newest = self._Node(e, self._head)
        if newest == self._size:
            raise Exception("Stack is full")
        else:
            self._head = newest
            self._size += 1
        

    def top(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        
        return self._head._element

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        
        return answer

class ModStack:
    """
    Implements a stack
    """

    class _Node:
        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        """
        Returns the length of the stack
        """
        return self._size

    def is_empty(self):
        """
        Returns whether the stack is empty
        """
        return self._size == 0

    def push(self, e):
        """
        Adds a new value to the stack
        """
        newest = self._Node(e, self._head)
        if newest == self._size:
            raise Exception("Stack is full")
        else:
            self._head = newest
            self._size += 1

    def smallest(self):
        """
        Returns the smallest value on the stack
        """
        