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


class VehicleStatsFaultCodesValue(object):
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
        'can_bus_type': 'str',
        'j1939': 'VehicleStatsFaultCodesValueJ1939',
        'obdii': 'VehicleStatsFaultCodesValueObdii'
    }

    attribute_map = {
        'can_bus_type': 'canBusType',
        'j1939': 'j1939',
        'obdii': 'obdii'
    }

    def __init__(self, can_bus_type=None, j1939=None, obdii=None, local_vars_configuration=None):  # noqa: E501
        """VehicleStatsFaultCodesValue - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._can_bus_type = None
        self._j1939 = None
        self._obdii = None
        self.discriminator = None

        if can_bus_type is not None:
            self.can_bus_type = can_bus_type
        if j1939 is not None:
            self.j1939 = j1939
        if obdii is not None:
            self.obdii = obdii

    @property
    def can_bus_type(self):
        """Gets the can_bus_type of this VehicleStatsFaultCodesValue.  # noqa: E501

        The CAN bus type of the vehicle.  # noqa: E501

        :return: The can_bus_type of this VehicleStatsFaultCodesValue.  # noqa: E501
        :rtype: str
        """
        return self._can_bus_type

    @can_bus_type.setter
    def can_bus_type(self, can_bus_type):
        """Sets the can_bus_type of this VehicleStatsFaultCodesValue.

        The CAN bus type of the vehicle.  # noqa: E501

        :param can_bus_type: The can_bus_type of this VehicleStatsFaultCodesValue.  # noqa: E501
        :type: str
        """

        self._can_bus_type = can_bus_type

    @property
    def j1939(self):
        """Gets the j1939 of this VehicleStatsFaultCodesValue.  # noqa: E501


        :return: The j1939 of this VehicleStatsFaultCodesValue.  # noqa: E501
        :rtype: VehicleStatsFaultCodesValueJ1939
        """
        return self._j1939

    @j1939.setter
    def j1939(self, j1939):
        """Sets the j1939 of this VehicleStatsFaultCodesValue.


        :param j1939: The j1939 of this VehicleStatsFaultCodesValue.  # noqa: E501
        :type: VehicleStatsFaultCodesValueJ1939
        """

        self._j1939 = j1939

    @property
    def obdii(self):
        """Gets the obdii of this VehicleStatsFaultCodesValue.  # noqa: E501


        :return: The obdii of this VehicleStatsFaultCodesValue.  # noqa: E501
        :rtype: VehicleStatsFaultCodesValueObdii
        """
        return self._obdii

    @obdii.setter
    def obdii(self, obdii):
        """Sets the obdii of this VehicleStatsFaultCodesValue.


        :param obdii: The obdii of this VehicleStatsFaultCodesValue.  # noqa: E501
        :type: VehicleStatsFaultCodesValueObdii
        """

        self._obdii = obdii

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
        if not isinstance(other, VehicleStatsFaultCodesValue):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VehicleStatsFaultCodesValue):
            return True

        return self.to_dict() != other.to_dict()
