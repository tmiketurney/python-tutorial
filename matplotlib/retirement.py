#!/usr/bin/env python3
#
#  @file    retirement.py
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
import statistics
from matplotlib.pyplot import hist, show

historical_stock_returns = [.1348, .3215, .1589, .0210, .1482, .2594, -.3655, .0548, .1561,
                            .0483, .1074, .2836, -.2197, -.1185, -.0903, .2089, .2834, .3310, .2268,
                            .3720, .0133, .0997, .0749, .3023, -.0306, .3148, .1654, .0581, .1849,
                            .3124, .0615, .2234, .2042, -.0470, .3174, .1852, .0651, -.0698, .2383,
                            .3700, -.2590, -.1431, .1876, .1422, .0356, -.0824, .1081, .2380, -.0997,
                            .1240, .1462, .2261, -.0881, .2664, .0034, .1206, .4372, -.1046, .0744,
                            .3260, .5256, -.0121, .1815, .2368, .3081, 1830, .0570, .0520, -.0843]

historical_bond_performance = [-.0202, .0422, .0784, .0654, .0593, .0524, .0697, .0433,
                               .0243, .0434, .0410, .1026, .0843, .1163, -.0082, .0870, .0964, .0364,
                               .1846, -.0292, .0975, .0740, .1600, .0896, .1453, .0789, .0275, .1530,
                               .2213, .1515, .0819, .3265, .0626, .2711, .2345]

historical_inflation = [.0, .016, .015, .021, .032, .016, -.004, .038, .028, .032,
                        .034, .027, .023, .016, .028, .034, .022, .016, .023, .030,
                        .028, .026, .030, .030, .042, .054, .048, .041, .036, .019,
                        .036, .043, .032, .062, .103, .135, .113, .076, .065, .058,
                        .091, .110, .062, .032, .044, .057, .055, .042, .031, .029,
                        .016, .013, .013, .010, .010, .017, .007, .028, .033, .015,
                        -.004, .007, .008, .019, .079, .013, -.012, .081, .144, .083]

def YearData():
    ''' Returns a rate of change for stocks, bonds, and inflation in a single tuple '''
    year = random.randrange(35)
    return(historical_stock_returns[year], historical_bond_performance[year], historical_inflation[year])

# Get information from user
initial_balance = float(input("What is your retirement account balance? "))
initial_expenses = float(input("What are your yearly expenses? "))
time_to_last = int(input("How many years does this need to last? "))

number_sims = 10000
final_balances = []
ran_out = 0                     # will count how many times the money ran out
stock_percentage = 0.5

for i in range(number_sims):
    # set initial conditions
    time=0
    balance_stocks = initial_balance * stock_percentage
    balance_bonds = initial_balance * (1.0-stock_percentage)
    expenses = initial_expenses

    while (time < time_to_last):
        # Increase balance and time
        time += 1
        stock_perform, bond_perform, inflation = YearData()
        balance_stocks *= (1.0+stock_perform)
        balance_bonds *= (1.0+bond_perform)

        # Reblance account
        balance_mixed = balance_stocks + balance_bonds
        target_stocks = balance_mixed * stock_percentage
        amount_to_move = balance_stocks - target_stocks
        balance_stocks -= amount_to_move
        balance_bonds += amount_to_move

        # Remove this year's expenses, which increase by inflation
        expenses *= (1.0+inflation)
        balance_stocks -= expenses * stock_percentage
        balance_bonds -= expenses * (1.0-stock_percentage)

        if (balance_stocks < 0):
            # We rean out of money! Increase ran_out count and set time to time_to_last to stop loop
            ran_out += 1
            time = time_to_last

    if (balance_stocks > 0):
        # The money lasted - save the final balance information
        final_balances.append(balance_stocks+balance_bonds)

percent_successful = (number_sims - ran_out)/number_sims * 100
final_balance_average = statistics.mean(final_balances)
final_balance_standard_deviation = statistics.stdev(final_balances)

print("The money lasted ", percent_successful, " percent of the time")
print("The average final balance when the money lasted was ", final_balance_average)
print("The standard deviation in the final balance when the money lasted was ", final_balance_standard_deviation)

# Output the simulation results
hist(final_balances, bins=20)
show()
