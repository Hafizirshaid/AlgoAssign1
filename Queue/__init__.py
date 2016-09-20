#
# Date: 21/09/2016
# Class: CS5310
# Assignment: Assignment 2
# Author(s): Hafez K.M Irshaid
# Description:
#


class Queue:

    def __init__(self, queue_size=10):
        self._size = queue_size
        self._queue = [None] * self._size
        self._front = 0
        self._rear = 0

    def enqueue(self, element):

        if self.is_full():
            print "queue is full, return"
            return
        # self._queue.insert(self._rear, element)
        self._queue[self._rear] = element
        self._rear = (self._rear + 1) % self._size

    def dequeue(self):

        if self.is_empty():
            print "the queue is empty, no more elements"
            return

        element_to_dequeue = self._queue[self._front]
        self._queue[self._front] = None
        self._front = (self._front + 1) % self._size

        return element_to_dequeue

    def first(self):
        return self._queue[self._front]

    def size(self):
        return self._size

    def is_empty(self):

        is_empty = False
        if self._rear == self._front:
            is_empty = True
        return is_empty

    def is_full(self):

        is_full = False
        if (self._size - self._front + self._rear) % self._size == self._size - 1:
            is_full = True
        return is_full

    def print_queue(self):
        print self._queue
