#
# Copyright (c) 2018 Amazon.com Inc. All Rights Reserved.

# AMAZON.COM CONFIDENTIAL
#
import configparser
import time
from abc import ABC, abstractmethod

from platforms.bluez import BlueZConnection
from pyagt.config.config import Capability, CapabilityTypes, InterfaceTypes, StateListenerSupportedTypes, \
    SpeechDataSupportedTypes, MusicDataSupportedTypes
from pyagt.gadget_base import BaseGadget
import logging
import argparse

# ------------------------------------------------
# sense_hat_config.ini constants
SENSE_HAT_CONFIG_INI = 'sense_hat_config.ini'

# Default section keys
DEFAULT = 'DEFAULT'
GADGET_TYPE = 'GadgetType'
GADGET_SECRET = 'GadgetSecret'
FRIENDLY_NAME = 'FriendlyName'

# GadgetSettings section keys
GADGET_SETTINGS = 'GadgetSettings'
BT_ADDRESS = 'BTAddress'

# Default values
DEFAULT_GADGET_TYPE = 'YOUR_GADGET_AMAZON_ID'
DEFAULT_GADGET_SECRET = 'YOUR_GADGET_SECRET'
# ------------------------------------------------

logger = logging.getLogger(__name__)


class SenseHatGadgetBase(BaseGadget, ABC):

    def __init__(self):
        """
        Gadget initialization.
        """
        # Get and read the sense_hat_config.ini into an object called self.sense_hat_gadget_config
        self.sense_hat_gadget_config = configparser.ConfigParser()
        self.sense_hat_gadget_config.read(SENSE_HAT_CONFIG_INI)

        # Get values from the self.simple_gadget_config and set them to variables
        gadget_type = self.sense_hat_gadget_config.get(DEFAULT, GADGET_TYPE)
        if not gadget_type or gadget_type == DEFAULT_GADGET_TYPE:
            raise Exception('Please specify the gadgettype in ' + SENSE_HAT_CONFIG_INI)

        gadget_secret = self.sense_hat_gadget_config.get(DEFAULT, GADGET_SECRET)
        if not gadget_secret  or gadget_secret == DEFAULT_GADGET_SECRET:
            raise Exception('Please specify the gadgetsecret in ' + SENSE_HAT_CONFIG_INI)

        # Make friendly_name an instance variable so we can use it in the start() function
        self.friendly_name = self.sense_hat_gadget_config.get(DEFAULT, FRIENDLY_NAME)
        if not self.friendly_name or self.friendly_name == '':
            raise Exception('Please specify the friendlyname in ' + SENSE_HAT_CONFIG_INI)

        # Initialize the parent class now that we have the above variables
        super().__init__(gadget_type, gadget_secret, self.friendly_name, BlueZConnection)

        # Parse arguments passed in by user
        self.parse_args()

        # Track first connection
        self.connection_seen = False

        # Add statelistener capability with all supported types
        statelistener_supported_types = [StateListenerSupportedTypes.TIMERS,
                                         StateListenerSupportedTypes.ALARMS,
                                         StateListenerSupportedTypes.REMINDERS,
                                         StateListenerSupportedTypes.TIMEINFO,
                                         StateListenerSupportedTypes.WAKEWORD]
        sl_cap = Capability(CapabilityTypes.ALEXAINTERFACE,
                            InterfaceTypes.STATELISTENER,
                            '1.0',
                            self.state_listener_cb,
                            statelistener_supported_types)

        # Add speechdata capability with all supported types
        speechdata_supported_types = [SpeechDataSupportedTypes.VISEME]
        speechdata_cap = Capability(CapabilityTypes.ALEXAINTERFACE,
                                    InterfaceTypes.SPEECHDATA,
                                    '1.0',
                                    self.speechdata_cb,
                                    speechdata_supported_types)

        # Add alerts capability (there are no supported types for this capability)
        alerts_cap = Capability(CapabilityTypes.ALEXAINTERFACE,
                                InterfaceTypes.ALERTS,
                                '1.1',
                                self.alerts_cb)

        # Add Notifications capability (there are no supported types for this capability)
        notifications_cap = Capability(CapabilityTypes.ALEXAINTERFACE,
                                       InterfaceTypes.NOTIFICATIONS,
                                       '1.0',
                                       self.notifications_cb)

        # Add musicdata capability with all supported types
        md_supported_types = [MusicDataSupportedTypes.TEMPO]
        musicdata_cap = Capability(CapabilityTypes.ALEXAINTERFACE,
                                   InterfaceTypes.MUSICDATA,
                                   '1.0',
                                   self.musicdata_cb,
                                   md_supported_types)

        # Add Sense Hat Display Directive
        custom_sense_cap = Capability(CapabilityTypes.ALEXAINTERFACE,
                                     "SenseHatGadget",
                                     "1.0",
                                    self.custom_sense_cb)

        self.config.add_capability(sl_cap)
        self.config.add_capability(speechdata_cap)
        self.config.add_capability(alerts_cap)
        self.config.add_capability(notifications_cap)
        self.config.add_capability(musicdata_cap)
        self.config.add_capability(custom_sense_cap)

    def start(self):
        """
        Start gadget. Inherited from base class. Is called in main()

        :return: None
        """
        super().start()

        # Reconnect if bluetooth address is in the configuration file, otherwise enter pairing mode.
        if BT_ADDRESS in self.sense_hat_gadget_config[GADGET_SETTINGS]:
            bt_addr = self.sense_hat_gadget_config.get(GADGET_SETTINGS, BT_ADDRESS)
            self.connection.reconnect(bt_addr)
        else:
            self.connection.pair(True)
            logger.debug('Device is now in pairing mode. Pair "' + self.friendly_name + '" in the companion app.')

    def update(self):
        """
        Update the gadget. Inherited from base class.

        :return: None
        """
        # Check whether first connection has happened and whether we are connected to an Echo device
        if not self.connection_seen and self.connection.is_connected():
            # In this case, we haven't been connected before, but are now, so do first time connection logic
            logger.debug('-------')
            logger.debug('Bluetooth Layer Connection Established with {}'.format(self.connection.get_connection_info()))

            # Set the bluetooth address of the echo device so we can
            bt_addr, unused = self.connection.get_connection_info()
            logger.debug("Bluetooth address of Echo device: " + bt_addr)

            # Set the bluetooth of the Echo device in the configuration file for future reconnection
            self.sense_hat_gadget_config.set(GADGET_SETTINGS, BT_ADDRESS, bt_addr)
            with open(SENSE_HAT_CONFIG_INI, 'w') as configfile:
                self.sense_hat_gadget_config.write(configfile)

            # Now that we've seen an initial connection, set self.connection_seen to True
            self.connection_seen = True

            # Turn off pairing mode if it was enabled.
            self.connection.pair(False)

        elif self.connection_seen and not self.connection.is_connected():
            # If we were connected before, but are not now, then we have been disconnected
            logger.debug('Device disconnected')

            # Start reconnection logic
            try:
                logger.debug('Trying to reconnect')
                bt_addr = self.sense_hat_gadget_config.get(GADGET_SETTINGS, BT_ADDRESS)
                self.connection.reconnect(bt_addr)

                time.sleep(2)

                # If reconnection logic succeeded, then let the user know
                if self.connection.is_connected():
                    logger.debug('-------')
                    logger.debug('Bluetooth Layer Connection Established with {}'.
                                 format(self.connection.get_connection_info()))
            except:
                # Reconnection was not successful...likely because the Echo device is unreachable at the moment.
                return

        elif not self.connection_seen:
            # User hasn't paired yet. Continue waiting for a connection
            return

    # ------------------------------------------------
    # Helper methods
    # ------------------------------------------------
    def parse_args(self):
        """
        Parse the arguments passed in by the user
        :return:
        """
        parser = argparse.ArgumentParser(description='Tiny Gadget to demonstrate pairing and reconnect.')

        # If --clear is passed in, then we'll want to remove the stored bluetooth address from the config file
        parser.add_argument('--clear', action='store_true', required=False, help='Reset gadget by forgetting the '
                                                                                 'BT address. Please forget gadget in '
                                                                                 'the companion app as well.')
        args = parser.parse_args()
        if args.clear:
            # Since clear was passed in, we will remove the bluetooth address
            return self.clear_btaddress()

    def clear_btaddress(self):
        """
        Simply removes the bluetooth address from the configuration file, which will cause the gadget to act as a new,
        unpaired gadget
        :return:
        """
        logger.debug('Resetting Gadget')
        self.sense_hat_gadget_config.remove_option(GADGET_SETTINGS, BT_ADDRESS)
        with open(SENSE_HAT_CONFIG_INI, 'w') as configfile:
            self.sense_hat_gadget_config.write(configfile)

    # ------------------------------------------------
    # Callback methods that sub classes must override
    # ------------------------------------------------
    @abstractmethod
    def state_listener_cb(self, payload):
        """
        This is the callback method for the statelistener capability. Must be implemented in the sub class
        :param payload:
        :return:
        """
        pass

    @abstractmethod
    def speechdata_cb(self, payload):
        """
        This is the callback method for the speechdata capability. Must be implemented in the sub class
        :param payload:
        :return:
        """
        pass

    @abstractmethod
    def alerts_cb(self, payload):
        """
        This is the callback method for the alerts capability. Must be implemented in the sub class
        :param payload:
        :return:
        """
        pass

    @abstractmethod
    def notifications_cb(self, payload):
        """
        This is the callback method for the notifications capability. Must be implemented in the sub class
        :param payload:
        :return:
        """
        pass

    @abstractmethod
    def musicdata_cb(self, payload):
        """
        This is the callback method for the musicdata capability. Must be implemented in the sub class
        :param payload:
        :return:
        """
        pass

    @abstractmethod
    def custom_sense_cb(self, payload):
        """
        This is the callback method for the custom sense hat capability. Must be implemented in the sub class
        :param payload:
        :return:
        """
        pass
