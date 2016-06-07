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

from datetime import date

class BankAccount:

    def __init__(self, initial_amount=0.0):
        self._balance = initial_amount
        self._deposits = []
        self.opendate = date(2011, 3, 15)

    def makeDeposit(self, amount):
        self._balance += amount
        self._deposits.append(amount)

    def makeWithdrawal(self, amount):
        self._balance -= amount

    def getBalance(self):
        return self._balance

    def getDeposits(self):
        copied_list = self._deposits[:]
        return copied_list

def winLottery(account):
    account.makeDeposit(10000000.00)

checking_account = BankAccount()
winLottery(checking_account)

print(checking_account.getBalance())
print(checking_account.getDeposits())
print(checking_account.opendate)
