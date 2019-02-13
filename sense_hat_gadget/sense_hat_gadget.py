#
# Copyright (c) 2018 Amazon.com Inc. All Rights Reserved.

# AMAZON.COM CONFIDENTIAL
#
from util import SenseHatGadgetBase
from sense_hat import SenseHat
import json
import logging

logger = logging.getLogger(__name__)


class SenseHatGadget(SenseHatGadgetBase):
    sense = SenseHat()
    alexa_blue = (72, 198, 240)
    alexa_grey = (20, 20, 20)

    alexa_logo = [
        alexa_grey, alexa_grey, alexa_blue, alexa_blue, alexa_blue, alexa_blue, alexa_grey, alexa_grey,
        alexa_grey, alexa_blue, alexa_blue, alexa_blue, alexa_blue, alexa_blue, alexa_blue, alexa_grey,
        alexa_blue, alexa_blue, alexa_blue, alexa_grey, alexa_grey, alexa_blue, alexa_blue, alexa_blue,
        alexa_blue, alexa_blue, alexa_grey, alexa_grey, alexa_grey, alexa_grey, alexa_blue, alexa_blue,
        alexa_blue, alexa_blue, alexa_grey, alexa_grey, alexa_grey, alexa_grey, alexa_blue, alexa_blue,
        alexa_blue, alexa_blue, alexa_blue, alexa_grey, alexa_grey, alexa_blue, alexa_blue, alexa_blue,
        alexa_grey, alexa_blue, alexa_blue, alexa_grey, alexa_blue, alexa_blue, alexa_blue, alexa_grey,
        alexa_grey, alexa_grey, alexa_blue, alexa_blue, alexa_blue, alexa_blue, alexa_grey, alexa_grey
        ]

    def state_listener_cb(self, payload):
        logger.debug(payload)

        states = payload.directive.payload.states
        for i in states:
            # Show an 'Alexa Logo' on wake word and clear it when complete
            if i.name == "wakeword":
                if i.value == "active":
                    self.sense.set_rotation(0)
                    self.sense.set_pixels(self.alexa_logo)
                elif i.value == "cleared":
                    self.sense.clear()

    def speechdata_cb(self, payload):
        logger.debug(payload)

    def alerts_cb(self, payload):
        logger.debug(payload)

    def notifications_cb(self, payload):
        logger.debug(payload)

    def musicdata_cb(self, payload):
        logger.debug(payload)

    def custom_sense_cb(self, payload):
        logger.debug(payload)
        name = payload.directive.header.name
        custom_directive = payload.directive.payload.decode("utf8")

        if name == "DisplayMessage":
            message_obj = json.loads(custom_directive)
            self.sense.show_message(message_obj["message"])
            self.sense.clear()
        else:
            self.sense.show_message("What?!")
            self.sense.clear()


if __name__ == '__main__':
    # Log to file as well
    file_handler_format = logging.Formatter("%(levelname)s : %(asctime)s --\n%(message)s\n")
    file_handler = logging.FileHandler("sense_hat.log", mode='w')
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(file_handler_format)
    logger.addHandler(file_handler)

    SenseHatGadget().main()
