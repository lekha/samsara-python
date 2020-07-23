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


class VehicleStatsListGps(object):
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
        'heading_degrees': 'float',
        'latitude': 'float',
        'longitude': 'float',
        'reverse_geo': 'VehicleLocationReverseGeo',
        'speed_miles_per_hour': 'float',
        'time': 'str'
    }

    attribute_map = {
        'decorations': 'decorations',
        'heading_degrees': 'headingDegrees',
        'latitude': 'latitude',
        'longitude': 'longitude',
        'reverse_geo': 'reverseGeo',
        'speed_miles_per_hour': 'speedMilesPerHour',
        'time': 'time'
    }

    def __init__(self, decorations=None, heading_degrees=None, latitude=None, longitude=None, reverse_geo=None, speed_miles_per_hour=None, time=None, local_vars_configuration=None):  # noqa: E501
        """VehicleStatsListGps - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._decorations = None
        self._heading_degrees = None
        self._latitude = None
        self._longitude = None
        self._reverse_geo = None
        self._speed_miles_per_hour = None
        self._time = None
        self.discriminator = None

        if decorations is not None:
            self.decorations = decorations
        if heading_degrees is not None:
            self.heading_degrees = heading_degrees
        self.latitude = latitude
        self.longitude = longitude
        if reverse_geo is not None:
            self.reverse_geo = reverse_geo
        if speed_miles_per_hour is not None:
            self.speed_miles_per_hour = speed_miles_per_hour
        self.time = time

    @property
    def decorations(self):
        """Gets the decorations of this VehicleStatsListGps.  # noqa: E501


        :return: The decorations of this VehicleStatsListGps.  # noqa: E501
        :rtype: VehicleStatsDecorations
        """
        return self._decorations

    @decorations.setter
    def decorations(self, decorations):
        """Sets the decorations of this VehicleStatsListGps.


        :param decorations: The decorations of this VehicleStatsListGps.  # noqa: E501
        :type: VehicleStatsDecorations
        """

        self._decorations = decorations

    @property
    def heading_degrees(self):
        """Gets the heading_degrees of this VehicleStatsListGps.  # noqa: E501

        Heading of the vehicle in degrees.  # noqa: E501

        :return: The heading_degrees of this VehicleStatsListGps.  # noqa: E501
        :rtype: float
        """
        return self._heading_degrees

    @heading_degrees.setter
    def heading_degrees(self, heading_degrees):
        """Sets the heading_degrees of this VehicleStatsListGps.

        Heading of the vehicle in degrees.  # noqa: E501

        :param heading_degrees: The heading_degrees of this VehicleStatsListGps.  # noqa: E501
        :type: float
        """

        self._heading_degrees = heading_degrees

    @property
    def latitude(self):
        """Gets the latitude of this VehicleStatsListGps.  # noqa: E501

        GPS latitude represented in degrees  # noqa: E501

        :return: The latitude of this VehicleStatsListGps.  # noqa: E501
        :rtype: float
        """
        return self._latitude

    @latitude.setter
    def latitude(self, latitude):
        """Sets the latitude of this VehicleStatsListGps.

        GPS latitude represented in degrees  # noqa: E501

        :param latitude: The latitude of this VehicleStatsListGps.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and latitude is None:  # noqa: E501
            raise ValueError("Invalid value for `latitude`, must not be `None`")  # noqa: E501

        self._latitude = latitude

    @property
    def longitude(self):
        """Gets the longitude of this VehicleStatsListGps.  # noqa: E501

        GPS longitude represented in degrees  # noqa: E501

        :return: The longitude of this VehicleStatsListGps.  # noqa: E501
        :rtype: float
        """
        return self._longitude

    @longitude.setter
    def longitude(self, longitude):
        """Sets the longitude of this VehicleStatsListGps.

        GPS longitude represented in degrees  # noqa: E501

        :param longitude: The longitude of this VehicleStatsListGps.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and longitude is None:  # noqa: E501
            raise ValueError("Invalid value for `longitude`, must not be `None`")  # noqa: E501

        self._longitude = longitude

    @property
    def reverse_geo(self):
        """Gets the reverse_geo of this VehicleStatsListGps.  # noqa: E501


        :return: The reverse_geo of this VehicleStatsListGps.  # noqa: E501
        :rtype: VehicleLocationReverseGeo
        """
        return self._reverse_geo

    @reverse_geo.setter
    def reverse_geo(self, reverse_geo):
        """Sets the reverse_geo of this VehicleStatsListGps.


        :param reverse_geo: The reverse_geo of this VehicleStatsListGps.  # noqa: E501
        :type: VehicleLocationReverseGeo
        """

        self._reverse_geo = reverse_geo

    @property
    def speed_miles_per_hour(self):
        """Gets the speed_miles_per_hour of this VehicleStatsListGps.  # noqa: E501

        GPS speed of the vehicle in miles per hour.  # noqa: E501

        :return: The speed_miles_per_hour of this VehicleStatsListGps.  # noqa: E501
        :rtype: float
        """
        return self._speed_miles_per_hour

    @speed_miles_per_hour.setter
    def speed_miles_per_hour(self, speed_miles_per_hour):
        """Sets the speed_miles_per_hour of this VehicleStatsListGps.

        GPS speed of the vehicle in miles per hour.  # noqa: E501

        :param speed_miles_per_hour: The speed_miles_per_hour of this VehicleStatsListGps.  # noqa: E501
        :type: float
        """

        self._speed_miles_per_hour = speed_miles_per_hour

    @property
    def time(self):
        """Gets the time of this VehicleStatsListGps.  # noqa: E501

        UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`.  # noqa: E501

        :return: The time of this VehicleStatsListGps.  # noqa: E501
        :rtype: str
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this VehicleStatsListGps.

        UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`.  # noqa: E501

        :param time: The time of this VehicleStatsListGps.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and time is None:  # noqa: E501
            raise ValueError("Invalid value for `time`, must not be `None`")  # noqa: E501

        self._time = time

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
        if not isinstance(other, VehicleStatsListGps):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VehicleStatsListGps):
            return True

        return self.to_dict() != other.to_dict()
