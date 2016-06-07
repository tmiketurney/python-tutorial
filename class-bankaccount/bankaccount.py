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
    balance = 0.0
    deposits = []

checking_account = BankAccount()
checking_account.deposits = []
savings_account = BankAccount()

checking_account.deposits.append(100.00)

print(savings_account.deposits)

