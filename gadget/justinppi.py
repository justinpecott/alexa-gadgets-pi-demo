#
# Copyright (c) 2018 Amazon.com Inc. All Rights Reserved.

# AMAZON.COM CONFIDENTIAL
#
import json
import logging

import protobuf.gadget.proto_gadget_base as proto_gadget
from pi_gadget import main
from sense_hat import SenseHat

class ExampleGadget(proto_gadget.ProtoGadgetBase):
    sense = SenseHat()
    red = (255, 0, 0)
    blue = (0, 0, 255)
    green = (0, 255, 0)
    white = (255, 255, 255)
    yellow = (255, 255, 0)

    def on_statelistener_stateupdate(self, incoming_msg):
        namespace = incoming_msg.directive.header.namespace
        name = incoming_msg.directive.header.name
        states = incoming_msg.directive.payload.states

        logging.info("Received Protobuf Message\n\tNamespace: " + namespace + "\tName: " + name)
        for i in states:
            logging.info("\tState name: " + i.name + "\t\t\tState Value: " + i.value)

    def on_notification_setindicator(self, incoming_msg):
        namespace = incoming_msg.directive.header.namespace
        name = incoming_msg.directive.header.name
        persist_visual_indidcator = str(incoming_msg.directive.payload.persistVisualIndicator)
        play_audio_indicator = str(incoming_msg.directive.payload.playAudioIndicator)
        asset_id = incoming_msg.directive.payload.asset.assetId
        url = incoming_msg.directive.payload.asset.url

        logging.info("Received Protobuf Message\n\tNamespace: " + namespace + "\tName: " + name)
        logging.info("Persist visual indicator:" + persist_visual_indidcator + "\tPlay audio indicator: " +
              play_audio_indicator + "\tAsset id: " + asset_id + "\tUrl: " + url)

    def on_notification_clearindicator(self, incoming_msg):
        namespace = incoming_msg.directive.header.namespace
        name = incoming_msg.directive.header.name
        logging.info("Received Protobuf Message\n\tNamespace: " + namespace + "\t\tName: " + name)

    def on_speechdata_speechmarks(self, incoming_msg):
        namespace = incoming_msg.directive.header.namespace
        name = incoming_msg.directive.header.name
        speechmarks_data = incoming_msg.directive.payload.speechmarksData

        logging.info("Received Protobuf Message\n\tNamespace: " + namespace + "\tName: " + name)
        for i in speechmarks_data:
            logging.info("\tSpeechmark start offset (millis): " + str(
                i.startOffsetInMilliSeconds) + "\tSpeechmark type: " + i.type + "\tSpeechmark value: " + i.value)

    def on_musicdata_tempo(self, incoming_msg):
        namespace = incoming_msg.directive.header.namespace
        name = incoming_msg.directive.header.name
        player_offset_in_milliseconds = incoming_msg.directive.payload.playerOffsetInMilliSeconds
        tempo_data = incoming_msg.directive.payload.tempoData

        logging.info("Received Protobuf Message\n\tNamespace: " + namespace + "\tName: " + name)
        logging.info("\tPlayer offset (millis): " + str(player_offset_in_milliseconds))
        for i in tempo_data:
            logging.info(
                "\t\tTempo data start offset (millis): " + str(i.startOffsetInMilliSeconds) + "\tTempo value : " + str(
                    i.value))

    def on_alerts_set(self, incoming_msg):
        namespace = incoming_msg.directive.header.namespace
        name = incoming_msg.directive.header.name
        asset_play_order = incoming_msg.directive.payload.assetPlayOrder
        loop_pause_in_milliseconds = incoming_msg.directive.payload.loopPauseInMilliSeconds
        scheduled_time = incoming_msg.directive.payload.scheduledTime
        assets = incoming_msg.directive.payload.assets
        loop_count = incoming_msg.directive.payload.loopCount
        background_alert_asset = incoming_msg.directive.payload.backgroundAlertAsset
        payload_type = incoming_msg.directive.payload.type
        token = incoming_msg.directive.payload.token

        logging.info("Received Protobuf Message\n\tNamespace: " + namespace + "\t\t\tName: " + name)
        logging.info("\tScheduled time: " + scheduled_time + "\tType: " + payload_type + "\tToken: " + token)
        if assets:
            for j in assets:
                logging.info("\tAsset Id: " + j.assetId + "\tAsset Url: " + j.url)
            for i in asset_play_order:
                logging.info("\tEnd offset: " + i)
            logging.info("\tLoop pause (millis): " + str(loop_pause_in_milliseconds))
            logging.info("\tLoop count: " + str(loop_count) + "\tBackground alert asset: " + background_alert_asset)

    def on_alerts_delete(self, incoming_msg):
        namespace = incoming_msg.directive.header.namespace
        name = incoming_msg.directive.header.name
        token = incoming_msg.directive.payload.token

        logging.info("Received Protobuf Message\n\tNamespace: " + namespace + "\t\tName: " + name + "\n\tToken: " + token)

    def on_custom(self, incoming_msg):
        namespace = incoming_msg.directive.header.namespace
        name = incoming_msg.directive.header.name
        payload = incoming_msg.directive.payload.decode("utf8")
        logging.info("Received Custom Protobuf Message\n\tNamespace: " + namespace + "\t\t\tName: " + name + "\n\tPayload: " + payload)

        if (namespace == "StatusGaugeGadget" or namespace == "PiTimeGadget") and name == "SetStatus":
            # Custom directive for the Alexa Status Gauge Skill
            status_obj = json.loads(payload)
            status_value = status_obj["status"]

            if status_value == 1:
                self.sense.show_message("Lunch!", text_colour=self.yellow, scroll_speed=.06)
            elif status_value == 2:
                self.sense.show_message("Meeting!", text_colour=self.blue, scroll_speed=.06)
            elif status_value == 3:
                self.sense.show_message("Busy!", text_colour=self.red, scroll_speed=.06)
            elif status_value == 4:
                self.sense.show_message("Travelling!", text_colour=self.white, scroll_speed=.06)
            elif status_value == 5:
                self.sense.show_message("Available!", text_colour=self.green, scroll_speed=.06)

            self.sense.clear()
        elif namespace == "PiTimeGadget" and name == "SendMessage":
            #message_obj = json.loads(payload)
            self.sense.show_message("Send Message Here")
            self.sense.clear()
        else:
            self.sense.show_message("What?!")
            self.sense.clear()


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.DEBUG,
        format="-- %(asctime)s --\n%(message)s\n----\n\n",
        handlers=[
            logging.FileHandler("justinppi.log"),
            logging.StreamHandler()
        ])
    main.RunMain(ExampleGadget()).run_main()
