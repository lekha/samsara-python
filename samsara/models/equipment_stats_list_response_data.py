# coding: utf-8

"""
    Samsara API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 2019-12-12
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from samsara.configuration import Configuration


class EquipmentStatsListResponseData(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'engine_rpm': 'list[EquipmentEngineRpm]',
        'engine_seconds': 'list[EquipmentEngineSeconds]',
        'engine_states': 'list[EquipmentEngineState]',
        'fuel_percent': 'list[EquipmentFuelPercent]',
        'gateway_engine_seconds': 'list[EquipmentGatewayEngineSeconds]',
        'gateway_engine_state': 'list[EquipmentGatewayEngineState]',
        'gps_odometer_meters': 'list[EquipmentGpsOdometerMeters]',
        'id': 'str',
        'name': 'str',
        'obd_engine_seconds': 'list[EquipmentObdEngineSeconds]',
        'obd_engine_state': 'list[EquipmentObdEngineState]'
    }

    attribute_map = {
        'engine_rpm': 'engineRpm',
        'engine_seconds': 'engineSeconds',
        'engine_states': 'engineStates',
        'fuel_percent': 'fuelPercent',
        'gateway_engine_seconds': 'gatewayEngineSeconds',
        'gateway_engine_state': 'gatewayEngineState',
        'gps_odometer_meters': 'gpsOdometerMeters',
        'id': 'id',
        'name': 'name',
        'obd_engine_seconds': 'obdEngineSeconds',
        'obd_engine_state': 'obdEngineState'
    }

    def __init__(self, engine_rpm=None, engine_seconds=None, engine_states=None, fuel_percent=None, gateway_engine_seconds=None, gateway_engine_state=None, gps_odometer_meters=None, id=None, name=None, obd_engine_seconds=None, obd_engine_state=None, local_vars_configuration=None):  # noqa: E501
        """EquipmentStatsListResponseData - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._engine_rpm = None
        self._engine_seconds = None
        self._engine_states = None
        self._fuel_percent = None
        self._gateway_engine_seconds = None
        self._gateway_engine_state = None
        self._gps_odometer_meters = None
        self._id = None
        self._name = None
        self._obd_engine_seconds = None
        self._obd_engine_state = None
        self.discriminator = None

        if engine_rpm is not None:
            self.engine_rpm = engine_rpm
        if engine_seconds is not None:
            self.engine_seconds = engine_seconds
        if engine_states is not None:
            self.engine_states = engine_states
        if fuel_percent is not None:
            self.fuel_percent = fuel_percent
        if gateway_engine_seconds is not None:
            self.gateway_engine_seconds = gateway_engine_seconds
        if gateway_engine_state is not None:
            self.gateway_engine_state = gateway_engine_state
        if gps_odometer_meters is not None:
            self.gps_odometer_meters = gps_odometer_meters
        self.id = id
        self.name = name
        if obd_engine_seconds is not None:
            self.obd_engine_seconds = obd_engine_seconds
        if obd_engine_state is not None:
            self.obd_engine_state = obd_engine_state

    @property
    def engine_rpm(self):
        """Gets the engine_rpm of this EquipmentStatsListResponseData.  # noqa: E501

        A time-series of engine RPM readings for the given unit of equipment.  # noqa: E501

        :return: The engine_rpm of this EquipmentStatsListResponseData.  # noqa: E501
        :rtype: list[EquipmentEngineRpm]
        """
        return self._engine_rpm

    @engine_rpm.setter
    def engine_rpm(self, engine_rpm):
        """Sets the engine_rpm of this EquipmentStatsListResponseData.

        A time-series of engine RPM readings for the given unit of equipment.  # noqa: E501

        :param engine_rpm: The engine_rpm of this EquipmentStatsListResponseData.  # noqa: E501
        :type: list[EquipmentEngineRpm]
        """

        self._engine_rpm = engine_rpm

    @property
    def engine_seconds(self):
        """Gets the engine_seconds of this EquipmentStatsListResponseData.  # noqa: E501

        [DEPRECATED] Please use either `gatewayEngineSeconds` or `obdEngineSeconds`.  # noqa: E501

        :return: The engine_seconds of this EquipmentStatsListResponseData.  # noqa: E501
        :rtype: list[EquipmentEngineSeconds]
        """
        return self._engine_seconds

    @engine_seconds.setter
    def engine_seconds(self, engine_seconds):
        """Sets the engine_seconds of this EquipmentStatsListResponseData.

        [DEPRECATED] Please use either `gatewayEngineSeconds` or `obdEngineSeconds`.  # noqa: E501

        :param engine_seconds: The engine_seconds of this EquipmentStatsListResponseData.  # noqa: E501
        :type: list[EquipmentEngineSeconds]
        """

        self._engine_seconds = engine_seconds

    @property
    def engine_states(self):
        """Gets the engine_states of this EquipmentStatsListResponseData.  # noqa: E501

        [DEPRECATED] Please use either `gatewayEngineStates` or `obdEngineStates`.  # noqa: E501

        :return: The engine_states of this EquipmentStatsListResponseData.  # noqa: E501
        :rtype: list[EquipmentEngineState]
        """
        return self._engine_states

    @engine_states.setter
    def engine_states(self, engine_states):
        """Sets the engine_states of this EquipmentStatsListResponseData.

        [DEPRECATED] Please use either `gatewayEngineStates` or `obdEngineStates`.  # noqa: E501

        :param engine_states: The engine_states of this EquipmentStatsListResponseData.  # noqa: E501
        :type: list[EquipmentEngineState]
        """

        self._engine_states = engine_states

    @property
    def fuel_percent(self):
        """Gets the fuel_percent of this EquipmentStatsListResponseData.  # noqa: E501

        A time-series of fuel percent level changes for the given unit of equipment.  # noqa: E501

        :return: The fuel_percent of this EquipmentStatsListResponseData.  # noqa: E501
        :rtype: list[EquipmentFuelPercent]
        """
        return self._fuel_percent

    @fuel_percent.setter
    def fuel_percent(self, fuel_percent):
        """Sets the fuel_percent of this EquipmentStatsListResponseData.

        A time-series of fuel percent level changes for the given unit of equipment.  # noqa: E501

        :param fuel_percent: The fuel_percent of this EquipmentStatsListResponseData.  # noqa: E501
        :type: list[EquipmentFuelPercent]
        """

        self._fuel_percent = fuel_percent

    @property
    def gateway_engine_seconds(self):
        """Gets the gateway_engine_seconds of this EquipmentStatsListResponseData.  # noqa: E501

        A time-series of engine seconds readings for the given unit of equipment. (An approximate based on readings from the AG24's aux/digio cable.)  # noqa: E501

        :return: The gateway_engine_seconds of this EquipmentStatsListResponseData.  # noqa: E501
        :rtype: list[EquipmentGatewayEngineSeconds]
        """
        return self._gateway_engine_seconds

    @gateway_engine_seconds.setter
    def gateway_engine_seconds(self, gateway_engine_seconds):
        """Sets the gateway_engine_seconds of this EquipmentStatsListResponseData.

        A time-series of engine seconds readings for the given unit of equipment. (An approximate based on readings from the AG24's aux/digio cable.)  # noqa: E501

        :param gateway_engine_seconds: The gateway_engine_seconds of this EquipmentStatsListResponseData.  # noqa: E501
        :type: list[EquipmentGatewayEngineSeconds]
        """

        self._gateway_engine_seconds = gateway_engine_seconds

    @property
    def gateway_engine_state(self):
        """Gets the gateway_engine_state of this EquipmentStatsListResponseData.  # noqa: E501

        A time-series of engine state changes (as read from the AG24's aux/digio cable) for the given unit of equipment.  # noqa: E501

        :return: The gateway_engine_state of this EquipmentStatsListResponseData.  # noqa: E501
        :rtype: list[EquipmentGatewayEngineState]
        """
        return self._gateway_engine_state

    @gateway_engine_state.setter
    def gateway_engine_state(self, gateway_engine_state):
        """Sets the gateway_engine_state of this EquipmentStatsListResponseData.

        A time-series of engine state changes (as read from the AG24's aux/digio cable) for the given unit of equipment.  # noqa: E501

        :param gateway_engine_state: The gateway_engine_state of this EquipmentStatsListResponseData.  # noqa: E501
        :type: list[EquipmentGatewayEngineState]
        """

        self._gateway_engine_state = gateway_engine_state

    @property
    def gps_odometer_meters(self):
        """Gets the gps_odometer_meters of this EquipmentStatsListResponseData.  # noqa: E501

        A time-series of GPS odometer readings for the given unit of equipment.  # noqa: E501

        :return: The gps_odometer_meters of this EquipmentStatsListResponseData.  # noqa: E501
        :rtype: list[EquipmentGpsOdometerMeters]
        """
        return self._gps_odometer_meters

    @gps_odometer_meters.setter
    def gps_odometer_meters(self, gps_odometer_meters):
        """Sets the gps_odometer_meters of this EquipmentStatsListResponseData.

        A time-series of GPS odometer readings for the given unit of equipment.  # noqa: E501

        :param gps_odometer_meters: The gps_odometer_meters of this EquipmentStatsListResponseData.  # noqa: E501
        :type: list[EquipmentGpsOdometerMeters]
        """

        self._gps_odometer_meters = gps_odometer_meters

    @property
    def id(self):
        """Gets the id of this EquipmentStatsListResponseData.  # noqa: E501

        Unique Samsara ID for the equipment.  # noqa: E501

        :return: The id of this EquipmentStatsListResponseData.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EquipmentStatsListResponseData.

        Unique Samsara ID for the equipment.  # noqa: E501

        :param id: The id of this EquipmentStatsListResponseData.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this EquipmentStatsListResponseData.  # noqa: E501

        Name of the equipment.  # noqa: E501

        :return: The name of this EquipmentStatsListResponseData.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EquipmentStatsListResponseData.

        Name of the equipment.  # noqa: E501

        :param name: The name of this EquipmentStatsListResponseData.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def obd_engine_seconds(self):
        """Gets the obd_engine_seconds of this EquipmentStatsListResponseData.  # noqa: E501

        A time-series of engine state changes for the given unit of equipment. (As directly from on-board diagnostics.)  # noqa: E501

        :return: The obd_engine_seconds of this EquipmentStatsListResponseData.  # noqa: E501
        :rtype: list[EquipmentObdEngineSeconds]
        """
        return self._obd_engine_seconds

    @obd_engine_seconds.setter
    def obd_engine_seconds(self, obd_engine_seconds):
        """Sets the obd_engine_seconds of this EquipmentStatsListResponseData.

        A time-series of engine state changes for the given unit of equipment. (As directly from on-board diagnostics.)  # noqa: E501

        :param obd_engine_seconds: The obd_engine_seconds of this EquipmentStatsListResponseData.  # noqa: E501
        :type: list[EquipmentObdEngineSeconds]
        """

        self._obd_engine_seconds = obd_engine_seconds

    @property
    def obd_engine_state(self):
        """Gets the obd_engine_state of this EquipmentStatsListResponseData.  # noqa: E501

        A time-series of engine state changes (as read from on-board diagnostics) for the given unit of equipment.  # noqa: E501

        :return: The obd_engine_state of this EquipmentStatsListResponseData.  # noqa: E501
        :rtype: list[EquipmentObdEngineState]
        """
        return self._obd_engine_state

    @obd_engine_state.setter
    def obd_engine_state(self, obd_engine_state):
        """Sets the obd_engine_state of this EquipmentStatsListResponseData.

        A time-series of engine state changes (as read from on-board diagnostics) for the given unit of equipment.  # noqa: E501

        :param obd_engine_state: The obd_engine_state of this EquipmentStatsListResponseData.  # noqa: E501
        :type: list[EquipmentObdEngineState]
        """

        self._obd_engine_state = obd_engine_state

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, EquipmentStatsListResponseData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EquipmentStatsListResponseData):
            return True

        return self.to_dict() != other.to_dict()