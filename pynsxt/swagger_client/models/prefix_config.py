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


class PrefixConfig(object):
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
        'action': 'str',
        'ge': 'int',
        'le': 'int',
        'network': 'str'
    }

    attribute_map = {
        'action': 'action',
        'ge': 'ge',
        'le': 'le',
        'network': 'network'
    }

    def __init__(self, action=None, ge=None, le=None, network=None):  # noqa: E501
        """PrefixConfig - a model defined in Swagger"""  # noqa: E501

        self._action = None
        self._ge = None
        self._le = None
        self._network = None
        self.discriminator = None

        self.action = action
        if ge is not None:
            self.ge = ge
        if le is not None:
            self.le = le
        if network is not None:
            self.network = network

    @property
    def action(self):
        """Gets the action of this PrefixConfig.  # noqa: E501

        Action for the IPPrefix  # noqa: E501

        :return: The action of this PrefixConfig.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this PrefixConfig.

        Action for the IPPrefix  # noqa: E501

        :param action: The action of this PrefixConfig.  # noqa: E501
        :type: str
        """
        if action is None:
            raise ValueError("Invalid value for `action`, must not be `None`")  # noqa: E501
        allowed_values = ["PERMIT", "DENY"]  # noqa: E501
        if action not in allowed_values:
            raise ValueError(
                "Invalid value for `action` ({0}), must be one of {1}"  # noqa: E501
                .format(action, allowed_values)
            )

        self._action = action

    @property
    def ge(self):
        """Gets the ge of this PrefixConfig.  # noqa: E501

        Greater than or equal to  # noqa: E501

        :return: The ge of this PrefixConfig.  # noqa: E501
        :rtype: int
        """
        return self._ge

    @ge.setter
    def ge(self, ge):
        """Sets the ge of this PrefixConfig.

        Greater than or equal to  # noqa: E501

        :param ge: The ge of this PrefixConfig.  # noqa: E501
        :type: int
        """
        if ge is not None and ge > 32:  # noqa: E501
            raise ValueError("Invalid value for `ge`, must be a value less than or equal to `32`")  # noqa: E501
        if ge is not None and ge < 1:  # noqa: E501
            raise ValueError("Invalid value for `ge`, must be a value greater than or equal to `1`")  # noqa: E501

        self._ge = ge

    @property
    def le(self):
        """Gets the le of this PrefixConfig.  # noqa: E501

        Less than or equal to  # noqa: E501

        :return: The le of this PrefixConfig.  # noqa: E501
        :rtype: int
        """
        return self._le

    @le.setter
    def le(self, le):
        """Sets the le of this PrefixConfig.

        Less than or equal to  # noqa: E501

        :param le: The le of this PrefixConfig.  # noqa: E501
        :type: int
        """
        if le is not None and le > 32:  # noqa: E501
            raise ValueError("Invalid value for `le`, must be a value less than or equal to `32`")  # noqa: E501
        if le is not None and le < 1:  # noqa: E501
            raise ValueError("Invalid value for `le`, must be a value greater than or equal to `1`")  # noqa: E501

        self._le = le

    @property
    def network(self):
        """Gets the network of this PrefixConfig.  # noqa: E501

        If absent, the action applies to all addresses.  # noqa: E501

        :return: The network of this PrefixConfig.  # noqa: E501
        :rtype: str
        """
        return self._network

    @network.setter
    def network(self, network):
        """Sets the network of this PrefixConfig.

        If absent, the action applies to all addresses.  # noqa: E501

        :param network: The network of this PrefixConfig.  # noqa: E501
        :type: str
        """

        self._network = network

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
        if not isinstance(other, PrefixConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other