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

var family = [{
    "name" : "Jason",
    "age" : "24",
    "gender" : "male"
},
{
    "name" : "Kyle",
    "age" : "21",
    "gender" : "male"
}];

myfile = open("Filename", "w")

json_string = json.dumps(data)
myfile.write(json_string+'\n')

myfile.close()

myfile = open("Filename", "r")

json_string = myfile.readline()
data = json.loads(json_string)

myfile.close()
