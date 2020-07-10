#!/usr/bin/env python3

from sense_hat import SenseHat

sense = SenseHat()

red = (255, 0, 0)

while True:
    acceleration = sense.get_accelerometer_raw()
    x = acceleration['x']
    y = acceleration['y']
    z = acceleration['z']

    x = abs(x)
    y = abs(y)
    z = abs(z)

    #print('{0} {1} {2}'.format(x,y,z))

    if x > 1.2 or y > 1.2 or z > 1.2:
        sense.show_letter("!", red)
    else:
        sense.clear()
