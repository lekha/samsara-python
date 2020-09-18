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


class UpdateAttributeRequest(object):
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
        'attribute_type': 'str',
        'attribute_value_quantity': 'str',
        'entities': 'list[CreateAttributeRequestEntities]',
        'entity_type': 'str',
        'name': 'str',
        'number_values': 'list[float]',
        'string_values': 'list[str]'
    }

    attribute_map = {
        'attribute_type': 'attributeType',
        'attribute_value_quantity': 'attributeValueQuantity',
        'entities': 'entities',
        'entity_type': 'entityType',
        'name': 'name',
        'number_values': 'numberValues',
        'string_values': 'stringValues'
    }

    def __init__(self, attribute_type='string', attribute_value_quantity='multi', entities=None, entity_type=None, name=None, number_values=None, string_values=None, local_vars_configuration=None):  # noqa: E501
        """UpdateAttributeRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._attribute_type = None
        self._attribute_value_quantity = None
        self._entities = None
        self._entity_type = None
        self._name = None
        self._number_values = None
        self._string_values = None
        self.discriminator = None

        if attribute_type is not None:
            self.attribute_type = attribute_type
        if attribute_value_quantity is not None:
            self.attribute_value_quantity = attribute_value_quantity
        if entities is not None:
            self.entities = entities
        self.entity_type = entity_type
        if name is not None:
            self.name = name
        if number_values is not None:
            self.number_values = number_values
        if string_values is not None:
            self.string_values = string_values

    @property
    def attribute_type(self):
        """Gets the attribute_type of this UpdateAttributeRequest.  # noqa: E501

        Denotes the data type of the attribute's values.  # noqa: E501

        :return: The attribute_type of this UpdateAttributeRequest.  # noqa: E501
        :rtype: str
        """
        return self._attribute_type

    @attribute_type.setter
    def attribute_type(self, attribute_type):
        """Sets the attribute_type of this UpdateAttributeRequest.

        Denotes the data type of the attribute's values.  # noqa: E501

        :param attribute_type: The attribute_type of this UpdateAttributeRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["string", "number"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and attribute_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `attribute_type` ({0}), must be one of {1}"  # noqa: E501
                .format(attribute_type, allowed_values)
            )

        self._attribute_type = attribute_type

    @property
    def attribute_value_quantity(self):
        """Gets the attribute_value_quantity of this UpdateAttributeRequest.  # noqa: E501

        Defines whether or not this attribute can be used on the same entity many times (with different values).  # noqa: E501

        :return: The attribute_value_quantity of this UpdateAttributeRequest.  # noqa: E501
        :rtype: str
        """
        return self._attribute_value_quantity

    @attribute_value_quantity.setter
    def attribute_value_quantity(self, attribute_value_quantity):
        """Sets the attribute_value_quantity of this UpdateAttributeRequest.

        Defines whether or not this attribute can be used on the same entity many times (with different values).  # noqa: E501

        :param attribute_value_quantity: The attribute_value_quantity of this UpdateAttributeRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["single", "multi"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and attribute_value_quantity not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `attribute_value_quantity` ({0}), must be one of {1}"  # noqa: E501
                .format(attribute_value_quantity, allowed_values)
            )

        self._attribute_value_quantity = attribute_value_quantity

    @property
    def entities(self):
        """Gets the entities of this UpdateAttributeRequest.  # noqa: E501

        Entities that will be applied to this attribute  # noqa: E501

        :return: The entities of this UpdateAttributeRequest.  # noqa: E501
        :rtype: list[CreateAttributeRequestEntities]
        """
        return self._entities

    @entities.setter
    def entities(self, entities):
        """Sets the entities of this UpdateAttributeRequest.

        Entities that will be applied to this attribute  # noqa: E501

        :param entities: The entities of this UpdateAttributeRequest.  # noqa: E501
        :type: list[CreateAttributeRequestEntities]
        """

        self._entities = entities

    @property
    def entity_type(self):
        """Gets the entity_type of this UpdateAttributeRequest.  # noqa: E501

        Denotes the type of entity, driver or vehicle.  # noqa: E501

        :return: The entity_type of this UpdateAttributeRequest.  # noqa: E501
        :rtype: str
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """Sets the entity_type of this UpdateAttributeRequest.

        Denotes the type of entity, driver or vehicle.  # noqa: E501

        :param entity_type: The entity_type of this UpdateAttributeRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and entity_type is None:  # noqa: E501
            raise ValueError("Invalid value for `entity_type`, must not be `None`")  # noqa: E501
        allowed_values = ["driver", "vehicle"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and entity_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `entity_type` ({0}), must be one of {1}"  # noqa: E501
                .format(entity_type, allowed_values)
            )

        self._entity_type = entity_type

    @property
    def name(self):
        """Gets the name of this UpdateAttributeRequest.  # noqa: E501

        Name  # noqa: E501

        :return: The name of this UpdateAttributeRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateAttributeRequest.

        Name  # noqa: E501

        :param name: The name of this UpdateAttributeRequest.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def number_values(self):
        """Gets the number_values of this UpdateAttributeRequest.  # noqa: E501

        Number values that can be associated with this attribute  # noqa: E501

        :return: The number_values of this UpdateAttributeRequest.  # noqa: E501
        :rtype: list[float]
        """
        return self._number_values

    @number_values.setter
    def number_values(self, number_values):
        """Sets the number_values of this UpdateAttributeRequest.

        Number values that can be associated with this attribute  # noqa: E501

        :param number_values: The number_values of this UpdateAttributeRequest.  # noqa: E501
        :type: list[float]
        """

        self._number_values = number_values

    @property
    def string_values(self):
        """Gets the string_values of this UpdateAttributeRequest.  # noqa: E501

        String values that can be associated with this attribute  # noqa: E501

        :return: The string_values of this UpdateAttributeRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._string_values

    @string_values.setter
    def string_values(self, string_values):
        """Sets the string_values of this UpdateAttributeRequest.

        String values that can be associated with this attribute  # noqa: E501

        :param string_values: The string_values of this UpdateAttributeRequest.  # noqa: E501
        :type: list[str]
        """

        self._string_values = string_values

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
        if not isinstance(other, UpdateAttributeRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdateAttributeRequest):
            return True

        return self.to_dict() != other.to_dict()
