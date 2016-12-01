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


class HistoryParam(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, group_id=None, start_ms=None, end_ms=None, step_ms=None, series=None, fill_missing='withNull'):
        """
        HistoryParam - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'group_id': 'int',
            'start_ms': 'int',
            'end_ms': 'int',
            'step_ms': 'int',
            'series': 'list[SensorshistorySeries]',
            'fill_missing': 'str'
        }

        self.attribute_map = {
            'group_id': 'groupId',
            'start_ms': 'startMs',
            'end_ms': 'endMs',
            'step_ms': 'stepMs',
            'series': 'series',
            'fill_missing': 'fillMissing'
        }

        self._group_id = group_id
        self._start_ms = start_ms
        self._end_ms = end_ms
        self._step_ms = step_ms
        self._series = series
        self._fill_missing = fill_missing

    @property
    def group_id(self):
        """
        Gets the group_id of this HistoryParam.
        Group ID to query.

        :return: The group_id of this HistoryParam.
        :rtype: int
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """
        Sets the group_id of this HistoryParam.
        Group ID to query.

        :param group_id: The group_id of this HistoryParam.
        :type: int
        """

        self._group_id = group_id

    @property
    def start_ms(self):
        """
        Gets the start_ms of this HistoryParam.
        Beginning of the time range, specified in milliseconds UNIX time.

        :return: The start_ms of this HistoryParam.
        :rtype: int
        """
        return self._start_ms

    @start_ms.setter
    def start_ms(self, start_ms):
        """
        Sets the start_ms of this HistoryParam.
        Beginning of the time range, specified in milliseconds UNIX time.

        :param start_ms: The start_ms of this HistoryParam.
        :type: int
        """

        self._start_ms = start_ms

    @property
    def end_ms(self):
        """
        Gets the end_ms of this HistoryParam.
        End of the time range, specified in milliseconds UNIX time.

        :return: The end_ms of this HistoryParam.
        :rtype: int
        """
        return self._end_ms

    @end_ms.setter
    def end_ms(self, end_ms):
        """
        Sets the end_ms of this HistoryParam.
        End of the time range, specified in milliseconds UNIX time.

        :param end_ms: The end_ms of this HistoryParam.
        :type: int
        """

        self._end_ms = end_ms

    @property
    def step_ms(self):
        """
        Gets the step_ms of this HistoryParam.
        Time resolution for which data should be returned, in milliseconds. Specifying 3600000 will return data at hour intervals.

        :return: The step_ms of this HistoryParam.
        :rtype: int
        """
        return self._step_ms

    @step_ms.setter
    def step_ms(self, step_ms):
        """
        Sets the step_ms of this HistoryParam.
        Time resolution for which data should be returned, in milliseconds. Specifying 3600000 will return data at hour intervals.

        :param step_ms: The step_ms of this HistoryParam.
        :type: int
        """

        self._step_ms = step_ms

    @property
    def series(self):
        """
        Gets the series of this HistoryParam.


        :return: The series of this HistoryParam.
        :rtype: list[SensorshistorySeries]
        """
        return self._series

    @series.setter
    def series(self, series):
        """
        Sets the series of this HistoryParam.


        :param series: The series of this HistoryParam.
        :type: list[SensorshistorySeries]
        """

        self._series = series

    @property
    def fill_missing(self):
        """
        Gets the fill_missing of this HistoryParam.


        :return: The fill_missing of this HistoryParam.
        :rtype: str
        """
        return self._fill_missing

    @fill_missing.setter
    def fill_missing(self, fill_missing):
        """
        Sets the fill_missing of this HistoryParam.


        :param fill_missing: The fill_missing of this HistoryParam.
        :type: str
        """
        allowed_values = ["withNull", "withPrevious"]
        if fill_missing not in allowed_values:
            raise ValueError(
                "Invalid value for `fill_missing` ({0}), must be one of {1}"
                .format(fill_missing, allowed_values)
            )

        self._fill_missing = fill_missing

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
