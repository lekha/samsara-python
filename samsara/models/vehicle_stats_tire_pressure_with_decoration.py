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


class VehicleStatsTirePressureWithDecoration(object):
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
        'decorations': 'VehicleStatsDecorations',
        'time': 'str',
        'value': 'VehicleStatsTirePressures'
    }

    attribute_map = {
        'decorations': 'decorations',
        'time': 'time',
        'value': 'value'
    }

    def __init__(self, decorations=None, time=None, value=None, local_vars_configuration=None):  # noqa: E501
        """VehicleStatsTirePressureWithDecoration - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._decorations = None
        self._time = None
        self._value = None
        self.discriminator = None

        if decorations is not None:
            self.decorations = decorations
        if time is not None:
            self.time = time
        if value is not None:
            self.value = value

    @property
    def decorations(self):
        """Gets the decorations of this VehicleStatsTirePressureWithDecoration.  # noqa: E501


        :return: The decorations of this VehicleStatsTirePressureWithDecoration.  # noqa: E501
        :rtype: VehicleStatsDecorations
        """
        return self._decorations

    @decorations.setter
    def decorations(self, decorations):
        """Sets the decorations of this VehicleStatsTirePressureWithDecoration.


        :param decorations: The decorations of this VehicleStatsTirePressureWithDecoration.  # noqa: E501
        :type: VehicleStatsDecorations
        """

        self._decorations = decorations

    @property
    def time(self):
        """Gets the time of this VehicleStatsTirePressureWithDecoration.  # noqa: E501

        UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`.  # noqa: E501

        :return: The time of this VehicleStatsTirePressureWithDecoration.  # noqa: E501
        :rtype: str
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this VehicleStatsTirePressureWithDecoration.

        UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`.  # noqa: E501

        :param time: The time of this VehicleStatsTirePressureWithDecoration.  # noqa: E501
        :type: str
        """

        self._time = time

    @property
    def value(self):
        """Gets the value of this VehicleStatsTirePressureWithDecoration.  # noqa: E501


        :return: The value of this VehicleStatsTirePressureWithDecoration.  # noqa: E501
        :rtype: VehicleStatsTirePressures
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this VehicleStatsTirePressureWithDecoration.


        :param value: The value of this VehicleStatsTirePressureWithDecoration.  # noqa: E501
        :type: VehicleStatsTirePressures
        """

        self._value = value

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
        if not isinstance(other, VehicleStatsTirePressureWithDecoration):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VehicleStatsTirePressureWithDecoration):
            return True

        return self.to_dict() != other.to_dict()
