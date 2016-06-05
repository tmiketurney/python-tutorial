#!/usr/bin/env python3
#
#  @file    matplot-play.py
#
#  COPYRIGHT:
#
#     Copyright: Tools Made Tough, 2016:
#
#     License:  GPL v2.1
#
#  @author   T.Michael Turney
#  @date     5.June.2016
#  @version  1.01
#

import random
from matplotlib.pyplot import hist, show

def ChangeInBalance(initial_balance):
    rate = random.gauss(0.03, 0.02)
    return initial_balance*rate

number_years = 10
number_sims = 10000
final_balances = []

for i in range(number_sims):
    # set initial conditions
    time=0
    balance=1000

    while (time < number_years):
        # Increase balance and time
        balance += ChangeInBalance(balance)
        time += 1

    # Store time and balance in lists
    final_balances.append(balance)

# Output the simulation results
hist(final_balances, bins=20)
show()
