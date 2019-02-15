from sense_hat import SenseHat

class SenseDisplay():
    # Alexa Logo Blue
    _AB = (72, 198, 240)
    # Alexa Logo Grey
    _AG = (20, 20, 20)
    # Red
    _R = (255, 0, 0)
    # White
    _W = (255, 255, 255)
    # Pink
    _P = (255, 0, 255)
    # Black / Off
    _B = (0, 0, 0)

    _ALEXA_LOGO = [
        _AG, _AG, _AB, _AB, _AB, _AB, _AG, _AG,
        _AG, _AB, _AB, _AB, _AB, _AB, _AB, _AG,
        _AB, _AB, _AB, _AG, _AG, _AB, _AB, _AB,
        _AB, _AB, _AG, _AG, _AG, _AG, _AB, _AB,
        _AB, _AB, _AG, _AG, _AG, _AG, _AB, _AB,
        _AB, _AB, _AB, _AG, _AG, _AB, _AB, _AB,
        _AG, _AB, _AB, _AG, _AB, _AB, _AB, _AG,
        _AG, _AG, _AB, _AB, _AB, _AB, _AG, _AG
        ]

    _QUESTION_MARK = [
        _W, _W, _W, _R, _R, _W, _W, _W,
        _W, _W, _R, _W, _W, _R, _W, _W,
        _W, _W, _W, _W, _W, _R, _W, _W,
        _W, _W, _W, _W, _R, _W, _W, _W,
        _W, _W, _W, _R, _W, _W, _W, _W,
        _W, _W, _W, _R, _W, _W, _W, _W,
        _W, _W, _W, _W, _W, _W, _W, _W,
        _W, _W, _W, _R, _W, _W, _W, _W
        ]

    _AEI = [
        _B, _B, _B, _B, _B, _B, _B, _B,
        _B, _B, _B, _B, _B, _B, _B, _B,
        _R, _R, _R, _R, _R, _R, _R, _R,
        _R, _W, _W, _W, _W, _W, _W, _R,
        _R, _B, _B, _B, _B, _B, _B, _R,
        _B, _R, _P, _P, _P, _P, _R, _B,
        _B, _B, _R, _R, _R, _R, _B, _B,
        _B, _B, _B, _B, _B, _B, _B, _B
        ]

    _BMP = [
        _B, _B, _B, _B, _B, _B, _B, _B,
        _B, _B, _B, _B, _B, _B, _B, _B,
        _B, _B, _B, _B, _B, _B, _B, _B,
        _R, _R, _R, _R, _R, _R, _R, _R,
        _R, _R, _R, _R, _R, _R, _R, _R,
        _B, _B, _B, _B, _B, _B, _B, _B,
        _B, _B, _B, _B, _B, _B, _B, _B,
        _B, _B, _B, _B, _B, _B, _B, _B
        ]

    _CDGKNSTXYZ = [
        _B, _B, _B, _B, _B, _B, _B, _B,
        _B, _B, _B, _B, _B, _B, _B, _B,
        _R, _R, _R, _R, _R, _R, _R, _R,
        _R, _W, _W, _W, _W, _W, _W, _R,
        _R, _B, _B, _P, _P, _B, _B, _R,
        _B, _R, _W, _W, _W, _W, _R, _B,
        _B, _B, _R, _R, _R, _R, _B, _B,
        _B, _B, _B, _B, _B, _B, _B, _B
        ]

    _CHJSH = [
        _B, _B, _B, _B, _B, _B, _B, _B,
        _B, _B, _B, _B, _B, _B, _B, _B,
        _R, _R, _R, _R, _R, _R, _R, _R,
        _R, _W, _W, _W, _W, _W, _W, _R,
        _R, _B, _B, _B, _B, _B, _B, _R,
        _B, _R, _W, _W, _W, _W, _R, _B,
        _B, _B, _R, _R, _R, _R, _B, _B,
        _B, _B, _B, _B, _B, _B, _B, _B
        ]

    _FV = [
        _B, _B, _B, _B, _B, _B, _B, _B,
        _B, _B, _B, _B, _B, _B, _B, _B,
        _R, _R, _R, _R, _R, _R, _R, _R,
        _R, _W, _W, _W, _W, _W, _W, _R,
        _R, _B, _B, _B, _B, _B, _B, _R,
        _B, _R, _P, _P, _P, _P, _R, _B,
        _B, _B, _R, _R, _R, _R, _B, _B,
        _B, _B, _B, _B, _B, _B, _B, _B
        ]

    _OH = [
        _B, _B, _B, _B, _B, _B, _B, _B,
        _B, _B, _B, _B, _B, _B, _B, _B,
        _B, _B, _R, _R, _R, _R, _B, _B,
        _B, _R, _W, _W, _W, _W, _R, _B,
        _B, _R, _B, _B, _B, _B, _R, _B,
        _B, _R, _P, _P, _P, _P, _R, _B,
        _B, _B, _R, _R, _R, _R, _B, _B,
        _B, _B, _B, _B, _B, _B, _B, _B
        ]

    _QWOO = [
        _B, _B, _B, _B, _B, _B, _B, _B,
        _B, _B, _B, _B, _B, _B, _B, _B,
        _B, _B, _R, _R, _R, _R, _B, _B,
        _B, _R, _W, _W, _W, _W, _R, _B,
        _B, _R, _B, _B, _B, _B, _R, _B,
        _B, _R, _B, _B, _B, _B, _R, _B,
        _B, _B, _R, _R, _R, _R, _B, _B,
        _B, _B, _B, _B, _B, _B, _B, _B
        ]

    _RR = [
        _B, _B, _B, _B, _B, _B, _B, _B,
        _B, _B, _B, _B, _B, _B, _B, _B,
        _R, _R, _R, _R, _R, _R, _R, _R,
        _R, _W, _W, _W, _W, _W, _W, _R,
        _R, _B, _B, _B, _B, _B, _B, _R,
        _B, _R, _W, _W, _W, _W, _R, _B,
        _B, _B, _R, _R, _R, _R, _B, _B,
        _B, _B, _B, _B, _B, _B, _B, _B
        ]

    _TH = [
        _B, _B, _B, _B, _B, _B, _B, _B,
        _B, _B, _B, _B, _B, _B, _B, _B,
        _R, _R, _R, _R, _R, _R, _R, _R,
        _R, _W, _W, _W, _W, _W, _W, _R,
        _R, _B, _B, _P, _P, _B, _B, _R,
        _B, _R, _P, _P, _P, _P, _R, _B,
        _B, _B, _R, _R, _R, _R, _B, _B,
        _B, _B, _B, _B, _B, _B, _B, _B
        ]

    _VISEMES = {
        "@": _AEI,
        "a": _AEI,
        "e": _AEI,
        "E": _AEI,
        "i": _AEI,
        "p": _BMP,
        "sil": _BMP,
        "k": _CDGKNSTXYZ,
        "s": _CDGKNSTXYZ,
        "t": _CDGKNSTXYZ,
        "S": _CHJSH,
        "f": _FV,
        "o": _OH,
        "O": _QWOO,
        "u": _QWOO,
        "r": _RR,
        "T": _TH,
        "?": _QUESTION_MARK
        }

    def __init__(self):
        self.sense = SenseHat()

    def alexa_logo(self):
        self.sense.set_rotation(0)
        self.sense.set_pixels(self._ALEXA_LOGO)

    def clear(self):
        self.sense.clear()

    def message(self, message):
        self.sense.show_message(message)

    def speechmark(self, viseme):
        if viseme == "sil":
            self.sense.clear()
        elif viseme in self._VISEMES:
            self.sense.set_rotation(0)
            self.sense.set_pixels(self._VISEMES[viseme])
        else:
            self.sense.set_rotation(0)
            self.sense.set_pixels(self._VISEMES["?"])
