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


class VehicleStatsListResponseObdiiMonitorStatus(object):
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
        'catalyst': 'str',
        'comprehensive': 'str',
        'egr': 'str',
        'evap_system': 'str',
        'fuel': 'str',
        'heated_catalyst': 'str',
        'heated_o2_sensor': 'str',
        'iso_sae_reserved': 'str',
        'misfire': 'str',
        'not_ready_count': 'int',
        'o2_sensor': 'str',
        'secondary_air': 'str'
    }

    attribute_map = {
        'catalyst': 'catalyst',
        'comprehensive': 'comprehensive',
        'egr': 'egr',
        'evap_system': 'evapSystem',
        'fuel': 'fuel',
        'heated_catalyst': 'heatedCatalyst',
        'heated_o2_sensor': 'heatedO2Sensor',
        'iso_sae_reserved': 'isoSaeReserved',
        'misfire': 'misfire',
        'not_ready_count': 'notReadyCount',
        'o2_sensor': 'o2Sensor',
        'secondary_air': 'secondaryAir'
    }

    def __init__(self, catalyst=None, comprehensive=None, egr=None, evap_system=None, fuel=None, heated_catalyst=None, heated_o2_sensor=None, iso_sae_reserved=None, misfire=None, not_ready_count=None, o2_sensor=None, secondary_air=None, local_vars_configuration=None):  # noqa: E501
        """VehicleStatsListResponseObdiiMonitorStatus - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._catalyst = None
        self._comprehensive = None
        self._egr = None
        self._evap_system = None
        self._fuel = None
        self._heated_catalyst = None
        self._heated_o2_sensor = None
        self._iso_sae_reserved = None
        self._misfire = None
        self._not_ready_count = None
        self._o2_sensor = None
        self._secondary_air = None
        self.discriminator = None

        if catalyst is not None:
            self.catalyst = catalyst
        if comprehensive is not None:
            self.comprehensive = comprehensive
        if egr is not None:
            self.egr = egr
        if evap_system is not None:
            self.evap_system = evap_system
        if fuel is not None:
            self.fuel = fuel
        if heated_catalyst is not None:
            self.heated_catalyst = heated_catalyst
        if heated_o2_sensor is not None:
            self.heated_o2_sensor = heated_o2_sensor
        if iso_sae_reserved is not None:
            self.iso_sae_reserved = iso_sae_reserved
        if misfire is not None:
            self.misfire = misfire
        if not_ready_count is not None:
            self.not_ready_count = not_ready_count
        if o2_sensor is not None:
            self.o2_sensor = o2_sensor
        if secondary_air is not None:
            self.secondary_air = secondary_air

    @property
    def catalyst(self):
        """Gets the catalyst of this VehicleStatsListResponseObdiiMonitorStatus.  # noqa: E501

        Enum of monitor status: -U: Unsupported -N: Not Complete -R: Complete   # noqa: E501

        :return: The catalyst of this VehicleStatsListResponseObdiiMonitorStatus.  # noqa: E501
        :rtype: str
        """
        return self._catalyst

    @catalyst.setter
    def catalyst(self, catalyst):
        """Sets the catalyst of this VehicleStatsListResponseObdiiMonitorStatus.

        Enum of monitor status: -U: Unsupported -N: Not Complete -R: Complete   # noqa: E501

        :param catalyst: The catalyst of this VehicleStatsListResponseObdiiMonitorStatus.  # noqa: E501
        :type: str
        """
        allowed_values = ["N", "R", "U"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and catalyst not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `catalyst` ({0}), must be one of {1}"  # noqa: E501
                .format(catalyst, allowed_values)
            )

        self._catalyst = catalyst

    @property
    def comprehensive(self):
        """Gets the comprehensive of this VehicleStatsListResponseObdiiMonitorStatus.  # noqa: E501

        Enum of monitor status: -U: Unsupported -N: Not Complete -R: Complete   # noqa: E501

        :return: The comprehensive of this VehicleStatsListResponseObdiiMonitorStatus.  # noqa: E501
        :rtype: str
        """
        return self._comprehensive

    @comprehensive.setter
    def comprehensive(self, comprehensive):
        """Sets the comprehensive of this VehicleStatsListResponseObdiiMonitorStatus.

        Enum of monitor status: -U: Unsupported -N: Not Complete -R: Complete   # noqa: E501

        :param comprehensive: The comprehensive of this VehicleStatsListResponseObdiiMonitorStatus.  # noqa: E501
        :type: str
        """
        allowed_values = ["N", "R", "U"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and comprehensive not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `comprehensive` ({0}), must be one of {1}"  # noqa: E501
                .format(comprehensive, allowed_values)
            )

        self._comprehensive = comprehensive

    @property
    def egr(self):
        """Gets the egr of this VehicleStatsListResponseObdiiMonitorStatus.  # noqa: E501

        Enum of monitor status: -U: Unsupported -N: Not Complete -R: Complete   # noqa: E501

        :return: The egr of this VehicleStatsListResponseObdiiMonitorStatus.  # noqa: E501
        :rtype: str
        """
        return self._egr

    @egr.setter
    def egr(self, egr):
        """Sets the egr of this VehicleStatsListResponseObdiiMonitorStatus.

        Enum of monitor status: -U: Unsupported -N: Not Complete -R: Complete   # noqa: E501

        :param egr: The egr of this VehicleStatsListResponseObdiiMonitorStatus.  # noqa: E501
        :type: str
        """
        allowed_values = ["N", "R", "U"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and egr not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `egr` ({0}), must be one of {1}"  # noqa: E501
                .format(egr, allowed_values)
            )

        self._egr = egr

    @property
    def evap_system(self):
        """Gets the evap_system of this VehicleStatsListResponseObdiiMonitorStatus.  # noqa: E501

        Enum of monitor status: -U: Unsupported -N: Not Complete -R: Complete   # noqa: E501

        :return: The evap_system of this VehicleStatsListResponseObdiiMonitorStatus.  # noqa: E501
        :rtype: str
        """
        return self._evap_system

    @evap_system.setter
    def evap_system(self, evap_system):
        """Sets the evap_system of this VehicleStatsListResponseObdiiMonitorStatus.

        Enum of monitor status: -U: Unsupported -N: Not Complete -R: Complete   # noqa: E501

        :param evap_system: The evap_system of this VehicleStatsListResponseObdiiMonitorStatus.  # noqa: E501
        :type: str
        """
        allowed_values = ["N", "R", "U"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and evap_system not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `evap_system` ({0}), must be one of {1}"  # noqa: E501
                .format(evap_system, allowed_values)
            )

        self._evap_system = evap_system

    @property
    def fuel(self):
        """Gets the fuel of this VehicleStatsListResponseObdiiMonitorStatus.  # noqa: E501

        Enum of monitor status: -U: Unsupported -N: Not Complete -R: Complete   # noqa: E501

        :return: The fuel of this VehicleStatsListResponseObdiiMonitorStatus.  # noqa: E501
        :rtype: str
        """
        return self._fuel

    @fuel.setter
    def fuel(self, fuel):
        """Sets the fuel of this VehicleStatsListResponseObdiiMonitorStatus.

        Enum of monitor status: -U: Unsupported -N: Not Complete -R: Complete   # noqa: E501

        :param fuel: The fuel of this VehicleStatsListResponseObdiiMonitorStatus.  # noqa: E501
        :type: str
        """
        allowed_values = ["N", "R", "U"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and fuel not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `fuel` ({0}), must be one of {1}"  # noqa: E501
                .format(fuel, allowed_values)
            )

        self._fuel = fuel

    @property
    def heated_catalyst(self):
        """Gets the heated_catalyst of this VehicleStatsListResponseObdiiMonitorStatus.  # noqa: E501

        Enum of monitor status: -U: Unsupported -N: Not Complete -R: Complete   # noqa: E501

        :return: The heated_catalyst of this VehicleStatsListResponseObdiiMonitorStatus.  # noqa: E501
        :rtype: str
        """
        return self._heated_catalyst

    @heated_catalyst.setter
    def heated_catalyst(self, heated_catalyst):
        """Sets the heated_catalyst of this VehicleStatsListResponseObdiiMonitorStatus.

        Enum of monitor status: -U: Unsupported -N: Not Complete -R: Complete   # noqa: E501

        :param heated_catalyst: The heated_catalyst of this VehicleStatsListResponseObdiiMonitorStatus.  # noqa: E501
        :type: str
        """
        allowed_values = ["N", "R", "U"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and heated_catalyst not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `heated_catalyst` ({0}), must be one of {1}"  # noqa: E501
                .format(heated_catalyst, allowed_values)
            )

        self._heated_catalyst = heated_catalyst

    @property
    def heated_o2_sensor(self):
        """Gets the heated_o2_sensor of this VehicleStatsListResponseObdiiMonitorStatus.  # noqa: E501

        Enum of monitor status: -U: Unsupported -N: Not Complete -R: Complete   # noqa: E501

        :return: The heated_o2_sensor of this VehicleStatsListResponseObdiiMonitorStatus.  # noqa: E501
        :rtype: str
        """
        return self._heated_o2_sensor

    @heated_o2_sensor.setter
    def heated_o2_sensor(self, heated_o2_sensor):
        """Sets the heated_o2_sensor of this VehicleStatsListResponseObdiiMonitorStatus.

        Enum of monitor status: -U: Unsupported -N: Not Complete -R: Complete   # noqa: E501

        :param heated_o2_sensor: The heated_o2_sensor of this VehicleStatsListResponseObdiiMonitorStatus.  # noqa: E501
        :type: str
        """
        allowed_values = ["N", "R", "U"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and heated_o2_sensor not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `heated_o2_sensor` ({0}), must be one of {1}"  # noqa: E501
                .format(heated_o2_sensor, allowed_values)
            )

        self._heated_o2_sensor = heated_o2_sensor

    @property
    def iso_sae_reserved(self):
        """Gets the iso_sae_reserved of this VehicleStatsListResponseObdiiMonitorStatus.  # noqa: E501

        Enum of monitor status: -U: Unsupported -N: Not Complete -R: Complete   # noqa: E501

        :return: The iso_sae_reserved of this VehicleStatsListResponseObdiiMonitorStatus.  # noqa: E501
        :rtype: str
        """
        return self._iso_sae_reserved

    @iso_sae_reserved.setter
    def iso_sae_reserved(self, iso_sae_reserved):
        """Sets the iso_sae_reserved of this VehicleStatsListResponseObdiiMonitorStatus.

        Enum of monitor status: -U: Unsupported -N: Not Complete -R: Complete   # noqa: E501

        :param iso_sae_reserved: The iso_sae_reserved of this VehicleStatsListResponseObdiiMonitorStatus.  # noqa: E501
        :type: str
        """
        allowed_values = ["N", "R", "U"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and iso_sae_reserved not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `iso_sae_reserved` ({0}), must be one of {1}"  # noqa: E501
                .format(iso_sae_reserved, allowed_values)
            )

        self._iso_sae_reserved = iso_sae_reserved

    @property
    def misfire(self):
        """Gets the misfire of this VehicleStatsListResponseObdiiMonitorStatus.  # noqa: E501

        Enum of monitor status: -U: Unsupported -N: Not Complete -R: Complete   # noqa: E501

        :return: The misfire of this VehicleStatsListResponseObdiiMonitorStatus.  # noqa: E501
        :rtype: str
        """
        return self._misfire

    @misfire.setter
    def misfire(self, misfire):
        """Sets the misfire of this VehicleStatsListResponseObdiiMonitorStatus.

        Enum of monitor status: -U: Unsupported -N: Not Complete -R: Complete   # noqa: E501

        :param misfire: The misfire of this VehicleStatsListResponseObdiiMonitorStatus.  # noqa: E501
        :type: str
        """
        allowed_values = ["N", "R", "U"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and misfire not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `misfire` ({0}), must be one of {1}"  # noqa: E501
                .format(misfire, allowed_values)
            )

        self._misfire = misfire

    @property
    def not_ready_count(self):
        """Gets the not_ready_count of this VehicleStatsListResponseObdiiMonitorStatus.  # noqa: E501

        Count of the number of sensors reporting N: Not Complete  # noqa: E501

        :return: The not_ready_count of this VehicleStatsListResponseObdiiMonitorStatus.  # noqa: E501
        :rtype: int
        """
        return self._not_ready_count

    @not_ready_count.setter
    def not_ready_count(self, not_ready_count):
        """Sets the not_ready_count of this VehicleStatsListResponseObdiiMonitorStatus.

        Count of the number of sensors reporting N: Not Complete  # noqa: E501

        :param not_ready_count: The not_ready_count of this VehicleStatsListResponseObdiiMonitorStatus.  # noqa: E501
        :type: int
        """

        self._not_ready_count = not_ready_count

    @property
    def o2_sensor(self):
        """Gets the o2_sensor of this VehicleStatsListResponseObdiiMonitorStatus.  # noqa: E501

        Enum of monitor status: -U: Unsupported -N: Not Complete -R: Complete   # noqa: E501

        :return: The o2_sensor of this VehicleStatsListResponseObdiiMonitorStatus.  # noqa: E501
        :rtype: str
        """
        return self._o2_sensor

    @o2_sensor.setter
    def o2_sensor(self, o2_sensor):
        """Sets the o2_sensor of this VehicleStatsListResponseObdiiMonitorStatus.

        Enum of monitor status: -U: Unsupported -N: Not Complete -R: Complete   # noqa: E501

        :param o2_sensor: The o2_sensor of this VehicleStatsListResponseObdiiMonitorStatus.  # noqa: E501
        :type: str
        """
        allowed_values = ["N", "R", "U"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and o2_sensor not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `o2_sensor` ({0}), must be one of {1}"  # noqa: E501
                .format(o2_sensor, allowed_values)
            )

        self._o2_sensor = o2_sensor

    @property
    def secondary_air(self):
        """Gets the secondary_air of this VehicleStatsListResponseObdiiMonitorStatus.  # noqa: E501

        Enum of monitor status: -U: Unsupported -N: Not Complete -R: Complete   # noqa: E501

        :return: The secondary_air of this VehicleStatsListResponseObdiiMonitorStatus.  # noqa: E501
        :rtype: str
        """
        return self._secondary_air

    @secondary_air.setter
    def secondary_air(self, secondary_air):
        """Sets the secondary_air of this VehicleStatsListResponseObdiiMonitorStatus.

        Enum of monitor status: -U: Unsupported -N: Not Complete -R: Complete   # noqa: E501

        :param secondary_air: The secondary_air of this VehicleStatsListResponseObdiiMonitorStatus.  # noqa: E501
        :type: str
        """
        allowed_values = ["N", "R", "U"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and secondary_air not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `secondary_air` ({0}), must be one of {1}"  # noqa: E501
                .format(secondary_air, allowed_values)
            )

        self._secondary_air = secondary_air

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
        if not isinstance(other, VehicleStatsListResponseObdiiMonitorStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VehicleStatsListResponseObdiiMonitorStatus):
            return True

        return self.to_dict() != other.to_dict()
