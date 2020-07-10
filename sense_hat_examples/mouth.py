#!/usr/bin/env python3

from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

R = (255, 0, 0)
W = (255, 255, 255)
P = (255, 0, 255)
B = (0, 0, 0)

question_mark = [
    W, W, W, R, R, W, W, W,
    W, W, R, W, W, R, W, W,
    W, W, W, W, W, R, W, W,
    W, W, W, W, R, W, W, W,
    W, W, W, R, W, W, W, W,
    W, W, W, R, W, W, W, W,
    W, W, W, W, W, W, W, W,
    W, W, W, R, W, W, W, W
    ]

aei = [
    B, B, B, B, B, B, B, B,
    R, R, R, R, R, R, R, R,
    R, W, W, W, W, W, W, R,
    R, B, B, B, B, B, B, R,
    R, B, B, B, B, B, B, R,
    B, R, P, P, P, P, R, B,
    B, B, R, R, R, R, B, B,
    B, B, B, B, B, B, B, B
    ]

bmp = [
    B, B, B, B, B, B, B, B,
    B, B, B, B, B, B, B, B,
    B, B, B, B, B, B, B, B,
    R, R, R, R, R, R, R, R,
    R, R, R, R, R, R, R, R,
    B, B, B, B, B, B, B, B,
    B, B, B, B, B, B, B, B,
    B, B, B, B, B, B, B, B
    ]

cdgknstxyz = [
    B, B, B, B, B, B, B, B,
    R, R, R, R, R, R, R, R,
    R, W, W, W, W, W, W, R,
    R, B, B, B, B, B, B, R,
    R, B, B, P, P, B, B, R,
    B, R, W, W, W, W, R, B,
    B, B, R, R, R, R, B, B,
    B, B, B, B, B, B, B, B
    ]
chjsh = [
    B, B, B, B, B, B, B, B,
    R, R, R, R, R, R, R, R,
    R, W, W, W, W, W, W, R,
    R, B, B, B, B, B, B, R,
    R, B, B, B, B, B, B, R,
    B, R, W, W, W, W, R, B,
    B, B, R, R, R, R, B, B,
    B, B, B, B, B, B, B, B
    ]

fv = [
    B, B, B, B, B, B, B, B,
    R, R, R, R, R, R, R, R,
    R, W, W, W, W, W, W, R,
    R, B, B, B, B, B, B, R,
    R, B, B, B, B, B, B, R,
    B, R, P, P, P, P, R, B,
    B, B, R, R, R, R, B, B,
    B, B, B, B, B, B, B, B
    ]

o = [
    B, B, R, R, R, R, B, B,
    B, R, R, W, W, R, R, B,
    R, R, W, B, B, W, R, R,
    R, B, B, B, B, B, B, R,
    R, B, B, B, B, B, B, R,
    R, R, P, B, B, P, R, R,
    B, R, R, P, P, R, R, B,
    B, B, R, R, R, R, B, B
    ]

qwoo = [
    B, B, R, R, R, R, B, B,
    B, R, R, B, B, R, R, B,
    R, R, B, B, B, B, R, R,
    R, B, B, B, B, B, B, R,
    R, B, B, B, B, B, B, R,
    R, R, P, B, B, P, R, R,
    B, R, R, P, P, R, R, B,
    B, B, R, R, R, R, B, B
    ]

r = [
    B, B, B, B, B, B, B, B,
    R, R, R, R, R, R, R, R,
    R, W, W, W, W, W, W, R,
    R, B, B, B, B, B, B, R,
    B, R, W, W, W, W, R, B,
    B, B, R, R, R, R, B, B,
    B, B, B, B, B, B, B, B,
    B, B, B, B, B, B, B, B
    ]

th = [
    B, B, B, B, B, B, B, B,
    R, R, R, R, R, R, R, R,
    R, W, W, W, W, W, W, R,
    R, B, B, P, P, B, B, R,
    B, R, P, P, P, P, R, B,
    B, B, R, R, R, R, B, B,
    B, B, B, B, B, B, B, B,
    B, B, B, B, B, B, B, B
    ]

visemes = {
    "@": aei,
    "a": aei,
    "e": aei,
    "E": aei,
    "i": aei,
    "p": bmp,
    "sil": bmp,
    "k": cdgknstxyz,
    "s": cdgknstxyz,
    "t": cdgknstxyz,
    "S": chjsh,
    "f": fv,
    "o": o,
    "O": qwoo,
    "u": qwoo,
    "r": r,
    "t": th
}

sense.set_pixels(question_mark)
sleep(1)
sense.set_pixels(visemes["@"])
sleep(1)
sense.set_pixels(visemes["p"])
sleep(1)
sense.set_pixels(visemes["k"])
sleep(1)
sense.set_pixels(visemes["S"])
sleep(1)
sense.set_pixels(visemes["f"])
sleep(1)
sense.set_pixels(visemes["o"])
sleep(1)
sense.set_pixels(visemes["O"])
sleep(1)
sense.set_pixels(visemes["r"])
sleep(1)
sense.set_pixels(visemes["t"])

