#!/usr/bin/env python3
#
#  @file    bankaccount.py
#
#  COPYRIGHT:
#
#     Copyright: Tools Made Tough, 2016:
#
#     License:  GPL v2.1
#
#  @author   T.Michael Turney
#  @date     2.June.2016
#  @version  1.02
#

class BankAccount:

    def __init__(self, initial_amount=0.0):
        self._balance = initial_amount
        self._deposits = []

    def makeDeposit(self, amount):
        self._balance += amount
        self._deposits.append(amount)

    def makeWithdrawal(self, amount):
        self._balance -= amount

    def getBalance(self):
        return self._balance

    def getDeposits(self):
        return self._deposits

checking_account = BankAccount(100.00)
checking_account.makeDeposit(50)
checking_account.makeWithdrawal(70.00)

print(checking_account.getBalance())
print(checking_account.getDeposits())
