#!/usr/bin/env python3

from sense_hat import SenseHat

sense = SenseHat()

red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
white = (255, 255, 255)
yellow = (255, 255, 0)

sense.show_message("Hello world!", text_colour=red, back_colour=blue, scroll_speed=.06)
sense.clear()

