#!/usr/bin/env python3
#
#  @file    pyglet-keypress.py
#
#  COPYRIGHT:
#
#     Copyright: Tools Made Tough, 2016:
#
#     License:  GPL v2.1
#
#  @author   T.Michael Turney
#  @date     3.June.2016
#  @version  1.01
#

import pyglet
from pyglet.window import key

window = pyglet.window.Window(width=400, height=300, caption="TestWindow")

label = pyglet.text.Label('Nothing pressed so far',
                            font_name='Times New Roman',
                            font_size=18,
                            x=50,
                            y=150)

@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.A:
        key_pressed = "a"
    elif symbol == key.RETURN:
        key_pressed = "return"
    elif symbol == key.LEFT:
        key_pressed = "left arrow"
    else:
        key_pressed = "unknown"
    global label
    label = pyglet.text.Label('You pressed the '+key_pressed+' key!',
                              font_name='Times New Roman',
                              font_size=18,
                              x=50, y=150)

@window.event
def on_draw():
    window.clear()
    label.draw()

pyglet.app.run()
