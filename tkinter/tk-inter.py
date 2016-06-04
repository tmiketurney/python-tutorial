#!/usr/bin/env python3
#
#  @file    tkinter.py
#
#  COPYRIGHT:
#
#     Copyright: Tools Made Tough, 2016:
#
#     License:  GPL v2.1
#
#  @author   T.Michael Turney
#  @date     4.June.2016
#  @version  1.01
#

import tkinter

class Application(tkinter.Frame):
    def __init__(self, master=None):
        tkinter.Frame.__init__(self, master)
        self.pack()

        self.increase_button = tkinter.Button(self)
        self.increase_button["text"] = "Increase"
        self.increase_button["command"] = self.increase_value
        self.increase_button.pack(side="right")

        self.decrease_button = tkinter.Button(self)
        self.decrease_button["text"] = "Decrease"
        self.decrease_button["command"] = self.decrease_value
        self.decrease_button.pack(side="left")

    def increase_value(self):
        global mainval
        mainval *= 2
        print(mainval)

    def decrease_value(self):
        global mainval
        mainval /= 2
        print(mainval)

mainval = 1.0

# main() starts here...
#######################

root = tkinter.Tk()
app = Application(master=root)
app.mainloop()
