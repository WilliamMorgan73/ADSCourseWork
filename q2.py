#!/usr/bin/env python
# coding: utf-8

# In[9]:


class LLStack:
    """
    Implements a stack using a singly-linked list.

    Example usage:

      mystack = LLStack()
      mystack.push(3)

    Please note that this implementation is incorrect/incomplete 
    and you are expected to modify it and include it in your 
    submission (see question).
    """

    class _Node:
        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def push(self, e):
        raise NotImplementedError

    def top(self):
        return self._head._element

    def pop(self):
        if self.is_empty():
            raise Exception
        self._head = self._head._next
        self._size -= 1
        answer = self._head._element

        return answer


class LLQueue:
    """
    Implements a queue using a singly-linked list.

    Example usage:

      myqueue = LLQueue()
      myqueue.enqueue(3)

    You must not modify this implementation or include 
    it in your submission.
    """

    class _Node:
        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def front(self):
        if self.is_empty():
            raise Exception

        return self._head._element

    def dequeue(self):
        if self.is_empty():
            raise Exception
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return answer

    def enqueue(self, e):
        newest = self._Node(e, None)
        if self.is_empty():
            self._head = newest
        else:
            self._tail._next = newest
        self._tail = newest
        self._size += 1

