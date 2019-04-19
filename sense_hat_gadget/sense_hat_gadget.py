#
# Copyright (c) 2018 Amazon.com Inc. All Rights Reserved.

# AMAZON.COM CONFIDENTIAL
#
from agt import AlexaGadget
from proto import SenseHatEvent
from sense_hat import SenseHat
from util import SenseDisplay
from pathlib import Path
from google.protobuf import json_format
import sys
import json
import logging
import threading
import time

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logger = logging.getLogger(__name__)

class SenseHatGadget(AlexaGadget):

    def __init__(self):
        self.sense = SenseHat()
        self.display = SenseDisplay(self.sense)
        shake_check = threading.Thread(target=self.alert_on_shake, args=(), daemon=True)
        shake_check.start()
        super().__init__()

    def on_alexa_gadget_statelistener_stateupdate(self, directive):
        """
        Alexa.Gadget.StateListener StateUpdate directive received.

        For more info, visit:
            https://developer.amazon.com/docs/alexa-gadgets-toolkit/alexa-gadget-statelistener-interface.html#StateUpdate-directive

        :param directive: Protocol Buffer Message that was send by Echo device.
        """
        logger.debug(directive)
        states = directive.payload.states
        for i in states:
            # Show an 'Alexa Logo' on wake word and clear it when complete
            if i.name == "wakeword":
                if i.value == "active":
                    self.display.alexa_logo()
                elif i.value == "cleared":
                    self.display.clear()
            # We can do something more complicated here but for now we'll just
            # Show alert set, alert active, and alert cleared
            elif i.name == "alarms" or i.name == "timers" or i.name == "reminders":
                if i.value == "active":
                    self.display.active_alert(i.name)
                elif i.value == "cleared":
                    self.display.clear_alert(i.name)

    def on_alexa_gadget_speechdata_speechmarks(self, directive):
        """
        Alexa.Gadget.SpeechData Speechmarks directive received.

        For more info, visit:
            https://developer.amazon.com/docs/alexa-gadgets-toolkit/alexa-gadget-speechdata-interface.html#Speechmarks-directive

        :param directive: Protocol Buffer Message that was send by Echo device.
        """
        logger.debug(directive)
        speechmarks_data = directive.payload.speechmarksData
        for i in speechmarks_data:
            # Show rudementary 'lip sync' images
            self.display.speechmark(i.value)

    def on_alerts_setalert(self, directive):
        """
        Alerts SetAlert directive received.

        For more info, visit:
            https://developer.amazon.com/docs/alexa-gadgets-toolkit/alerts-interface.html#SetAlert-directive

        :param directive: Protocol Buffer Message that was send by Echo device.
        """
        # We can do something more complicated here but for now we'll just
        # Show alert set, alert active, and alert cleared
        logger.debug(directive)
        alert_type = directive.payload.type
        # alert_token = payload.directive.payload.token
        # alert_time = payload.directive.payload.scheduledTime
        self.display.set_alert(alert_type)


    def on_alerts_deletealert(self, directive):
        """
        Alerts DeleteAlert directive received.

        For more info, visit:
            https://developer.amazon.com/docs/alexa-gadgets-toolkit/alerts-interface.html#DeleteAlert-directive

        :param directive: Protocol Buffer Message that was send by Echo device.
        """
        logger.debug(directive)
        # alert_token = payload.directive.payload.token


    def on_notifications_setindicator(self, directive):
        """
        Notifications SetIndicator directive received.

        For more info, visit:
            https://developer.amazon.com/docs/alexa-gadgets-toolkit/notifications-interface.html#SetIndicator-directive

        :param directive: Protocol Buffer Message that was send by Echo device.
        """
        # We can do something more complicated here but for now we'll just
        # Show notification active and notification cleared
        # persist_indicator = payload.directive.payload.persistVisualIndicator
        # audio_indicator = payload.directive.payload.playAudioIndicator
        logger.debug(directive)
        self.display.active_alert("notifications")

    def on_notifications_clearindicator(self, directive):
        """
        Notifications ClearIndicator directive received.

        For more info, visit:
            https://developer.amazon.com/docs/alexa-gadgets-toolkit/notifications-interface.html#ClearIndicator-directive

        :param directive: Protocol Buffer Message that was send by Echo device.
        """
        # We can do something more complicated here but for now we'll just
        # Show notification active and notification cleared
        logger.debug(directive)
        self.display.clear_alert("notifications")

    def on_alexa_gadget_musicdata_tempo(self, directive):
        """
        Alexa.Gadget.MusicData Tempo directive received.

        For more info, visit:
            https://developer.amazon.com/docs/alexa-gadgets-toolkit/alexa-gadget-musicdata-interface.html#Tempo-directive

        :param directive: Protocol Buffer Message that was send by Echo device.
        """
        logger.debug(directive)
        tempo_data = directive.payload.tempoData
        for i in tempo_data:
            if i.value > 0:
                self.display.show_bpm(i.value)

    def on_custom_sensehatgadget_displaymessage(self, directive):
        """
        Custom Directive Handling for SenseHatGadget.DisplayMessage
        """
        logger.debug(directive)
        message_obj = json.loads(directive.payload.decode("utf8"))
        self.display.message(message_obj["message"])
        self.display.clear()

    def alert_on_shake(self):
        logger.debug("KICKING THE SHAKE CHECK THREAD OFF")
        while True:
            time.sleep(.5)
            acceleration = self.sense.get_accelerometer_raw()
            x = abs(acceleration['x'])
            y = abs(acceleration['y'])
            z = abs(acceleration['z'])
            if x > 2 or y > 2 or z > 2:
                logger.debug("Shake detected.")
                logger.debug("x:" + str(x) + " y:" + str(y) + " z:" + str(z))
                self.sense.show_letter("!", (255, 0, 0))

                custom_event = SenseHatEvent()
                custom_event.header.namespace = "Custom.SenseHatGadget"
                custom_event.header.name = "VoiceResponse"
                custom_event.header.messageId = ""
                payload = {
                    "message": "Shake it like a polaroid picture"
                }
                custom_event.payload = json.dumps(payload)
                self.send_event(custom_event)
                time.sleep(.5)
                self.sense.clear()

        logger.debug("SHAKE CHECK THREAD IS DEAD")

if __name__ == '__main__':
    SenseHatGadget().main()
