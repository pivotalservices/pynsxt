# coding: utf-8

"""
    NSX API

    VMware NSX REST API  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.models.resource import Resource  # noqa: F401,E501
from swagger_client.models.resource_link import ResourceLink  # noqa: F401,E501
from swagger_client.models.self_resource_link import SelfResourceLink  # noqa: F401,E501


class CapacityUsage(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        '_self': 'SelfResourceLink',
        'links': 'list[ResourceLink]',
        'schema': 'str',
        'usage_count': 'int',
        'capacity_type': 'str'
    }

    attribute_map = {
        '_self': '_self',
        'links': '_links',
        'schema': '_schema',
        'usage_count': 'usage_count',
        'capacity_type': 'capacity_type'
    }

    def __init__(self, _self=None, links=None, schema=None, usage_count=None, capacity_type=None):  # noqa: E501
        """CapacityUsage - a model defined in Swagger"""  # noqa: E501

        self.__self = None
        self._links = None
        self._schema = None
        self._usage_count = None
        self._capacity_type = None
        self.discriminator = None

        if _self is not None:
            self._self = _self
        if links is not None:
            self.links = links
        if schema is not None:
            self.schema = schema
        if usage_count is not None:
            self.usage_count = usage_count
        if capacity_type is not None:
            self.capacity_type = capacity_type

    @property
    def _self(self):
        """Gets the _self of this CapacityUsage.  # noqa: E501


        :return: The _self of this CapacityUsage.  # noqa: E501
        :rtype: SelfResourceLink
        """
        return self.__self

    @_self.setter
    def _self(self, _self):
        """Sets the _self of this CapacityUsage.


        :param _self: The _self of this CapacityUsage.  # noqa: E501
        :type: SelfResourceLink
        """

        self.__self = _self

    @property
    def links(self):
        """Gets the links of this CapacityUsage.  # noqa: E501

        The server will populate this field when returing the resource. Ignored on PUT and POST.  # noqa: E501

        :return: The links of this CapacityUsage.  # noqa: E501
        :rtype: list[ResourceLink]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this CapacityUsage.

        The server will populate this field when returing the resource. Ignored on PUT and POST.  # noqa: E501

        :param links: The links of this CapacityUsage.  # noqa: E501
        :type: list[ResourceLink]
        """

        self._links = links

    @property
    def schema(self):
        """Gets the schema of this CapacityUsage.  # noqa: E501


        :return: The schema of this CapacityUsage.  # noqa: E501
        :rtype: str
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        """Sets the schema of this CapacityUsage.


        :param schema: The schema of this CapacityUsage.  # noqa: E501
        :type: str
        """

        self._schema = schema

    @property
    def usage_count(self):
        """Gets the usage_count of this CapacityUsage.  # noqa: E501

        count of number of items of capacity_type  # noqa: E501

        :return: The usage_count of this CapacityUsage.  # noqa: E501
        :rtype: int
        """
        return self._usage_count

    @usage_count.setter
    def usage_count(self, usage_count):
        """Sets the usage_count of this CapacityUsage.

        count of number of items of capacity_type  # noqa: E501

        :param usage_count: The usage_count of this CapacityUsage.  # noqa: E501
        :type: int
        """

        self._usage_count = usage_count

    @property
    def capacity_type(self):
        """Gets the capacity_type of this CapacityUsage.  # noqa: E501

        type of the capacity field  # noqa: E501

        :return: The capacity_type of this CapacityUsage.  # noqa: E501
        :rtype: str
        """
        return self._capacity_type

    @capacity_type.setter
    def capacity_type(self, capacity_type):
        """Sets the capacity_type of this CapacityUsage.

        type of the capacity field  # noqa: E501

        :param capacity_type: The capacity_type of this CapacityUsage.  # noqa: E501
        :type: str
        """

        self._capacity_type = capacity_type

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if not isinstance(other, CapacityUsage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other