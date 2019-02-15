#
# Copyright (c) 2018 Amazon.com Inc. All Rights Reserved.

# AMAZON.COM CONFIDENTIAL
#
from util import SenseHatGadgetBase, SenseDisplay
import json
import logging

logger = logging.getLogger(__name__)

class SenseHatGadget(SenseHatGadgetBase):

    def __init__(self):
        self.display = SenseDisplay()
        super().__init__()

    def state_listener_cb(self, payload):
        logger.debug(payload)

        states = payload.directive.payload.states
        for i in states:
            # Show an 'Alexa Logo' on wake word and clear it when complete
            if i.name == "wakeword":
                if i.value == "active":
                    self.display.alexa_logo()
                elif i.value == "cleared":
                    self.display.clear()

    def speechdata_cb(self, payload):
        logger.debug(payload)
        speechmarks_data = payload.directive.payload.speechmarksData
        for i in speechmarks_data:
            # Show rudementary 'lip sync' images
            self.display.speechmark(i.value)

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
            self.display.message(message_obj["message"])
            self.display.clear()
        else:
            self.display.message("What?!")
            self.display.clear()


if __name__ == '__main__':
    # Log to file as well
    file_handler_format = logging.Formatter("%(levelname)s : %(asctime)s --\n%(message)s\n")
    file_handler = logging.FileHandler("sense_hat.log", mode='w')
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(file_handler_format)
    logger.addHandler(file_handler)

    SenseHatGadget().main()
