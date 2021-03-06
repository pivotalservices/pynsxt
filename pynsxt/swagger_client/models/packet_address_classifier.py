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


class PacketAddressClassifier(object):
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
        'vlan': 'int',
        'ip_address': 'str',
        'mac_address': 'str'
    }

    attribute_map = {
        'vlan': 'vlan',
        'ip_address': 'ip_address',
        'mac_address': 'mac_address'
    }

    def __init__(self, vlan=None, ip_address=None, mac_address=None):  # noqa: E501
        """PacketAddressClassifier - a model defined in Swagger"""  # noqa: E501

        self._vlan = None
        self._ip_address = None
        self._mac_address = None
        self.discriminator = None

        if vlan is not None:
            self.vlan = vlan
        if ip_address is not None:
            self.ip_address = ip_address
        if mac_address is not None:
            self.mac_address = mac_address

    @property
    def vlan(self):
        """Gets the vlan of this PacketAddressClassifier.  # noqa: E501


        :return: The vlan of this PacketAddressClassifier.  # noqa: E501
        :rtype: int
        """
        return self._vlan

    @vlan.setter
    def vlan(self, vlan):
        """Sets the vlan of this PacketAddressClassifier.


        :param vlan: The vlan of this PacketAddressClassifier.  # noqa: E501
        :type: int
        """

        self._vlan = vlan

    @property
    def ip_address(self):
        """Gets the ip_address of this PacketAddressClassifier.  # noqa: E501

        A single IP address or a subnet, e.g. x.x.x.x or x.x.x.x/y  # noqa: E501

        :return: The ip_address of this PacketAddressClassifier.  # noqa: E501
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """Sets the ip_address of this PacketAddressClassifier.

        A single IP address or a subnet, e.g. x.x.x.x or x.x.x.x/y  # noqa: E501

        :param ip_address: The ip_address of this PacketAddressClassifier.  # noqa: E501
        :type: str
        """

        self._ip_address = ip_address

    @property
    def mac_address(self):
        """Gets the mac_address of this PacketAddressClassifier.  # noqa: E501

        A single MAC address  # noqa: E501

        :return: The mac_address of this PacketAddressClassifier.  # noqa: E501
        :rtype: str
        """
        return self._mac_address

    @mac_address.setter
    def mac_address(self, mac_address):
        """Sets the mac_address of this PacketAddressClassifier.

        A single MAC address  # noqa: E501

        :param mac_address: The mac_address of this PacketAddressClassifier.  # noqa: E501
        :type: str
        """
        if mac_address is not None and not re.search('^(([0-9A-Fa-f]{2}[:]){5}([0-9A-Fa-f]{2}))|(([0-9A-Fa-f]{2}[-]){5}([0-9A-Fa-f]{2}))$', mac_address):  # noqa: E501
            raise ValueError("Invalid value for `mac_address`, must be a follow pattern or equal to `/^(([0-9A-Fa-f]{2}[:]){5}([0-9A-Fa-f]{2}))|(([0-9A-Fa-f]{2}[-]){5}([0-9A-Fa-f]{2}))$/`")  # noqa: E501

        self._mac_address = mac_address

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
        if not isinstance(other, PacketAddressClassifier):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
