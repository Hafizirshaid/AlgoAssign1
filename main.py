#
# Date: 21/09/2016
# Class: CS5310
# Assignment: Assignment 2
# Author(s): Hafez K.M Irshaid
# Description:
#


from Stack import Stack
from Queue import Queue
from List import List


def test_queue():

    my_queue = Queue(10)

    for i in range(0, 10):
        my_queue.enqueue("elm" + str(i))

    for i in range(0, 10):
        print ",,,,,,,,,,,,,,,,"
        print "queue elements"
        my_queue.print_queue()
        print "first come first serve: " + str(my_queue.dequeue())


def test_stack():

    my_stack = Stack()

    for i in range(0, 10):
        my_stack.push("elm" + str(i))

    for i in range(0, 13):
        print ",,,,,,,,,,,,,,,,,,,,,,,,,,,"
        print "stack elements:"
        my_stack.print_stack()
        print "the element to pop is: " + str(my_stack.pop())


def test_list():

    my_list = List()

    for i in range(0, 10):
        my_list.add(i, "elm" + str(i))

    for i in range(0, 10):
        print my_list.get(i)

    for i in range(0, 10):
        print my_list.remove(i)
        my_list.print_list()


def main():
    # test_stack()
    test_list()
    # test_queue()

main()
