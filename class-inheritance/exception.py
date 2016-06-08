#!/usr/bin/env python3
#
#  @file    exception.py
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

def computeDivision(first, second):
    try:
        division = first/second
    except TypeError:
        print("You didn't enter two floating point numbers!")
    except ZeroDivisionError:
        print("Don't give a zero for the second number!")
    except:
        print("There was some other exception")
    else:
        return division
