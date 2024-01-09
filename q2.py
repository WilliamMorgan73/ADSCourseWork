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
        """
        Returns the element at the top of the stack
        """
        if self.is_empty():
            raise Exception("Stack is empty")
        
        return self._head._element

    def pop(self):
        """
        Removes the element at the top of the stack
        """
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

    def top(self):
        """
        Returns the element at the top of the stack
        """
        if self.is_empty():
            raise Exception("Stack is empty")
        
        return self._head._element

    def pop(self):
        """
        Removes the element at the top of the stack
        """
        if self.is_empty():
            raise Exception("Stack is empty")
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        
        return answer
    

    def smallest(self):
        """
        Returns the smallest value on the stack
        """
        if self.is_empty():
            raise Exception("Stack is empty")

        current = self._head
        min_val = current._element

        while current:
            min_val = min(min_val, current._element)
            current = current._next

        return min_val
    

def reverse(queue):
    """
    Reverses a queue using a stack
    To do so, dequeue elements from a queue, and push them into a stack and then enqueue them to a new queue
    """
    
    stack = LLStack()
    reverseQueue = LLQueue()
    
    #Dequeue elements and push them onto a stack
    while not queue.is_empty():
        stack.push(queue.dequeue())
    
    #Add them to the back of the reverse queue
    while not stack.is_empty():
        reverseQueue.enqueue(stack.pop())
        
    return reverseQueue

