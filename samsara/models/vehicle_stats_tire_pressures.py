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


class VehicleStatsTirePressures(object):
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
        'back_left_tire_pressure_k_pa': 'int',
        'back_right_tire_pressure_k_pa': 'int',
        'front_left_tire_pressure_k_pa': 'int',
        'front_right_tire_pressure_k_pa': 'int'
    }

    attribute_map = {
        'back_left_tire_pressure_k_pa': 'backLeftTirePressureKPa',
        'back_right_tire_pressure_k_pa': 'backRightTirePressureKPa',
        'front_left_tire_pressure_k_pa': 'frontLeftTirePressureKPa',
        'front_right_tire_pressure_k_pa': 'frontRightTirePressureKPa'
    }

    def __init__(self, back_left_tire_pressure_k_pa=None, back_right_tire_pressure_k_pa=None, front_left_tire_pressure_k_pa=None, front_right_tire_pressure_k_pa=None, local_vars_configuration=None):  # noqa: E501
        """VehicleStatsTirePressures - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._back_left_tire_pressure_k_pa = None
        self._back_right_tire_pressure_k_pa = None
        self._front_left_tire_pressure_k_pa = None
        self._front_right_tire_pressure_k_pa = None
        self.discriminator = None

        if back_left_tire_pressure_k_pa is not None:
            self.back_left_tire_pressure_k_pa = back_left_tire_pressure_k_pa
        if back_right_tire_pressure_k_pa is not None:
            self.back_right_tire_pressure_k_pa = back_right_tire_pressure_k_pa
        if front_left_tire_pressure_k_pa is not None:
            self.front_left_tire_pressure_k_pa = front_left_tire_pressure_k_pa
        if front_right_tire_pressure_k_pa is not None:
            self.front_right_tire_pressure_k_pa = front_right_tire_pressure_k_pa

    @property
    def back_left_tire_pressure_k_pa(self):
        """Gets the back_left_tire_pressure_k_pa of this VehicleStatsTirePressures.  # noqa: E501

        The tire pressure of the rear left tire as seen when standing behind the vehicle in kilopascals.  # noqa: E501

        :return: The back_left_tire_pressure_k_pa of this VehicleStatsTirePressures.  # noqa: E501
        :rtype: int
        """
        return self._back_left_tire_pressure_k_pa

    @back_left_tire_pressure_k_pa.setter
    def back_left_tire_pressure_k_pa(self, back_left_tire_pressure_k_pa):
        """Sets the back_left_tire_pressure_k_pa of this VehicleStatsTirePressures.

        The tire pressure of the rear left tire as seen when standing behind the vehicle in kilopascals.  # noqa: E501

        :param back_left_tire_pressure_k_pa: The back_left_tire_pressure_k_pa of this VehicleStatsTirePressures.  # noqa: E501
        :type: int
        """

        self._back_left_tire_pressure_k_pa = back_left_tire_pressure_k_pa

    @property
    def back_right_tire_pressure_k_pa(self):
        """Gets the back_right_tire_pressure_k_pa of this VehicleStatsTirePressures.  # noqa: E501

        The tire pressure of the rear right tire as seen when standing behind the vehicle in kilopascals.  # noqa: E501

        :return: The back_right_tire_pressure_k_pa of this VehicleStatsTirePressures.  # noqa: E501
        :rtype: int
        """
        return self._back_right_tire_pressure_k_pa

    @back_right_tire_pressure_k_pa.setter
    def back_right_tire_pressure_k_pa(self, back_right_tire_pressure_k_pa):
        """Sets the back_right_tire_pressure_k_pa of this VehicleStatsTirePressures.

        The tire pressure of the rear right tire as seen when standing behind the vehicle in kilopascals.  # noqa: E501

        :param back_right_tire_pressure_k_pa: The back_right_tire_pressure_k_pa of this VehicleStatsTirePressures.  # noqa: E501
        :type: int
        """

        self._back_right_tire_pressure_k_pa = back_right_tire_pressure_k_pa

    @property
    def front_left_tire_pressure_k_pa(self):
        """Gets the front_left_tire_pressure_k_pa of this VehicleStatsTirePressures.  # noqa: E501

        The tire pressure of the front left tire as seen when standing behind the vehicle in kilopascals.  # noqa: E501

        :return: The front_left_tire_pressure_k_pa of this VehicleStatsTirePressures.  # noqa: E501
        :rtype: int
        """
        return self._front_left_tire_pressure_k_pa

    @front_left_tire_pressure_k_pa.setter
    def front_left_tire_pressure_k_pa(self, front_left_tire_pressure_k_pa):
        """Sets the front_left_tire_pressure_k_pa of this VehicleStatsTirePressures.

        The tire pressure of the front left tire as seen when standing behind the vehicle in kilopascals.  # noqa: E501

        :param front_left_tire_pressure_k_pa: The front_left_tire_pressure_k_pa of this VehicleStatsTirePressures.  # noqa: E501
        :type: int
        """

        self._front_left_tire_pressure_k_pa = front_left_tire_pressure_k_pa

    @property
    def front_right_tire_pressure_k_pa(self):
        """Gets the front_right_tire_pressure_k_pa of this VehicleStatsTirePressures.  # noqa: E501

        The tire pressure of the front right tire as seen when standing behind the vehicle in kilopascals.  # noqa: E501

        :return: The front_right_tire_pressure_k_pa of this VehicleStatsTirePressures.  # noqa: E501
        :rtype: int
        """
        return self._front_right_tire_pressure_k_pa

    @front_right_tire_pressure_k_pa.setter
    def front_right_tire_pressure_k_pa(self, front_right_tire_pressure_k_pa):
        """Sets the front_right_tire_pressure_k_pa of this VehicleStatsTirePressures.

        The tire pressure of the front right tire as seen when standing behind the vehicle in kilopascals.  # noqa: E501

        :param front_right_tire_pressure_k_pa: The front_right_tire_pressure_k_pa of this VehicleStatsTirePressures.  # noqa: E501
        :type: int
        """

        self._front_right_tire_pressure_k_pa = front_right_tire_pressure_k_pa

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
        if not isinstance(other, VehicleStatsTirePressures):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VehicleStatsTirePressures):
            return True

        return self.to_dict() != other.to_dict()