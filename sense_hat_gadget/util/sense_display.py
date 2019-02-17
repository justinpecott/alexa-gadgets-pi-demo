from sense_hat import SenseHat
from time import sleep


class SenseDisplay():
    # Alexa Logo Blue
    _AB = (72, 198, 240)
    # Grey
    _GY = (32, 32, 32)
    # Red
    _RD = (153, 0, 0)
    # White
    _WH = (153, 153, 153)
    # Pink
    _PK = (153, 0, 153)
    # Black / Off
    _BK = (0, 0, 0)
    # Green
    _GR = (0, 153, 76)
    # Orange
    _OR = (153, 76, 0)
    # Blue
    _BL = (0, 76, 153)
    # Purple
    _PP = (76, 0, 153)
    # Yellow
    _YL = (153, 153, 0)
    # Cyan
    _CY = (0, 153, 153)

    _ALEXA_LOGO = [
        _GY, _GY, _AB, _AB, _AB, _AB, _GY, _GY,
        _GY, _AB, _AB, _AB, _AB, _AB, _AB, _GY,
        _AB, _AB, _AB, _GY, _GY, _AB, _AB, _AB,
        _AB, _AB, _GY, _GY, _GY, _GY, _AB, _AB,
        _AB, _AB, _GY, _GY, _GY, _GY, _AB, _AB,
        _AB, _AB, _AB, _GY, _GY, _AB, _AB, _AB,
        _GY, _AB, _AB, _GY, _AB, _AB, _AB, _GY,
        _GY, _GY, _AB, _AB, _AB, _AB, _GY, _GY
    ]

    _ALARM = [
        _PP, _PP, _PP, _PP, _PP, _PP, _PP, _PP,
        _PP, _WH, _WH, _WH, _WH, _WH, _WH, _PP,
        _PP, _WH, _PP, _PP, _PP, _PP, _WH, _PP,
        _PP, _WH, _PP, _WH, _WH, _PP, _WH, _PP,
        _PP, _WH, _PP, _PP, _PP, _PP, _WH, _PP,
        _PP, _WH, _PP, _WH, _WH, _PP, _WH, _PP,
        _PP, _WH, _WH, _WH, _WH, _WH, _WH, _PP,
        _PP, _PP, _PP, _PP, _PP, _PP, _PP, _PP
    ]

    _ALARM_ALT = [
        _WH, _WH, _WH, _WH, _WH, _WH, _WH, _WH,
        _WH, _PP, _PP, _PP, _PP, _PP, _PP, _WH,
        _WH, _PP, _WH, _WH, _WH, _WH, _PP, _WH,
        _WH, _PP, _WH, _PP, _PP, _WH, _PP, _WH,
        _WH, _PP, _WH, _WH, _WH, _WH, _PP, _WH,
        _WH, _PP, _WH, _PP, _PP, _WH, _PP, _WH,
        _WH, _PP, _PP, _PP, _PP, _PP, _PP, _WH,
        _WH, _WH, _WH, _WH, _WH, _WH, _WH, _WH
    ]

    _ALARM_CLEAR = [
        _PP, _PP, _PP, _PP, _PP, _PP, _PP, _PP,
        _PP, _WH, _WH, _WH, _WH, _WH, _RD, _PP,
        _PP, _WH, _PP, _PP, _PP, _RD, _WH, _PP,
        _PP, _WH, _PP, _WH, _WH, _RD, _WH, _PP,
        _PP, _RD, _PP, _PP, _RD, _PP, _WH, _PP,
        _PP, _WH, _RD, _WH, _RD, _PP, _WH, _PP,
        _PP, _WH, _WH, _RD, _WH, _WH, _WH, _PP,
        _PP, _PP, _PP, _PP, _PP, _PP, _PP, _PP
    ]

    _TIMER = [
        _OR, _OR, _OR, _OR, _OR, _OR, _OR, _OR,
        _OR, _WH, _WH, _WH, _WH, _WH, _WH, _OR,
        _OR, _WH, _OR, _OR, _OR, _OR, _WH, _OR,
        _OR, _WH, _OR, _OR, _OR, _OR, _WH, _OR,
        _OR, _WH, _WH, _OR, _OR, _WH, _WH, _OR,
        _OR, _WH, _WH, _OR, _OR, _WH, _WH, _OR,
        _OR, _WH, _WH, _WH, _WH, _WH, _WH, _OR,
        _OR, _OR, _OR, _OR, _OR, _OR, _OR, _OR,
    ]

    _TIMER_ALT = [
        _WH, _WH, _WH, _WH, _WH, _WH, _WH, _WH,
        _WH, _OR, _OR, _OR, _OR, _OR, _OR, _WH,
        _WH, _OR, _WH, _WH, _WH, _WH, _OR, _WH,
        _WH, _OR, _WH, _WH, _WH, _WH, _OR, _WH,
        _WH, _OR, _OR, _WH, _WH, _OR, _OR, _WH,
        _WH, _OR, _OR, _WH, _WH, _OR, _OR, _WH,
        _WH, _OR, _OR, _OR, _OR, _OR, _OR, _WH,
        _WH, _WH, _WH, _WH, _WH, _WH, _WH, _WH
    ]

    _TIMER_CLEAR = [
        _OR, _OR, _OR, _OR, _OR, _OR, _OR, _OR,
        _OR, _WH, _WH, _WH, _WH, _WH, _RD, _OR,
        _OR, _WH, _OR, _OR, _OR, _RD, _WH, _OR,
        _OR, _WH, _OR, _OR, _OR, _RD, _WH, _OR,
        _OR, _RD, _WH, _OR, _RD, _WH, _WH, _OR,
        _OR, _WH, _RD, _OR, _RD, _WH, _WH, _OR,
        _OR, _WH, _WH, _RD, _WH, _WH, _WH, _OR,
        _OR, _OR, _OR, _OR, _OR, _OR, _OR, _OR,
    ]

    _REMINDER = [
        _BL, _BL, _BL, _BL, _BL, _BL, _BL, _BL,
        _BL, _WH, _WH, _WH, _WH, _WH, _WH, _BL,
        _BL, _WH, _BL, _BL, _BL, _BL, _WH, _BL,
        _BL, _WH, _BL, _WH, _WH, _BL, _WH, _BL,
        _BL, _WH, _BL, _BL, _BL, _BL, _WH, _BL,
        _BL, _WH, _BL, _WH, _BL, _WH, _WH, _BL,
        _BL, _WH, _WH, _WH, _WH, _WH, _WH, _BL,
        _BL, _BL, _BL, _BL, _BL, _BL, _BL, _BL
    ]

    _REMINDER_ALT = [
        _WH, _WH, _WH, _WH, _WH, _WH, _WH, _WH,
        _WH, _BL, _BL, _BL, _BL, _BL, _BL, _WH,
        _WH, _BL, _WH, _WH, _WH, _WH, _BL, _WH,
        _WH, _BL, _WH, _BL, _BL, _WH, _BL, _WH,
        _WH, _BL, _WH, _WH, _WH, _WH, _BL, _WH,
        _WH, _BL, _WH, _BL, _WH, _BL, _BL, _WH,
        _WH, _BL, _BL, _BL, _BL, _BL, _BL, _WH,
        _WH, _WH, _WH, _WH, _WH, _WH, _WH, _WH
    ]

    _REMINDER_CLEAR = [
        _BL, _BL, _BL, _BL, _BL, _BL, _BL, _BL,
        _BL, _WH, _WH, _WH, _WH, _WH, _RD, _BL,
        _BL, _WH, _BL, _BL, _BL, _RD, _WH, _BL,
        _BL, _WH, _BL, _WH, _WH, _RD, _WH, _BL,
        _BL, _RD, _BL, _BL, _RD, _BL, _WH, _BL,
        _BL, _WH, _RD, _WH, _RD, _WH, _WH, _BL,
        _BL, _WH, _WH, _RD, _WH, _WH, _WH, _BL,
        _BL, _BL, _BL, _BL, _BL, _BL, _BL, _BL
    ]

    _NOTIFICATION = [
        _GR, _GR, _GR, _GR, _GR, _GR, _GR, _GR,
        _GR, _WH, _WH, _WH, _WH, _WH, _WH, _GR,
        _GR, _WH, _GR, _GR, _GR, _GR, _WH, _GR,
        _GR, _WH, _GR, _WH, _WH, _GR, _WH, _GR,
        _GR, _WH, _GR, _WH, _WH, _GR, _WH, _GR,
        _GR, _WH, _GR, _WH, _WH, _GR, _WH, _GR,
        _GR, _WH, _WH, _WH, _WH, _WH, _WH, _GR,
        _GR, _GR, _GR, _GR, _GR, _GR, _GR, _GR
    ]

    _NOTIFICATION_ALT = [
        _WH, _WH, _WH, _WH, _WH, _WH, _WH, _WH,
        _WH, _GR, _GR, _GR, _GR, _GR, _GR, _WH,
        _WH, _GR, _WH, _WH, _WH, _WH, _GR, _WH,
        _WH, _GR, _WH, _GR, _GR, _WH, _GR, _WH,
        _WH, _GR, _WH, _GR, _GR, _WH, _GR, _WH,
        _WH, _GR, _WH, _GR, _GR, _WH, _GR, _WH,
        _WH, _GR, _GR, _GR, _GR, _GR, _GR, _WH,
        _WH, _WH, _WH, _WH, _WH, _WH, _WH, _WH
    ]

    _NOTIFICATION_CLEAR = [
        _WH, _WH, _WH, _WH, _WH, _WH, _WH, _WH,
        _WH, _GR, _GR, _GR, _GR, _GR, _RD, _WH,
        _WH, _GR, _WH, _WH, _WH, _RD, _GR, _WH,
        _WH, _GR, _WH, _GR, _GR, _RD, _GR, _WH,
        _WH, _RD, _WH, _GR, _RD, _WH, _GR, _WH,
        _WH, _GR, _RD, _GR, _RD, _WH, _GR, _WH,
        _WH, _GR, _GR, _RD, _GR, _GR, _GR, _WH,
        _WH, _WH, _WH, _WH, _WH, _WH, _WH, _WH
    ]

    _MUSIC = [
        _BK, _BK, _BK, _BK, _BK, _BK, _BK, _BK,
        _BK, _BK, _YL, _YL, _YL, _YL, _YL, _BK,
        _BK, _BK, _YL, _YL, _YL, _YL, _YL, _BK,
        _BK, _BK, _YL, _BK, _BK, _BK, _YL, _BK,
        _BK, _BK, _YL, _BK, _BK, _BK, _YL, _BK,
        _BK, _YL, _YL, _BK, _BK, _YL, _YL, _BK,
        _BK, _YL, _YL, _BK, _BK, _YL, _YL, _BK,
        _BK, _BK, _BK, _BK, _BK, _BK, _BK, _BK
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

    _ALERT_LOGOS = {
        "alarms": _ALARM,
        "ALARM": _ALARM,
        "alarms_alt": _ALARM_ALT,
        "alarms_clear": _ALARM_CLEAR,
        "timers": _TIMER,
        "TIMER": _TIMER,
        "timers_alt": _TIMER_ALT,
        "timers_clear": _TIMER_CLEAR,
        "reminders": _REMINDER,
        "REMINDER": _REMINDER,
        "reminders_alt": _REMINDER_ALT,
        "reminders_clear": _REMINDER_CLEAR,
        "notifications": _NOTIFICATION,
        "notifications_alt": _NOTIFICATION_ALT,
        "notifications_clear": _NOTIFICATION_CLEAR
    }

    _COLORS = {
        "grey": _GY,
        "gray": _GY,
        "red": _RD,
        "white": _WH,
        "pink": _PK,
        "black": _BK,
        "off": _BK,
        "green": _GR,
        "orange": _OR,
        "blue": _BL,
        "purple": _PP,
        "yellow": _YL,
        "cyan": _CY
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

    def set_alert(self, alert_type):
        self.sense.set_rotation(0)
        self.sense.set_pixels(self._ALERT_LOGOS[alert_type])
        sleep(2)
        self.clear()

    def active_alert(self, alert_type):
        self.sense.set_rotation(0)
        for x in range(0, 4):
            self.sense.set_pixels(self._ALERT_LOGOS[alert_type])
            sleep(.5)
            self.sense.set_pixels(self._ALERT_LOGOS[alert_type + "_alt"])
            sleep(.5)
        self.clear()

    def clear_alert(self, alert_type):
        self.sense.set_rotation(0)
        self.sense.set_pixels(self._ALERT_LOGOS[alert_type + "_clear"])
        sleep(2)
        self.clear()

    def show_bpm(self, bpm):
        self.sense.set_rotation(0)
        self.sense.set_pixels(self._MUSIC)
        sleep(.5)
        self.sense.show_message(str(bpm), text_colour=self._YL)
        self.sense.set_pixels(self._MUSIC)
        sleep(.5)
        self.clear()
