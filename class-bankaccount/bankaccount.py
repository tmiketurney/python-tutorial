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
        self.balance = initial_amount
        self.deposits = []

    def makeDeposit(self, amount):
        self.balance += amount
        self.deposits.append(amount)

    def makeWithdrawal(self, amount):
        self.balance -= amount

checking_account = BankAccount(100.00)
checking_account.makeDeposit(50)
checking_account.makeWithdrawal(70.00)

print(checking_account.balance)
print(checking_account.deposits)
