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
from swagger_client.models.tag import Tag  # noqa: F401,E501


class DiscoveredResource(object):
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
        'last_sync_time': 'int',
        'display_name': 'str',
        'description': 'str',
        'resource_type': 'str',
        'tags': 'list[Tag]'
    }

    attribute_map = {
        '_self': '_self',
        'links': '_links',
        'schema': '_schema',
        'last_sync_time': '_last_sync_time',
        'display_name': 'display_name',
        'description': 'description',
        'resource_type': 'resource_type',
        'tags': 'tags'
    }

    def __init__(self, _self=None, links=None, schema=None, last_sync_time=None, display_name=None, description=None, resource_type=None, tags=None):  # noqa: E501
        """DiscoveredResource - a model defined in Swagger"""  # noqa: E501

        self.__self = None
        self._links = None
        self._schema = None
        self._last_sync_time = None
        self._display_name = None
        self._description = None
        self._resource_type = None
        self._tags = None
        self.discriminator = None

        if _self is not None:
            self._self = _self
        if links is not None:
            self.links = links
        if schema is not None:
            self.schema = schema
        if last_sync_time is not None:
            self.last_sync_time = last_sync_time
        if display_name is not None:
            self.display_name = display_name
        if description is not None:
            self.description = description
        if resource_type is not None:
            self.resource_type = resource_type
        if tags is not None:
            self.tags = tags

    @property
    def _self(self):
        """Gets the _self of this DiscoveredResource.  # noqa: E501


        :return: The _self of this DiscoveredResource.  # noqa: E501
        :rtype: SelfResourceLink
        """
        return self.__self

    @_self.setter
    def _self(self, _self):
        """Sets the _self of this DiscoveredResource.


        :param _self: The _self of this DiscoveredResource.  # noqa: E501
        :type: SelfResourceLink
        """

        self.__self = _self

    @property
    def links(self):
        """Gets the links of this DiscoveredResource.  # noqa: E501

        The server will populate this field when returing the resource. Ignored on PUT and POST.  # noqa: E501

        :return: The links of this DiscoveredResource.  # noqa: E501
        :rtype: list[ResourceLink]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this DiscoveredResource.

        The server will populate this field when returing the resource. Ignored on PUT and POST.  # noqa: E501

        :param links: The links of this DiscoveredResource.  # noqa: E501
        :type: list[ResourceLink]
        """

        self._links = links

    @property
    def schema(self):
        """Gets the schema of this DiscoveredResource.  # noqa: E501


        :return: The schema of this DiscoveredResource.  # noqa: E501
        :rtype: str
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        """Sets the schema of this DiscoveredResource.


        :param schema: The schema of this DiscoveredResource.  # noqa: E501
        :type: str
        """

        self._schema = schema

    @property
    def last_sync_time(self):
        """Gets the last_sync_time of this DiscoveredResource.  # noqa: E501

        Timestamp of last modification  # noqa: E501

        :return: The last_sync_time of this DiscoveredResource.  # noqa: E501
        :rtype: int
        """
        return self._last_sync_time

    @last_sync_time.setter
    def last_sync_time(self, last_sync_time):
        """Sets the last_sync_time of this DiscoveredResource.

        Timestamp of last modification  # noqa: E501

        :param last_sync_time: The last_sync_time of this DiscoveredResource.  # noqa: E501
        :type: int
        """

        self._last_sync_time = last_sync_time

    @property
    def display_name(self):
        """Gets the display_name of this DiscoveredResource.  # noqa: E501

        Defaults to ID if not set  # noqa: E501

        :return: The display_name of this DiscoveredResource.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this DiscoveredResource.

        Defaults to ID if not set  # noqa: E501

        :param display_name: The display_name of this DiscoveredResource.  # noqa: E501
        :type: str
        """
        if display_name is not None and len(display_name) > 255:
            raise ValueError("Invalid value for `display_name`, length must be less than or equal to `255`")  # noqa: E501

        self._display_name = display_name

    @property
    def description(self):
        """Gets the description of this DiscoveredResource.  # noqa: E501

        Description of this resource  # noqa: E501

        :return: The description of this DiscoveredResource.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DiscoveredResource.

        Description of this resource  # noqa: E501

        :param description: The description of this DiscoveredResource.  # noqa: E501
        :type: str
        """
        if description is not None and len(description) > 1024:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `1024`")  # noqa: E501

        self._description = description

    @property
    def resource_type(self):
        """Gets the resource_type of this DiscoveredResource.  # noqa: E501

        The type of this resource.  # noqa: E501

        :return: The resource_type of this DiscoveredResource.  # noqa: E501
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this DiscoveredResource.

        The type of this resource.  # noqa: E501

        :param resource_type: The resource_type of this DiscoveredResource.  # noqa: E501
        :type: str
        """

        self._resource_type = resource_type

    @property
    def tags(self):
        """Gets the tags of this DiscoveredResource.  # noqa: E501

        Opaque identifiers meaningful to the API user  # noqa: E501

        :return: The tags of this DiscoveredResource.  # noqa: E501
        :rtype: list[Tag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this DiscoveredResource.

        Opaque identifiers meaningful to the API user  # noqa: E501

        :param tags: The tags of this DiscoveredResource.  # noqa: E501
        :type: list[Tag]
        """

        self._tags = tags

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
        if not isinstance(other, DiscoveredResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
