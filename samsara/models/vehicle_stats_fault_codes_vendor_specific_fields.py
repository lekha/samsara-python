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


class VehicleStatsFaultCodesVendorSpecificFields(object):
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
        'dtc_description': 'str',
        'repair_instructions_url': 'str'
    }

    attribute_map = {
        'dtc_description': 'dtcDescription',
        'repair_instructions_url': 'repairInstructionsUrl'
    }

    def __init__(self, dtc_description=None, repair_instructions_url=None, local_vars_configuration=None):  # noqa: E501
        """VehicleStatsFaultCodesVendorSpecificFields - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._dtc_description = None
        self._repair_instructions_url = None
        self.discriminator = None

        if dtc_description is not None:
            self.dtc_description = dtc_description
        if repair_instructions_url is not None:
            self.repair_instructions_url = repair_instructions_url

    @property
    def dtc_description(self):
        """Gets the dtc_description of this VehicleStatsFaultCodesVendorSpecificFields.  # noqa: E501

        The DTC description, if available.  # noqa: E501

        :return: The dtc_description of this VehicleStatsFaultCodesVendorSpecificFields.  # noqa: E501
        :rtype: str
        """
        return self._dtc_description

    @dtc_description.setter
    def dtc_description(self, dtc_description):
        """Sets the dtc_description of this VehicleStatsFaultCodesVendorSpecificFields.

        The DTC description, if available.  # noqa: E501

        :param dtc_description: The dtc_description of this VehicleStatsFaultCodesVendorSpecificFields.  # noqa: E501
        :type: str
        """

        self._dtc_description = dtc_description

    @property
    def repair_instructions_url(self):
        """Gets the repair_instructions_url of this VehicleStatsFaultCodesVendorSpecificFields.  # noqa: E501

        A link to vendor repair instructions, if available.  # noqa: E501

        :return: The repair_instructions_url of this VehicleStatsFaultCodesVendorSpecificFields.  # noqa: E501
        :rtype: str
        """
        return self._repair_instructions_url

    @repair_instructions_url.setter
    def repair_instructions_url(self, repair_instructions_url):
        """Sets the repair_instructions_url of this VehicleStatsFaultCodesVendorSpecificFields.

        A link to vendor repair instructions, if available.  # noqa: E501

        :param repair_instructions_url: The repair_instructions_url of this VehicleStatsFaultCodesVendorSpecificFields.  # noqa: E501
        :type: str
        """

        self._repair_instructions_url = repair_instructions_url

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
        if not isinstance(other, VehicleStatsFaultCodesVendorSpecificFields):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VehicleStatsFaultCodesVendorSpecificFields):
            return True

        return self.to_dict() != other.to_dict()