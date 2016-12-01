# coding: utf-8

"""
    Samsara API

    # Introduction The Samsara REST API lets you interact with the Samsara Cloud from anything that can send an HTTP request. With the Samsara API you can build powerful applications and custom solutions with sensor data.  Samsara has endpoints available to track and analyze sensors, vehicles, and entire fleets. If you’re familiar with what you can build with a REST API, the following API reference guide will be your go-to resource.  API access to the Samsara cloud is available to all Samsara administrators. If you’d like to try the API, [contact us](https://www.samsara.com/free-trial). The API is currently in beta and may be subject to frequent changes.  # Connecting to the API There are two ways to connect to the API. If you prefer to use the API in Javascript or Python, we supply SDKs which you can download here: [Javascript SDK](https://github.com/samsarahq/samsara-js), [Python SDK](https://github.com/samsarahq/samsara-python).  If you’d rather use another language to interact with the Samsara API, the endpoints and examples are in the reference guide below.  

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from pprint import pformat
from six import iteritems
import re


class VehicleLocation(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, name=None, latitude=None, longitude=None, location=None, time=None):
        """
        VehicleLocation - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'name': 'str',
            'latitude': 'float',
            'longitude': 'float',
            'location': 'str',
            'time': 'int'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'latitude': 'latitude',
            'longitude': 'longitude',
            'location': 'location',
            'time': 'time'
        }

        self._id = id
        self._name = name
        self._latitude = latitude
        self._longitude = longitude
        self._location = location
        self._time = time

    @property
    def id(self):
        """
        Gets the id of this VehicleLocation.
        ID of the vehicle.

        :return: The id of this VehicleLocation.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this VehicleLocation.
        ID of the vehicle.

        :param id: The id of this VehicleLocation.
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this VehicleLocation.
        Name of the vehicle.

        :return: The name of this VehicleLocation.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this VehicleLocation.
        Name of the vehicle.

        :param name: The name of this VehicleLocation.
        :type: str
        """

        self._name = name

    @property
    def latitude(self):
        """
        Gets the latitude of this VehicleLocation.
        Latitude in decimal degrees.

        :return: The latitude of this VehicleLocation.
        :rtype: float
        """
        return self._latitude

    @latitude.setter
    def latitude(self, latitude):
        """
        Sets the latitude of this VehicleLocation.
        Latitude in decimal degrees.

        :param latitude: The latitude of this VehicleLocation.
        :type: float
        """

        self._latitude = latitude

    @property
    def longitude(self):
        """
        Gets the longitude of this VehicleLocation.
        Longitude in decimal degrees.

        :return: The longitude of this VehicleLocation.
        :rtype: float
        """
        return self._longitude

    @longitude.setter
    def longitude(self, longitude):
        """
        Sets the longitude of this VehicleLocation.
        Longitude in decimal degrees.

        :param longitude: The longitude of this VehicleLocation.
        :type: float
        """

        self._longitude = longitude

    @property
    def location(self):
        """
        Gets the location of this VehicleLocation.
        Text representation of nearest identifiable location to (latitude, longitude) coordinates.

        :return: The location of this VehicleLocation.
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """
        Sets the location of this VehicleLocation.
        Text representation of nearest identifiable location to (latitude, longitude) coordinates.

        :param location: The location of this VehicleLocation.
        :type: str
        """

        self._location = location

    @property
    def time(self):
        """
        Gets the time of this VehicleLocation.
        The time the reported location was logged, reported as a UNIX timestamp in milliseconds.

        :return: The time of this VehicleLocation.
        :rtype: int
        """
        return self._time

    @time.setter
    def time(self, time):
        """
        Sets the time of this VehicleLocation.
        The time the reported location was logged, reported as a UNIX timestamp in milliseconds.

        :param time: The time of this VehicleLocation.
        :type: int
        """

        self._time = time

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
