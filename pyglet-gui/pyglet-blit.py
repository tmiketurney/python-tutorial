#!/usr/bin/env python3
#
#  @file    pyglet-blit.py
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

window = pyglet.window.Window(width=400, height=500, caption="TestWindow")
Im1 = pyglet.image.load('turquoise-bucket.jpg')

label = pyglet.text.Label('Nothing pressed so far',
                            font_name='Times New Roman',
                            font_size=18,
                            x=50,
                            y=50)

@window.event
def on_mouse_motion(x, y, dx, dy):
    global label
    label = pyglet.text.Label('Mouse is at position ('+str(x)+', '+str(y)+')',
                              font_name='Times New Roman',
                              font_size=18,
                              x=50, y=50)

@window.event
def on_draw():
    window.clear()
    Im1.blit(100,100)
    label.draw()

pyglet.app.run()
