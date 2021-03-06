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


class CsmConfig(object):
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
        'csm_appliance_status': 'str',
        'single_region': 'bool'
    }

    attribute_map = {
        '_self': '_self',
        'links': '_links',
        'schema': '_schema',
        'csm_appliance_status': 'csm_appliance_status',
        'single_region': 'single_region'
    }

    def __init__(self, _self=None, links=None, schema=None, csm_appliance_status=None, single_region=None):  # noqa: E501
        """CsmConfig - a model defined in Swagger"""  # noqa: E501

        self.__self = None
        self._links = None
        self._schema = None
        self._csm_appliance_status = None
        self._single_region = None
        self.discriminator = None

        if _self is not None:
            self._self = _self
        if links is not None:
            self.links = links
        if schema is not None:
            self.schema = schema
        if csm_appliance_status is not None:
            self.csm_appliance_status = csm_appliance_status
        if single_region is not None:
            self.single_region = single_region

    @property
    def _self(self):
        """Gets the _self of this CsmConfig.  # noqa: E501


        :return: The _self of this CsmConfig.  # noqa: E501
        :rtype: SelfResourceLink
        """
        return self.__self

    @_self.setter
    def _self(self, _self):
        """Sets the _self of this CsmConfig.


        :param _self: The _self of this CsmConfig.  # noqa: E501
        :type: SelfResourceLink
        """

        self.__self = _self

    @property
    def links(self):
        """Gets the links of this CsmConfig.  # noqa: E501

        The server will populate this field when returing the resource. Ignored on PUT and POST.  # noqa: E501

        :return: The links of this CsmConfig.  # noqa: E501
        :rtype: list[ResourceLink]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this CsmConfig.

        The server will populate this field when returing the resource. Ignored on PUT and POST.  # noqa: E501

        :param links: The links of this CsmConfig.  # noqa: E501
        :type: list[ResourceLink]
        """

        self._links = links

    @property
    def schema(self):
        """Gets the schema of this CsmConfig.  # noqa: E501


        :return: The schema of this CsmConfig.  # noqa: E501
        :rtype: str
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        """Sets the schema of this CsmConfig.


        :param schema: The schema of this CsmConfig.  # noqa: E501
        :type: str
        """

        self._schema = schema

    @property
    def csm_appliance_status(self):
        """Gets the csm_appliance_status of this CsmConfig.  # noqa: E501

        Csm appliance status  # noqa: E501

        :return: The csm_appliance_status of this CsmConfig.  # noqa: E501
        :rtype: str
        """
        return self._csm_appliance_status

    @csm_appliance_status.setter
    def csm_appliance_status(self, csm_appliance_status):
        """Sets the csm_appliance_status of this CsmConfig.

        Csm appliance status  # noqa: E501

        :param csm_appliance_status: The csm_appliance_status of this CsmConfig.  # noqa: E501
        :type: str
        """
        allowed_values = ["UNINITIALIZED", "INITIALIZED"]  # noqa: E501
        if csm_appliance_status not in allowed_values:
            raise ValueError(
                "Invalid value for `csm_appliance_status` ({0}), must be one of {1}"  # noqa: E501
                .format(csm_appliance_status, allowed_values)
            )

        self._csm_appliance_status = csm_appliance_status

    @property
    def single_region(self):
        """Gets the single_region of this CsmConfig.  # noqa: E501

        This property is used only if CSM is running in service mode  # noqa: E501

        :return: The single_region of this CsmConfig.  # noqa: E501
        :rtype: bool
        """
        return self._single_region

    @single_region.setter
    def single_region(self, single_region):
        """Sets the single_region of this CsmConfig.

        This property is used only if CSM is running in service mode  # noqa: E501

        :param single_region: The single_region of this CsmConfig.  # noqa: E501
        :type: bool
        """

        self._single_region = single_region

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
        if not isinstance(other, CsmConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
