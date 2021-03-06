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


class NodeLogProperties(object):
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
        'last_modified_time': 'int',
        'log_size': 'int',
        'log_name': 'str'
    }

    attribute_map = {
        '_self': '_self',
        'links': '_links',
        'schema': '_schema',
        'last_modified_time': 'last_modified_time',
        'log_size': 'log_size',
        'log_name': 'log_name'
    }

    def __init__(self, _self=None, links=None, schema=None, last_modified_time=None, log_size=None, log_name=None):  # noqa: E501
        """NodeLogProperties - a model defined in Swagger"""  # noqa: E501

        self.__self = None
        self._links = None
        self._schema = None
        self._last_modified_time = None
        self._log_size = None
        self._log_name = None
        self.discriminator = None

        if _self is not None:
            self._self = _self
        if links is not None:
            self.links = links
        if schema is not None:
            self.schema = schema
        if last_modified_time is not None:
            self.last_modified_time = last_modified_time
        if log_size is not None:
            self.log_size = log_size
        if log_name is not None:
            self.log_name = log_name

    @property
    def _self(self):
        """Gets the _self of this NodeLogProperties.  # noqa: E501


        :return: The _self of this NodeLogProperties.  # noqa: E501
        :rtype: SelfResourceLink
        """
        return self.__self

    @_self.setter
    def _self(self, _self):
        """Sets the _self of this NodeLogProperties.


        :param _self: The _self of this NodeLogProperties.  # noqa: E501
        :type: SelfResourceLink
        """

        self.__self = _self

    @property
    def links(self):
        """Gets the links of this NodeLogProperties.  # noqa: E501

        The server will populate this field when returing the resource. Ignored on PUT and POST.  # noqa: E501

        :return: The links of this NodeLogProperties.  # noqa: E501
        :rtype: list[ResourceLink]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this NodeLogProperties.

        The server will populate this field when returing the resource. Ignored on PUT and POST.  # noqa: E501

        :param links: The links of this NodeLogProperties.  # noqa: E501
        :type: list[ResourceLink]
        """

        self._links = links

    @property
    def schema(self):
        """Gets the schema of this NodeLogProperties.  # noqa: E501


        :return: The schema of this NodeLogProperties.  # noqa: E501
        :rtype: str
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        """Sets the schema of this NodeLogProperties.


        :param schema: The schema of this NodeLogProperties.  # noqa: E501
        :type: str
        """

        self._schema = schema

    @property
    def last_modified_time(self):
        """Gets the last_modified_time of this NodeLogProperties.  # noqa: E501

        Last modified time expressed in milliseconds since epoch  # noqa: E501

        :return: The last_modified_time of this NodeLogProperties.  # noqa: E501
        :rtype: int
        """
        return self._last_modified_time

    @last_modified_time.setter
    def last_modified_time(self, last_modified_time):
        """Sets the last_modified_time of this NodeLogProperties.

        Last modified time expressed in milliseconds since epoch  # noqa: E501

        :param last_modified_time: The last_modified_time of this NodeLogProperties.  # noqa: E501
        :type: int
        """

        self._last_modified_time = last_modified_time

    @property
    def log_size(self):
        """Gets the log_size of this NodeLogProperties.  # noqa: E501

        Size of log file in bytes  # noqa: E501

        :return: The log_size of this NodeLogProperties.  # noqa: E501
        :rtype: int
        """
        return self._log_size

    @log_size.setter
    def log_size(self, log_size):
        """Sets the log_size of this NodeLogProperties.

        Size of log file in bytes  # noqa: E501

        :param log_size: The log_size of this NodeLogProperties.  # noqa: E501
        :type: int
        """

        self._log_size = log_size

    @property
    def log_name(self):
        """Gets the log_name of this NodeLogProperties.  # noqa: E501

        Name of log file  # noqa: E501

        :return: The log_name of this NodeLogProperties.  # noqa: E501
        :rtype: str
        """
        return self._log_name

    @log_name.setter
    def log_name(self, log_name):
        """Sets the log_name of this NodeLogProperties.

        Name of log file  # noqa: E501

        :param log_name: The log_name of this NodeLogProperties.  # noqa: E501
        :type: str
        """

        self._log_name = log_name

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
        if not isinstance(other, NodeLogProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
