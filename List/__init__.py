#
# Date: 21/09/2016
# Class: CS5310
# Assignment: Assignment 2
# Author(s): Hafez K.M Irshaid
# Description:
#


class List:

    def __init__(self, list_size=10):

        self._fixed_size = list_size
        self._actual_size = 0
        self._list = [None] * self._fixed_size

    def add(self, index, element):

        if self.is_full():
            print "list is full"
            return

        if index < self._actual_size:
            self.shift_list_to_left(index)
        self._list[index] = element
        self._actual_size += 1
        return

    def remove(self, index):

        print index
        print "remove method"
        element_to_remove = self._list[index]

        print "the element that is removed is: " + element_to_remove
        # self._list[index] = None

        if index < self._actual_size - 1:
            self.shift_list_to_right(index)
        self._actual_size -= 1
        return element_to_remove

    def get(self, index):
        return self._list[index]

    def set(self, index, element):
        self._list[index] = element

    def is_empty(self):

        print "is empty"
        if self._fixed_size == 0:
            return True
        return False

    def is_full(self):

        is_full = False
        if self._actual_size == self._fixed_size:
            is_full = True

        return is_full

    def shift_list_to_left(self, index):
        print "here im gonna shift them to new size to : "
        print index
        for i in range(self._actual_size - 1, index, -1):
            self._list[i + 1] = self._list[i]

    def shift_list_to_right(self, index):

        print "here im gonna shift them to new size to : "
        print index

        for i in range(index, self._actual_size - 2):
            self._list[i] = self._list[i + 1]

    def print_list(self):
        print self._list[0 : self._actual_size + 1]
