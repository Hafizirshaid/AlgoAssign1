#
# Date: 21/09/2016
# Class: CS5310
# Assignment: Assignment 2
# Author(s): Hafez K.M Irshaid (hafezkm.irshaid@wmich.edu)
# Description:
#

from Stack import Stack
from Queue import Queue
from List import List


def test_queue(test_cases_size=50):

    print "######################## QUEUE TEST CASES ############################"
    my_queue = Queue()

    for i in range(0, test_cases_size):
        my_queue.enqueue("elm" + str(i))

    for i in range(0, test_cases_size):
        print "queue elements"
        my_queue.print_queue()
        print "first come first serve: " + str(my_queue.dequeue())


def test_stack(test_cases_size=50):

    print "######################## STACK TEST CASES ############################"
    my_stack = Stack()

    for i in range(0, test_cases_size):
        my_stack.push("elm" + str(i))

    for i in range(0, test_cases_size):
        my_stack.print_stack()
        print "the element to pop is: " + str(my_stack.pop())


def test_list(test_cases_size=50):

    print "######################## LIST TEST CASES ############################"
    my_list = List()

    for i in range(0, test_cases_size):
        my_list.add(i, "elm" + str(i))

    my_list.print_list()

    print my_list.get(0)


def main():
    test_queue()
    test_stack()
    test_list()

main()
