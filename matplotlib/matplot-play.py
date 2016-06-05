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

from matplotlib.pyplot import plot, axis, show

# main() starts here...
#######################
#if __name__ == '__main__':

#plot([0,1,2,3,4,5], [0,1,4,9,16,25])
#axis([0,5,0,25])
#show()

xlist = range(0,6)
ylist = []
for i in xlist:
    ylist.append(i*i)

plot(xlist, ylist)
axis([0,5,0,25])
show()
