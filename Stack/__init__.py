#
# Date: 21/09/2016
# Class: CS5310
# Assignment: Assignment 2
# Author(s): Hafez K.M Irshaid (hafezkm.irshaid@wmich.edu)
#
# Description: This class represents a Stack data structure
#


class Stack:

    def __init__(self, stack_size=10):

        self._size = stack_size
        self._pointer = 0
        self._stack = [None] * self._size

    def expand_stack(self):

        new_size = self._size * 2
        new_stack = [None] * new_size

        for i in range(0, self._size):
            new_stack[i] = self._stack[i]

        self._stack = new_stack
        self._size = new_size

    def is_empty(self):

        is_empty = False
        if self._pointer == 0:
            is_empty = True

        return is_empty

    def is_full(self):

        is_full = False
        if self._size == self._pointer:
            is_full = True
        return is_full

    def top(self):
        return self._stack[self._pointer - 1]

    def size(self):
        return self._pointer

    def push(self, element):

        if self.is_full():
            self.expand_stack()
        self._stack[self._pointer] = element
        self._pointer += 1
        return True

    def pop(self):

        if self._pointer < 0:
            print "The stack is empty"
            return

        element_to_pop = self._stack[self._pointer - 1]
        self._stack[self._pointer - 1] = None
        self._pointer -= 1
        return element_to_pop

    def print_stack(self):
        print self._stack
