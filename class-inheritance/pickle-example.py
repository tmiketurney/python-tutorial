#!/usr/bin/env python3
#
#  @file    pickle-example.py
#
#  COPYRIGHT:
#
#     Copyright: Tools Made Tough, 2016:
#
#     License:  GPL v2.1
#
#  @author   T.Michael Turney
#  @date     7.June.2016
#  @version  1.01
#

import pickle

account = 134218954
owner = "John Smith"
balance = 1783.45

# put into BankAccount.dat

outfile = open("BankAccount.dat", "wb")

pickle.dump(account, outfile)
pickle.dump(owner, outfile)
pickle.dump(balance, outfile)

outfile.close()

# read the data back in

infile = open("BankAccount.dat", "rb")

accountP = pickle.load(infile)
ownerP = pickle.load(infile)
balanceP = pickle.load(infile)

infile.close()

if account == accountP:
    print("Accounts DO match up")
else:
    print("Accounts don't match up")

if owner == ownerP:
    print("Owners DO match up")
else:
    print("Owners don't match up")

if balance == balanceP:
    print("Balances DO match up")
else:
    print("Balances don't match up")
