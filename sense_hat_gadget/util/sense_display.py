from sense_hat import SenseHat

class SenseDisplay():
    # Alexa Logo Blue
    _AB = (72, 198, 240)
    # Alexa Logo Grey
    _AG = (20, 20, 20)

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

    def __init__(self):
        self.sense = SenseHat()

    def alexa_logo(self):
        self.sense.set_rotation(0)
        self.sense.set_pixels(self._ALEXA_LOGO)

    def clear(self):
        self.sense.clear()

    def message(self, message):
        self.sense.show_message(message)