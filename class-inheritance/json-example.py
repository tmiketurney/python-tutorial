#!/usr/bin/env python3
#
#  @file    json-example.py
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

import json

length = 20.0
width = 15

outfile = open("datafile1.dat", "w")

json_string = json.dumps(length)
outfile.write(json_string+'\n')

json_string = json.dumps(width)
outfile.write(json_string+'\n')

json_string = json.dumps("Data for an example")
outfile.write(json_string+'\n')

outfile.close()

infile = open("datafile1.dat", "r")

json_string = infile.readline()
l = json.loads(json_string)

json_string = infile.readline()
w = json.loads(json_string)

json_string = infile.readline()
description = json.loads(json_string)

infile.close()

print(description)
print(l*w)
