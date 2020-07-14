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


class LocationDataPointGpsLocation(object):
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
        'formatted_address': 'str',
        'gps_meters_per_second': 'float',
        'heading_degrees': 'float',
        'latitude': 'float',
        'longitude': 'float',
        'place': 'LocationDataPointGpsLocationPlace'
    }

    attribute_map = {
        'formatted_address': 'formattedAddress',
        'gps_meters_per_second': 'gpsMetersPerSecond',
        'heading_degrees': 'headingDegrees',
        'latitude': 'latitude',
        'longitude': 'longitude',
        'place': 'place'
    }

    def __init__(self, formatted_address=None, gps_meters_per_second=None, heading_degrees=None, latitude=None, longitude=None, place=None, local_vars_configuration=None):  # noqa: E501
        """LocationDataPointGpsLocation - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._formatted_address = None
        self._gps_meters_per_second = None
        self._heading_degrees = None
        self._latitude = None
        self._longitude = None
        self._place = None
        self.discriminator = None

        if formatted_address is not None:
            self.formatted_address = formatted_address
        if gps_meters_per_second is not None:
            self.gps_meters_per_second = gps_meters_per_second
        if heading_degrees is not None:
            self.heading_degrees = heading_degrees
        if latitude is not None:
            self.latitude = latitude
        if longitude is not None:
            self.longitude = longitude
        if place is not None:
            self.place = place

    @property
    def formatted_address(self):
        """Gets the formatted_address of this LocationDataPointGpsLocation.  # noqa: E501

        Formatted address of the location  # noqa: E501

        :return: The formatted_address of this LocationDataPointGpsLocation.  # noqa: E501
        :rtype: str
        """
        return self._formatted_address

    @formatted_address.setter
    def formatted_address(self, formatted_address):
        """Sets the formatted_address of this LocationDataPointGpsLocation.

        Formatted address of the location  # noqa: E501

        :param formatted_address: The formatted_address of this LocationDataPointGpsLocation.  # noqa: E501
        :type: str
        """

        self._formatted_address = formatted_address

    @property
    def gps_meters_per_second(self):
        """Gets the gps_meters_per_second of this LocationDataPointGpsLocation.  # noqa: E501

        Speed of GPS (meters per second)  # noqa: E501

        :return: The gps_meters_per_second of this LocationDataPointGpsLocation.  # noqa: E501
        :rtype: float
        """
        return self._gps_meters_per_second

    @gps_meters_per_second.setter
    def gps_meters_per_second(self, gps_meters_per_second):
        """Sets the gps_meters_per_second of this LocationDataPointGpsLocation.

        Speed of GPS (meters per second)  # noqa: E501

        :param gps_meters_per_second: The gps_meters_per_second of this LocationDataPointGpsLocation.  # noqa: E501
        :type: float
        """

        self._gps_meters_per_second = gps_meters_per_second

    @property
    def heading_degrees(self):
        """Gets the heading_degrees of this LocationDataPointGpsLocation.  # noqa: E501

        Heading degrees  # noqa: E501

        :return: The heading_degrees of this LocationDataPointGpsLocation.  # noqa: E501
        :rtype: float
        """
        return self._heading_degrees

    @heading_degrees.setter
    def heading_degrees(self, heading_degrees):
        """Sets the heading_degrees of this LocationDataPointGpsLocation.

        Heading degrees  # noqa: E501

        :param heading_degrees: The heading_degrees of this LocationDataPointGpsLocation.  # noqa: E501
        :type: float
        """

        self._heading_degrees = heading_degrees

    @property
    def latitude(self):
        """Gets the latitude of this LocationDataPointGpsLocation.  # noqa: E501

        Latitude of the location  # noqa: E501

        :return: The latitude of this LocationDataPointGpsLocation.  # noqa: E501
        :rtype: float
        """
        return self._latitude

    @latitude.setter
    def latitude(self, latitude):
        """Sets the latitude of this LocationDataPointGpsLocation.

        Latitude of the location  # noqa: E501

        :param latitude: The latitude of this LocationDataPointGpsLocation.  # noqa: E501
        :type: float
        """

        self._latitude = latitude

    @property
    def longitude(self):
        """Gets the longitude of this LocationDataPointGpsLocation.  # noqa: E501

        Longitude of the location  # noqa: E501

        :return: The longitude of this LocationDataPointGpsLocation.  # noqa: E501
        :rtype: float
        """
        return self._longitude

    @longitude.setter
    def longitude(self, longitude):
        """Sets the longitude of this LocationDataPointGpsLocation.

        Longitude of the location  # noqa: E501

        :param longitude: The longitude of this LocationDataPointGpsLocation.  # noqa: E501
        :type: float
        """

        self._longitude = longitude

    @property
    def place(self):
        """Gets the place of this LocationDataPointGpsLocation.  # noqa: E501


        :return: The place of this LocationDataPointGpsLocation.  # noqa: E501
        :rtype: LocationDataPointGpsLocationPlace
        """
        return self._place

    @place.setter
    def place(self, place):
        """Sets the place of this LocationDataPointGpsLocation.


        :param place: The place of this LocationDataPointGpsLocation.  # noqa: E501
        :type: LocationDataPointGpsLocationPlace
        """

        self._place = place

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
        if not isinstance(other, LocationDataPointGpsLocation):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LocationDataPointGpsLocation):
            return True

        return self.to_dict() != other.to_dict()