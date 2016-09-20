#
# Date: 21/09/2016
# Class: CS5310
# Assignment: Assignment 2
# Author(s): Hafez K.M Irshaid
# Description:
#


class Stack:

    def __init__(self, stack_size=10):
        self._size = stack_size
        self._pointer = 0
        self._stack = [None] * self._size

    def push(self, element):

        if self.is_full():
            print "hey, the array is full"
            return False

        self._stack[self._pointer] = element
        self._pointer += 1
        return True

    def pop(self):

        if self._pointer < 0:
            print "hey, the array is empty"
            return

        print self._pointer
        element_to_return = self._stack[self._pointer - 1]
        self._stack[self._pointer - 1] = None
        self._pointer -= 1

        return element_to_return

    def top(self):
        return self._stack[self._pointer]

    def size(self):
        return self._pointer

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

    def print_stack(self):
        print self._stack
