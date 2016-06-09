#!/usr/bin/env python3
#
#  @file    dictionary.py
#
#  COPYRIGHT:
#
#     Copyright: Tools Made Tough, 2016:
#
#     License:  GPL v2.1
#
#  @author   T.Michael Turney
#  @date     9.June.2016
#  @version  1.01
#

nicknames = {}

nicknames["Superstar"] = "Sue Smith"
nicknames["CowboysFan"] = "Bill Brown"
nicknames["JJwins"] = "John James"

for nickname in nicknames:
    print("The nickname for "+nicknames[nickname]+" is "+nickname)
