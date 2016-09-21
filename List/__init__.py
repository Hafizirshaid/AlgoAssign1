#
# Date: 21/09/2016
# Class: CS5310
# Assignment: Assignment 2
# Author(s): Hafez K.M Irshaid (hafezkm.irshaid@wmich.edu)
#
# Description: This class represents a List data structure.
#


class List:

    def __init__(self, list_size=10):

        self._fixed_size = list_size
        self._actual_size = 0
        self._list = [None] * self._fixed_size

    def expand_list(self):
        new_size = self._fixed_size * 2

        new_list = [None] * new_size

        for i in range(0, self._actual_size):
            new_list[i] = self._list[i]

        self._list = new_list
        self._fixed_size = new_size

    def add(self, index, element):

        # TODO check if the index is in the range
        if self.is_full():
            self.expand_list()

        if index < self._actual_size:
            for i in range(self._actual_size - 1, index - 1, -1):
                self._list[i + 1] = self._list[i]

        self._list[index] = element
        self._actual_size += 1

    def remove(self, index):

        element_to_remove = self._list[index]

        if index < self._actual_size - 1:
            for i in range(index, self._actual_size - 1):
                self._list[i] = self._list[i + 1]

        self._actual_size -= 1
        return element_to_remove

    def get(self, index):

        if index > self._actual_size:
            print "index out of range"
            return
        return self._list[index]

    def set(self, index, element):

        if index > self._actual_size:
            print "index out of range"
            return
        self._list[index] = element

    def is_empty(self):

        if self._fixed_size == 0:
            return True
        return False

    def is_full(self):

        is_full = False
        if self._actual_size == self._fixed_size:
            is_full = True

        return is_full

    def print_list(self):

        list_str = "["

        for i in range(0, self._actual_size):
            list_str += str(self._list[i])
            if self._actual_size - 1 != i:
                list_str += ","
        list_str += "]"
        print list_str
