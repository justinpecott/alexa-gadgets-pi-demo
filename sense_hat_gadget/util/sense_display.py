from sense_hat import SenseHat
from time import sleep

class SenseDisplay():
    # Alexa Logo Blue
    _AB = (72, 198, 240)
    # Alexa Logo Grey
    _AG = (20, 20, 20)
    # Red
    _RD = (255, 0, 0)
    # White
    _WH = (255, 255, 255)
    # Pink
    _PK = (255, 0, 255)
    # Black / Off
    _BK = (0, 0, 0)
    # Green
    _GR = (0, 255, 0)

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

    _ALARM = [
        _RD, _RD, _RD, _RD, _RD, _RD, _RD, _RD,
        _RD, _WH, _WH, _WH, _WH, _WH, _WH, _RD,
        _RD, _WH, _RD, _RD, _RD, _RD, _WH, _RD,
        _RD, _WH, _RD, _WH, _WH, _RD, _WH, _RD,
        _RD, _WH, _RD, _RD, _RD, _RD, _WH, _RD,
        _RD, _WH, _RD, _WH, _WH, _RD, _WH, _RD,
        _RD, _WH, _WH, _WH, _WH, _WH, _WH, _RD,
        _RD, _RD, _RD, _RD, _RD, _RD, _RD, _RD
        ]

    _ALARM_ALT = [
        _WH, _WH, _WH, _WH, _WH, _WH, _WH, _WH,
        _WH, _RD, _RD, _RD, _RD, _RD, _RD, _WH,
        _WH, _RD, _WH, _WH, _WH, _WH, _RD, _WH,
        _WH, _RD, _WH, _RD, _RD, _WH, _RD, _WH,
        _WH, _RD, _WH, _WH, _WH, _WH, _RD, _WH,
        _WH, _RD, _WH, _RD, _RD, _WH, _RD, _WH,
        _WH, _RD, _RD, _RD, _RD, _RD, _RD, _WH,
        _WH, _WH, _WH, _WH, _WH, _WH, _WH, _WH
        ]

    _ALARM_CLEAR = [
        _RD, _RD, _RD, _RD, _RD, _RD, _RD, _RD,
        _RD, _WH, _WH, _WH, _WH, _WH, _GR, _RD,
        _RD, _WH, _RD, _RD, _RD, _GR, _WH, _RD,
        _RD, _WH, _RD, _WH, _WH, _GR, _WH, _RD,
        _RD, _GR, _RD, _RD, _GR, _RD, _WH, _RD,
        _RD, _WH, _GR, _WH, _GR, _RD, _WH, _RD,
        _RD, _WH, _WH, _GR, _WH, _WH, _WH, _RD,
        _RD, _RD, _RD, _RD, _RD, _RD, _RD, _RD
        ]

    _QUESTION_MARK = [
        _WH, _WH, _WH, _RD, _RD, _WH, _WH, _WH,
        _WH, _WH, _RD, _WH, _WH, _RD, _WH, _WH,
        _WH, _WH, _WH, _WH, _WH, _RD, _WH, _WH,
        _WH, _WH, _WH, _WH, _RD, _WH, _WH, _WH,
        _WH, _WH, _WH, _RD, _WH, _WH, _WH, _WH,
        _WH, _WH, _WH, _RD, _WH, _WH, _WH, _WH,
        _WH, _WH, _WH, _WH, _WH, _WH, _WH, _WH,
        _WH, _WH, _WH, _RD, _WH, _WH, _WH, _WH
        ]

    _AEI = [
        _BK, _BK, _BK, _BK, _BK, _BK, _BK, _BK,
        _BK, _BK, _BK, _BK, _BK, _BK, _BK, _BK,
        _RD, _RD, _RD, _RD, _RD, _RD, _RD, _RD,
        _RD, _WH, _WH, _WH, _WH, _WH, _WH, _RD,
        _RD, _BK, _BK, _BK, _BK, _BK, _BK, _RD,
        _BK, _RD, _PK, _PK, _PK, _PK, _RD, _BK,
        _BK, _BK, _RD, _RD, _RD, _RD, _BK, _BK,
        _BK, _BK, _BK, _BK, _BK, _BK, _BK, _BK
        ]

    _BMP = [
        _BK, _BK, _BK, _BK, _BK, _BK, _BK, _BK,
        _BK, _BK, _BK, _BK, _BK, _BK, _BK, _BK,
        _BK, _BK, _BK, _BK, _BK, _BK, _BK, _BK,
        _RD, _RD, _RD, _RD, _RD, _RD, _RD, _RD,
        _RD, _RD, _RD, _RD, _RD, _RD, _RD, _RD,
        _BK, _BK, _BK, _BK, _BK, _BK, _BK, _BK,
        _BK, _BK, _BK, _BK, _BK, _BK, _BK, _BK,
        _BK, _BK, _BK, _BK, _BK, _BK, _BK, _BK
        ]

    _CDGKNSTXYZ = [
        _BK, _BK, _BK, _BK, _BK, _BK, _BK, _BK,
        _BK, _BK, _BK, _BK, _BK, _BK, _BK, _BK,
        _RD, _RD, _RD, _RD, _RD, _RD, _RD, _RD,
        _RD, _WH, _WH, _WH, _WH, _WH, _WH, _RD,
        _RD, _BK, _BK, _PK, _PK, _BK, _BK, _RD,
        _BK, _RD, _WH, _WH, _WH, _WH, _RD, _BK,
        _BK, _BK, _RD, _RD, _RD, _RD, _BK, _BK,
        _BK, _BK, _BK, _BK, _BK, _BK, _BK, _BK
        ]

    _CHJSH = [
        _BK, _BK, _BK, _BK, _BK, _BK, _BK, _BK,
        _BK, _BK, _BK, _BK, _BK, _BK, _BK, _BK,
        _RD, _RD, _RD, _RD, _RD, _RD, _RD, _RD,
        _RD, _WH, _WH, _WH, _WH, _WH, _WH, _RD,
        _RD, _BK, _BK, _BK, _BK, _BK, _BK, _RD,
        _BK, _RD, _WH, _WH, _WH, _WH, _RD, _BK,
        _BK, _BK, _RD, _RD, _RD, _RD, _BK, _BK,
        _BK, _BK, _BK, _BK, _BK, _BK, _BK, _BK
        ]

    _FV = [
        _BK, _BK, _BK, _BK, _BK, _BK, _BK, _BK,
        _BK, _BK, _BK, _BK, _BK, _BK, _BK, _BK,
        _RD, _RD, _RD, _RD, _RD, _RD, _RD, _RD,
        _RD, _WH, _WH, _WH, _WH, _WH, _WH, _RD,
        _RD, _BK, _BK, _BK, _BK, _BK, _BK, _RD,
        _BK, _RD, _PK, _PK, _PK, _PK, _RD, _BK,
        _BK, _BK, _RD, _RD, _RD, _RD, _BK, _BK,
        _BK, _BK, _BK, _BK, _BK, _BK, _BK, _BK
        ]

    _O = [
        _BK, _BK, _BK, _BK, _BK, _BK, _BK, _BK,
        _BK, _BK, _BK, _BK, _BK, _BK, _BK, _BK,
        _BK, _BK, _RD, _RD, _RD, _RD, _BK, _BK,
        _BK, _RD, _WH, _WH, _WH, _WH, _RD, _BK,
        _BK, _RD, _BK, _BK, _BK, _BK, _RD, _BK,
        _BK, _RD, _PK, _PK, _PK, _PK, _RD, _BK,
        _BK, _BK, _RD, _RD, _RD, _RD, _BK, _BK,
        _BK, _BK, _BK, _BK, _BK, _BK, _BK, _BK
        ]

    _QWOO = [
        _BK, _BK, _BK, _BK, _BK, _BK, _BK, _BK,
        _BK, _BK, _BK, _BK, _BK, _BK, _BK, _BK,
        _BK, _BK, _RD, _RD, _RD, _RD, _BK, _BK,
        _BK, _RD, _WH, _WH, _WH, _WH, _RD, _BK,
        _BK, _RD, _BK, _BK, _BK, _BK, _RD, _BK,
        _BK, _RD, _BK, _BK, _BK, _BK, _RD, _BK,
        _BK, _BK, _RD, _RD, _RD, _RD, _BK, _BK,
        _BK, _BK, _BK, _BK, _BK, _BK, _BK, _BK
        ]

    _R = [
        _BK, _BK, _BK, _BK, _BK, _BK, _BK, _BK,
        _BK, _BK, _BK, _BK, _BK, _BK, _BK, _BK,
        _RD, _RD, _RD, _RD, _RD, _RD, _RD, _RD,
        _RD, _WH, _WH, _WH, _WH, _WH, _WH, _RD,
        _RD, _BK, _BK, _BK, _BK, _BK, _BK, _RD,
        _BK, _RD, _WH, _WH, _WH, _WH, _RD, _BK,
        _BK, _BK, _RD, _RD, _RD, _RD, _BK, _BK,
        _BK, _BK, _BK, _BK, _BK, _BK, _BK, _BK
        ]

    _TH = [
        _BK, _BK, _BK, _BK, _BK, _BK, _BK, _BK,
        _BK, _BK, _BK, _BK, _BK, _BK, _BK, _BK,
        _RD, _RD, _RD, _RD, _RD, _RD, _RD, _RD,
        _RD, _WH, _WH, _WH, _WH, _WH, _WH, _RD,
        _RD, _BK, _BK, _PK, _PK, _BK, _BK, _RD,
        _BK, _RD, _PK, _PK, _PK, _PK, _RD, _BK,
        _BK, _BK, _RD, _RD, _RD, _RD, _BK, _BK,
        _BK, _BK, _BK, _BK, _BK, _BK, _BK, _BK
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
        "o": _O,
        "O": _QWOO,
        "u": _QWOO,
        "r": _R,
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

    def set_alarm(self):
        self.sense.set_rotation(0)
        self.sense.set_pixels(self._ALARM)
        sleep(2)
        self.clear()

    def active_alarm(self):
        self.sense.set_rotation(0)
        for x in range(0, 4):
            self.sense.set_pixels(self._ALARM)
            sleep(.5)
            self.sense.set_pixels(self._ALARM_ALT)
            sleep(.5)
        self.clear()

    def clear_alarm(self):
        self.sense.set_rotation(0)
        self.sense.set_pixels(self._ALARM_CLEAR)
        sleep(2)
        self.clear()
