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


class TransportZoneStatus(object):
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
        'num_logical_ports': 'int',
        'transport_zone_id': 'str',
        'num_logical_switches': 'int',
        'num_transport_nodes': 'int'
    }

    attribute_map = {
        'num_logical_ports': 'num_logical_ports',
        'transport_zone_id': 'transport_zone_id',
        'num_logical_switches': 'num_logical_switches',
        'num_transport_nodes': 'num_transport_nodes'
    }

    def __init__(self, num_logical_ports=None, transport_zone_id=None, num_logical_switches=None, num_transport_nodes=None):  # noqa: E501
        """TransportZoneStatus - a model defined in Swagger"""  # noqa: E501

        self._num_logical_ports = None
        self._transport_zone_id = None
        self._num_logical_switches = None
        self._num_transport_nodes = None
        self.discriminator = None

        if num_logical_ports is not None:
            self.num_logical_ports = num_logical_ports
        if transport_zone_id is not None:
            self.transport_zone_id = transport_zone_id
        if num_logical_switches is not None:
            self.num_logical_switches = num_logical_switches
        if num_transport_nodes is not None:
            self.num_transport_nodes = num_transport_nodes

    @property
    def num_logical_ports(self):
        """Gets the num_logical_ports of this TransportZoneStatus.  # noqa: E501

        Count of logical ports in the transport zone  # noqa: E501

        :return: The num_logical_ports of this TransportZoneStatus.  # noqa: E501
        :rtype: int
        """
        return self._num_logical_ports

    @num_logical_ports.setter
    def num_logical_ports(self, num_logical_ports):
        """Sets the num_logical_ports of this TransportZoneStatus.

        Count of logical ports in the transport zone  # noqa: E501

        :param num_logical_ports: The num_logical_ports of this TransportZoneStatus.  # noqa: E501
        :type: int
        """

        self._num_logical_ports = num_logical_ports

    @property
    def transport_zone_id(self):
        """Gets the transport_zone_id of this TransportZoneStatus.  # noqa: E501

        Unique ID identifying the transport zone  # noqa: E501

        :return: The transport_zone_id of this TransportZoneStatus.  # noqa: E501
        :rtype: str
        """
        return self._transport_zone_id

    @transport_zone_id.setter
    def transport_zone_id(self, transport_zone_id):
        """Sets the transport_zone_id of this TransportZoneStatus.

        Unique ID identifying the transport zone  # noqa: E501

        :param transport_zone_id: The transport_zone_id of this TransportZoneStatus.  # noqa: E501
        :type: str
        """

        self._transport_zone_id = transport_zone_id

    @property
    def num_logical_switches(self):
        """Gets the num_logical_switches of this TransportZoneStatus.  # noqa: E501

        Count of logical switches in the transport zone  # noqa: E501

        :return: The num_logical_switches of this TransportZoneStatus.  # noqa: E501
        :rtype: int
        """
        return self._num_logical_switches

    @num_logical_switches.setter
    def num_logical_switches(self, num_logical_switches):
        """Sets the num_logical_switches of this TransportZoneStatus.

        Count of logical switches in the transport zone  # noqa: E501

        :param num_logical_switches: The num_logical_switches of this TransportZoneStatus.  # noqa: E501
        :type: int
        """

        self._num_logical_switches = num_logical_switches

    @property
    def num_transport_nodes(self):
        """Gets the num_transport_nodes of this TransportZoneStatus.  # noqa: E501

        Count of transport nodes in the transport zone  # noqa: E501

        :return: The num_transport_nodes of this TransportZoneStatus.  # noqa: E501
        :rtype: int
        """
        return self._num_transport_nodes

    @num_transport_nodes.setter
    def num_transport_nodes(self, num_transport_nodes):
        """Sets the num_transport_nodes of this TransportZoneStatus.

        Count of transport nodes in the transport zone  # noqa: E501

        :param num_transport_nodes: The num_transport_nodes of this TransportZoneStatus.  # noqa: E501
        :type: int
        """

        self._num_transport_nodes = num_transport_nodes

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
        if not isinstance(other, TransportZoneStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other