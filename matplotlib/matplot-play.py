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

from matplotlib.pyplot import plot, axis, show, legend

# main() starts here...
#######################
#if __name__ == '__main__':

#plot([0,1,2,3,4,5], [0,1,4,9,16,25])
#axis([0,5,0,25])
#show()

xlist = range(0,6)
ylist = []
ylist2 = []
for i in xlist:
    ylist.append(i*i)
    ylist2.append(i*i*i)

plot(xlist, ylist, label="squares", marker='+', color="red", markeredgecolor="blue")
plot(xlist, ylist2, label="cubes", marker="o", color="green", markeredgecolor="green")

axis([0,5,0,125])

legend()

show()
