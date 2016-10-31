# coding: utf-8

"""
    Samsara API


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


class FleetdispatchJobsupdateDispatchJobs(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, external_identifier=None, driver_id=None, vehicle_id=None, job_state=None, scheduled_arrival_time_ms=None, started_at_ms=None, completed_at_ms=None, cancelled_at_ms=None, notes=None, destination_name=None, destination_address=None, destination_lat=None, destination_lng=None):
        """
        FleetdispatchJobsupdateDispatchJobs - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'external_identifier': 'str',
            'driver_id': 'int',
            'vehicle_id': 'int',
            'job_state': 'str',
            'scheduled_arrival_time_ms': 'int',
            'started_at_ms': 'int',
            'completed_at_ms': 'int',
            'cancelled_at_ms': 'int',
            'notes': 'str',
            'destination_name': 'str',
            'destination_address': 'str',
            'destination_lat': 'float',
            'destination_lng': 'float'
        }

        self.attribute_map = {
            'id': 'id',
            'external_identifier': 'external_identifier',
            'driver_id': 'driver_id',
            'vehicle_id': 'vehicle_id',
            'job_state': 'job_state',
            'scheduled_arrival_time_ms': 'scheduled_arrival_time_ms',
            'started_at_ms': 'started_at_ms',
            'completed_at_ms': 'completed_at_ms',
            'cancelled_at_ms': 'cancelled_at_ms',
            'notes': 'notes',
            'destination_name': 'destination_name',
            'destination_address': 'destination_address',
            'destination_lat': 'destination_lat',
            'destination_lng': 'destination_lng'
        }

        self._id = id
        self._external_identifier = external_identifier
        self._driver_id = driver_id
        self._vehicle_id = vehicle_id
        self._job_state = job_state
        self._scheduled_arrival_time_ms = scheduled_arrival_time_ms
        self._started_at_ms = started_at_ms
        self._completed_at_ms = completed_at_ms
        self._cancelled_at_ms = cancelled_at_ms
        self._notes = notes
        self._destination_name = destination_name
        self._destination_address = destination_address
        self._destination_lat = destination_lat
        self._destination_lng = destination_lng

    @property
    def id(self):
        """
        Gets the id of this FleetdispatchJobsupdateDispatchJobs.


        :return: The id of this FleetdispatchJobsupdateDispatchJobs.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this FleetdispatchJobsupdateDispatchJobs.


        :param id: The id of this FleetdispatchJobsupdateDispatchJobs.
        :type: int
        """

        self._id = id

    @property
    def external_identifier(self):
        """
        Gets the external_identifier of this FleetdispatchJobsupdateDispatchJobs.


        :return: The external_identifier of this FleetdispatchJobsupdateDispatchJobs.
        :rtype: str
        """
        return self._external_identifier

    @external_identifier.setter
    def external_identifier(self, external_identifier):
        """
        Sets the external_identifier of this FleetdispatchJobsupdateDispatchJobs.


        :param external_identifier: The external_identifier of this FleetdispatchJobsupdateDispatchJobs.
        :type: str
        """

        self._external_identifier = external_identifier

    @property
    def driver_id(self):
        """
        Gets the driver_id of this FleetdispatchJobsupdateDispatchJobs.


        :return: The driver_id of this FleetdispatchJobsupdateDispatchJobs.
        :rtype: int
        """
        return self._driver_id

    @driver_id.setter
    def driver_id(self, driver_id):
        """
        Sets the driver_id of this FleetdispatchJobsupdateDispatchJobs.


        :param driver_id: The driver_id of this FleetdispatchJobsupdateDispatchJobs.
        :type: int
        """

        self._driver_id = driver_id

    @property
    def vehicle_id(self):
        """
        Gets the vehicle_id of this FleetdispatchJobsupdateDispatchJobs.


        :return: The vehicle_id of this FleetdispatchJobsupdateDispatchJobs.
        :rtype: int
        """
        return self._vehicle_id

    @vehicle_id.setter
    def vehicle_id(self, vehicle_id):
        """
        Sets the vehicle_id of this FleetdispatchJobsupdateDispatchJobs.


        :param vehicle_id: The vehicle_id of this FleetdispatchJobsupdateDispatchJobs.
        :type: int
        """

        self._vehicle_id = vehicle_id

    @property
    def job_state(self):
        """
        Gets the job_state of this FleetdispatchJobsupdateDispatchJobs.


        :return: The job_state of this FleetdispatchJobsupdateDispatchJobs.
        :rtype: str
        """
        return self._job_state

    @job_state.setter
    def job_state(self, job_state):
        """
        Sets the job_state of this FleetdispatchJobsupdateDispatchJobs.


        :param job_state: The job_state of this FleetdispatchJobsupdateDispatchJobs.
        :type: str
        """
        allowed_values = ["JobState_Unassigned", "JobState_Assigned", "JobState_Started", "JobState_Completed", "JobState_Cancelled"]
        if job_state not in allowed_values:
            raise ValueError(
                "Invalid value for `job_state` ({0}), must be one of {1}"
                .format(job_state, allowed_values)
            )

        self._job_state = job_state

    @property
    def scheduled_arrival_time_ms(self):
        """
        Gets the scheduled_arrival_time_ms of this FleetdispatchJobsupdateDispatchJobs.


        :return: The scheduled_arrival_time_ms of this FleetdispatchJobsupdateDispatchJobs.
        :rtype: int
        """
        return self._scheduled_arrival_time_ms

    @scheduled_arrival_time_ms.setter
    def scheduled_arrival_time_ms(self, scheduled_arrival_time_ms):
        """
        Sets the scheduled_arrival_time_ms of this FleetdispatchJobsupdateDispatchJobs.


        :param scheduled_arrival_time_ms: The scheduled_arrival_time_ms of this FleetdispatchJobsupdateDispatchJobs.
        :type: int
        """

        self._scheduled_arrival_time_ms = scheduled_arrival_time_ms

    @property
    def started_at_ms(self):
        """
        Gets the started_at_ms of this FleetdispatchJobsupdateDispatchJobs.


        :return: The started_at_ms of this FleetdispatchJobsupdateDispatchJobs.
        :rtype: int
        """
        return self._started_at_ms

    @started_at_ms.setter
    def started_at_ms(self, started_at_ms):
        """
        Sets the started_at_ms of this FleetdispatchJobsupdateDispatchJobs.


        :param started_at_ms: The started_at_ms of this FleetdispatchJobsupdateDispatchJobs.
        :type: int
        """

        self._started_at_ms = started_at_ms

    @property
    def completed_at_ms(self):
        """
        Gets the completed_at_ms of this FleetdispatchJobsupdateDispatchJobs.


        :return: The completed_at_ms of this FleetdispatchJobsupdateDispatchJobs.
        :rtype: int
        """
        return self._completed_at_ms

    @completed_at_ms.setter
    def completed_at_ms(self, completed_at_ms):
        """
        Sets the completed_at_ms of this FleetdispatchJobsupdateDispatchJobs.


        :param completed_at_ms: The completed_at_ms of this FleetdispatchJobsupdateDispatchJobs.
        :type: int
        """

        self._completed_at_ms = completed_at_ms

    @property
    def cancelled_at_ms(self):
        """
        Gets the cancelled_at_ms of this FleetdispatchJobsupdateDispatchJobs.


        :return: The cancelled_at_ms of this FleetdispatchJobsupdateDispatchJobs.
        :rtype: int
        """
        return self._cancelled_at_ms

    @cancelled_at_ms.setter
    def cancelled_at_ms(self, cancelled_at_ms):
        """
        Sets the cancelled_at_ms of this FleetdispatchJobsupdateDispatchJobs.


        :param cancelled_at_ms: The cancelled_at_ms of this FleetdispatchJobsupdateDispatchJobs.
        :type: int
        """

        self._cancelled_at_ms = cancelled_at_ms

    @property
    def notes(self):
        """
        Gets the notes of this FleetdispatchJobsupdateDispatchJobs.


        :return: The notes of this FleetdispatchJobsupdateDispatchJobs.
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """
        Sets the notes of this FleetdispatchJobsupdateDispatchJobs.


        :param notes: The notes of this FleetdispatchJobsupdateDispatchJobs.
        :type: str
        """

        self._notes = notes

    @property
    def destination_name(self):
        """
        Gets the destination_name of this FleetdispatchJobsupdateDispatchJobs.


        :return: The destination_name of this FleetdispatchJobsupdateDispatchJobs.
        :rtype: str
        """
        return self._destination_name

    @destination_name.setter
    def destination_name(self, destination_name):
        """
        Sets the destination_name of this FleetdispatchJobsupdateDispatchJobs.


        :param destination_name: The destination_name of this FleetdispatchJobsupdateDispatchJobs.
        :type: str
        """

        self._destination_name = destination_name

    @property
    def destination_address(self):
        """
        Gets the destination_address of this FleetdispatchJobsupdateDispatchJobs.


        :return: The destination_address of this FleetdispatchJobsupdateDispatchJobs.
        :rtype: str
        """
        return self._destination_address

    @destination_address.setter
    def destination_address(self, destination_address):
        """
        Sets the destination_address of this FleetdispatchJobsupdateDispatchJobs.


        :param destination_address: The destination_address of this FleetdispatchJobsupdateDispatchJobs.
        :type: str
        """

        self._destination_address = destination_address

    @property
    def destination_lat(self):
        """
        Gets the destination_lat of this FleetdispatchJobsupdateDispatchJobs.


        :return: The destination_lat of this FleetdispatchJobsupdateDispatchJobs.
        :rtype: float
        """
        return self._destination_lat

    @destination_lat.setter
    def destination_lat(self, destination_lat):
        """
        Sets the destination_lat of this FleetdispatchJobsupdateDispatchJobs.


        :param destination_lat: The destination_lat of this FleetdispatchJobsupdateDispatchJobs.
        :type: float
        """

        self._destination_lat = destination_lat

    @property
    def destination_lng(self):
        """
        Gets the destination_lng of this FleetdispatchJobsupdateDispatchJobs.


        :return: The destination_lng of this FleetdispatchJobsupdateDispatchJobs.
        :rtype: float
        """
        return self._destination_lng

    @destination_lng.setter
    def destination_lng(self, destination_lng):
        """
        Sets the destination_lng of this FleetdispatchJobsupdateDispatchJobs.


        :param destination_lng: The destination_lng of this FleetdispatchJobsupdateDispatchJobs.
        :type: float
        """

        self._destination_lng = destination_lng

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
