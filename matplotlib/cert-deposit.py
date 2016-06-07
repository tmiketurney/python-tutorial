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

from matplotlib.pyplot import plot, show

# set initial conditions
time = 0
balance = 1000

# set list to store data
timelist=[time]
balancelist=[balance]

# main() starts here...
#######################
#if __name__ == '__main__':

while (time < 10):
    # Increase balance and time
    balance += balance*0.03
    time += 1

    # Store time and balance in lists
    timelist.append(time)
    balancelist.append(balance)

# Output the simulation results
for i in range(len(timelist)):
    print("Year:", timelist[i], "  Balance:", balancelist[i])

plot(timelist, balancelist)
show()
