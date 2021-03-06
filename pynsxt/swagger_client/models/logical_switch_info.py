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


class LogicalSwitchInfo(object):
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
        'logical_switch_id': 'str',
        'instances_count': 'int',
        'logical_switch_display_name': 'str',
        'is_default_logical_switch': 'bool',
        'nsx_switch_tag': 'str'
    }

    attribute_map = {
        'logical_switch_id': 'logical_switch_id',
        'instances_count': 'instances_count',
        'logical_switch_display_name': 'logical_switch_display_name',
        'is_default_logical_switch': 'is_default_logical_switch',
        'nsx_switch_tag': 'nsx_switch_tag'
    }

    def __init__(self, logical_switch_id=None, instances_count=None, logical_switch_display_name=None, is_default_logical_switch=None, nsx_switch_tag=None):  # noqa: E501
        """LogicalSwitchInfo - a model defined in Swagger"""  # noqa: E501

        self._logical_switch_id = None
        self._instances_count = None
        self._logical_switch_display_name = None
        self._is_default_logical_switch = None
        self._nsx_switch_tag = None
        self.discriminator = None

        if logical_switch_id is not None:
            self.logical_switch_id = logical_switch_id
        if instances_count is not None:
            self.instances_count = instances_count
        if logical_switch_display_name is not None:
            self.logical_switch_display_name = logical_switch_display_name
        if is_default_logical_switch is not None:
            self.is_default_logical_switch = is_default_logical_switch
        if nsx_switch_tag is not None:
            self.nsx_switch_tag = nsx_switch_tag

    @property
    def logical_switch_id(self):
        """Gets the logical_switch_id of this LogicalSwitchInfo.  # noqa: E501

        ID of the logical switch  # noqa: E501

        :return: The logical_switch_id of this LogicalSwitchInfo.  # noqa: E501
        :rtype: str
        """
        return self._logical_switch_id

    @logical_switch_id.setter
    def logical_switch_id(self, logical_switch_id):
        """Sets the logical_switch_id of this LogicalSwitchInfo.

        ID of the logical switch  # noqa: E501

        :param logical_switch_id: The logical_switch_id of this LogicalSwitchInfo.  # noqa: E501
        :type: str
        """

        self._logical_switch_id = logical_switch_id

    @property
    def instances_count(self):
        """Gets the instances_count of this LogicalSwitchInfo.  # noqa: E501

        Number of instances on this logical switch  # noqa: E501

        :return: The instances_count of this LogicalSwitchInfo.  # noqa: E501
        :rtype: int
        """
        return self._instances_count

    @instances_count.setter
    def instances_count(self, instances_count):
        """Sets the instances_count of this LogicalSwitchInfo.

        Number of instances on this logical switch  # noqa: E501

        :param instances_count: The instances_count of this LogicalSwitchInfo.  # noqa: E501
        :type: int
        """

        self._instances_count = instances_count

    @property
    def logical_switch_display_name(self):
        """Gets the logical_switch_display_name of this LogicalSwitchInfo.  # noqa: E501

        Name of the logical switch  # noqa: E501

        :return: The logical_switch_display_name of this LogicalSwitchInfo.  # noqa: E501
        :rtype: str
        """
        return self._logical_switch_display_name

    @logical_switch_display_name.setter
    def logical_switch_display_name(self, logical_switch_display_name):
        """Sets the logical_switch_display_name of this LogicalSwitchInfo.

        Name of the logical switch  # noqa: E501

        :param logical_switch_display_name: The logical_switch_display_name of this LogicalSwitchInfo.  # noqa: E501
        :type: str
        """

        self._logical_switch_display_name = logical_switch_display_name

    @property
    def is_default_logical_switch(self):
        """Gets the is_default_logical_switch of this LogicalSwitchInfo.  # noqa: E501

        Flag to identify if this is the default logical switch  # noqa: E501

        :return: The is_default_logical_switch of this LogicalSwitchInfo.  # noqa: E501
        :rtype: bool
        """
        return self._is_default_logical_switch

    @is_default_logical_switch.setter
    def is_default_logical_switch(self, is_default_logical_switch):
        """Sets the is_default_logical_switch of this LogicalSwitchInfo.

        Flag to identify if this is the default logical switch  # noqa: E501

        :param is_default_logical_switch: The is_default_logical_switch of this LogicalSwitchInfo.  # noqa: E501
        :type: bool
        """

        self._is_default_logical_switch = is_default_logical_switch

    @property
    def nsx_switch_tag(self):
        """Gets the nsx_switch_tag of this LogicalSwitchInfo.  # noqa: E501

        This tag is applied on cloud compute resource to be attached to this logical switch   # noqa: E501

        :return: The nsx_switch_tag of this LogicalSwitchInfo.  # noqa: E501
        :rtype: str
        """
        return self._nsx_switch_tag

    @nsx_switch_tag.setter
    def nsx_switch_tag(self, nsx_switch_tag):
        """Sets the nsx_switch_tag of this LogicalSwitchInfo.

        This tag is applied on cloud compute resource to be attached to this logical switch   # noqa: E501

        :param nsx_switch_tag: The nsx_switch_tag of this LogicalSwitchInfo.  # noqa: E501
        :type: str
        """

        self._nsx_switch_tag = nsx_switch_tag

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
        if not isinstance(other, LogicalSwitchInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
