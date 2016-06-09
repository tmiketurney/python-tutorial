#!/usr/bin/env python3
#
#  @file    queue.py
#
#  COPYRIGHT:
#
#     Copyright: Tools Made Tough, 2016:
#
#     License:  GPL v2.1
#
#  @author   T.Michael Turney
#  @date     8.June.2016
#  @version  1.01
#

import random

class Queue:
    _queue = []

    def enqueue(self, item):
        self._queue.append(item)

    def dequeue(self):
        return self._queue.pop(0)

    def isEmpty(self):
        return (len(self._queue) == 0)

class Order:
    def __init__(self, customer="", amt=0):
        self._customer = customer
        self._amount = amt

    def customer(self):
        return self._customer

    def numOrdered(self):
        return self._amount

orders = Queue()

for ordernum in range(20):
    amount = random.randint(1,200)
    customer = "Customer "+str(ordernum)
    neworder = Order(customer, amount)
    orders.enqueue(neworder)

inventory = 1000

while not orders.isEmpty():
    order = orders.dequeue()
    if order.numOrdered() < inventory:
        # We can fill the order
        print("Fill order for ", order.numOrdered(), "shrubberies for customer:", order.customer())
        inventory -= order.numOrdered()
    else:
        print("Notify ", order.customer(), "that we cannot fulfill the order")

exit()
