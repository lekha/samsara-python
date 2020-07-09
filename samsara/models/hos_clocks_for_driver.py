# coding: utf-8

"""
    Samsara API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 2020-06-15
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from samsara.configuration import Configuration


class HosClocksForDriver(object):
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
        'clocks': 'HosClocks',
        'current_duty_status': 'CurrentDutyStatus',
        'current_vehicle': 'VehicleTinyResponse',
        'driver': 'DriverTinyResponse',
        'violations': 'HosViolations'
    }

    attribute_map = {
        'clocks': 'clocks',
        'current_duty_status': 'currentDutyStatus',
        'current_vehicle': 'currentVehicle',
        'driver': 'driver',
        'violations': 'violations'
    }

    def __init__(self, clocks=None, current_duty_status=None, current_vehicle=None, driver=None, violations=None, local_vars_configuration=None):  # noqa: E501
        """HosClocksForDriver - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._clocks = None
        self._current_duty_status = None
        self._current_vehicle = None
        self._driver = None
        self._violations = None
        self.discriminator = None

        if clocks is not None:
            self.clocks = clocks
        if current_duty_status is not None:
            self.current_duty_status = current_duty_status
        if current_vehicle is not None:
            self.current_vehicle = current_vehicle
        if driver is not None:
            self.driver = driver
        if violations is not None:
            self.violations = violations

    @property
    def clocks(self):
        """Gets the clocks of this HosClocksForDriver.  # noqa: E501


        :return: The clocks of this HosClocksForDriver.  # noqa: E501
        :rtype: HosClocks
        """
        return self._clocks

    @clocks.setter
    def clocks(self, clocks):
        """Sets the clocks of this HosClocksForDriver.


        :param clocks: The clocks of this HosClocksForDriver.  # noqa: E501
        :type: HosClocks
        """

        self._clocks = clocks

    @property
    def current_duty_status(self):
        """Gets the current_duty_status of this HosClocksForDriver.  # noqa: E501


        :return: The current_duty_status of this HosClocksForDriver.  # noqa: E501
        :rtype: CurrentDutyStatus
        """
        return self._current_duty_status

    @current_duty_status.setter
    def current_duty_status(self, current_duty_status):
        """Sets the current_duty_status of this HosClocksForDriver.


        :param current_duty_status: The current_duty_status of this HosClocksForDriver.  # noqa: E501
        :type: CurrentDutyStatus
        """

        self._current_duty_status = current_duty_status

    @property
    def current_vehicle(self):
        """Gets the current_vehicle of this HosClocksForDriver.  # noqa: E501


        :return: The current_vehicle of this HosClocksForDriver.  # noqa: E501
        :rtype: VehicleTinyResponse
        """
        return self._current_vehicle

    @current_vehicle.setter
    def current_vehicle(self, current_vehicle):
        """Sets the current_vehicle of this HosClocksForDriver.


        :param current_vehicle: The current_vehicle of this HosClocksForDriver.  # noqa: E501
        :type: VehicleTinyResponse
        """

        self._current_vehicle = current_vehicle

    @property
    def driver(self):
        """Gets the driver of this HosClocksForDriver.  # noqa: E501


        :return: The driver of this HosClocksForDriver.  # noqa: E501
        :rtype: DriverTinyResponse
        """
        return self._driver

    @driver.setter
    def driver(self, driver):
        """Sets the driver of this HosClocksForDriver.


        :param driver: The driver of this HosClocksForDriver.  # noqa: E501
        :type: DriverTinyResponse
        """

        self._driver = driver

    @property
    def violations(self):
        """Gets the violations of this HosClocksForDriver.  # noqa: E501


        :return: The violations of this HosClocksForDriver.  # noqa: E501
        :rtype: HosViolations
        """
        return self._violations

    @violations.setter
    def violations(self, violations):
        """Sets the violations of this HosClocksForDriver.


        :param violations: The violations of this HosClocksForDriver.  # noqa: E501
        :type: HosViolations
        """

        self._violations = violations

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
        if not isinstance(other, HosClocksForDriver):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, HosClocksForDriver):
            return True

        return self.to_dict() != other.to_dict()