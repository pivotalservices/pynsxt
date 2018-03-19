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

from swagger_client.models.status_count import StatusCount  # noqa: F401,E501
from swagger_client.models.tunnel_status_count import TunnelStatusCount  # noqa: F401,E501


class TransportNodeStatus(object):
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
        'status': 'str',
        'node_uuid': 'str',
        'mgmt_connection_status': 'str',
        'control_connection_status': 'StatusCount',
        'pnic_status': 'StatusCount',
        'node_display_name': 'str',
        'tunnel_status': 'TunnelStatusCount'
    }

    attribute_map = {
        'status': 'status',
        'node_uuid': 'node_uuid',
        'mgmt_connection_status': 'mgmt_connection_status',
        'control_connection_status': 'control_connection_status',
        'pnic_status': 'pnic_status',
        'node_display_name': 'node_display_name',
        'tunnel_status': 'tunnel_status'
    }

    def __init__(self, status=None, node_uuid=None, mgmt_connection_status=None, control_connection_status=None, pnic_status=None, node_display_name=None, tunnel_status=None):  # noqa: E501
        """TransportNodeStatus - a model defined in Swagger"""  # noqa: E501

        self._status = None
        self._node_uuid = None
        self._mgmt_connection_status = None
        self._control_connection_status = None
        self._pnic_status = None
        self._node_display_name = None
        self._tunnel_status = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if node_uuid is not None:
            self.node_uuid = node_uuid
        if mgmt_connection_status is not None:
            self.mgmt_connection_status = mgmt_connection_status
        if control_connection_status is not None:
            self.control_connection_status = control_connection_status
        if pnic_status is not None:
            self.pnic_status = pnic_status
        if node_display_name is not None:
            self.node_display_name = node_display_name
        if tunnel_status is not None:
            self.tunnel_status = tunnel_status

    @property
    def status(self):
        """Gets the status of this TransportNodeStatus.  # noqa: E501

        Roll-up status of pNIC, management connection, control connection, tunnel status  # noqa: E501

        :return: The status of this TransportNodeStatus.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this TransportNodeStatus.

        Roll-up status of pNIC, management connection, control connection, tunnel status  # noqa: E501

        :param status: The status of this TransportNodeStatus.  # noqa: E501
        :type: str
        """
        allowed_values = ["UP", "DOWN", "DEGRADED", "UNKNOWN"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def node_uuid(self):
        """Gets the node_uuid of this TransportNodeStatus.  # noqa: E501

        Transport node uuid  # noqa: E501

        :return: The node_uuid of this TransportNodeStatus.  # noqa: E501
        :rtype: str
        """
        return self._node_uuid

    @node_uuid.setter
    def node_uuid(self, node_uuid):
        """Sets the node_uuid of this TransportNodeStatus.

        Transport node uuid  # noqa: E501

        :param node_uuid: The node_uuid of this TransportNodeStatus.  # noqa: E501
        :type: str
        """

        self._node_uuid = node_uuid

    @property
    def mgmt_connection_status(self):
        """Gets the mgmt_connection_status of this TransportNodeStatus.  # noqa: E501

        Management connection status  # noqa: E501

        :return: The mgmt_connection_status of this TransportNodeStatus.  # noqa: E501
        :rtype: str
        """
        return self._mgmt_connection_status

    @mgmt_connection_status.setter
    def mgmt_connection_status(self, mgmt_connection_status):
        """Sets the mgmt_connection_status of this TransportNodeStatus.

        Management connection status  # noqa: E501

        :param mgmt_connection_status: The mgmt_connection_status of this TransportNodeStatus.  # noqa: E501
        :type: str
        """
        allowed_values = ["UP", "DOWN"]  # noqa: E501
        if mgmt_connection_status not in allowed_values:
            raise ValueError(
                "Invalid value for `mgmt_connection_status` ({0}), must be one of {1}"  # noqa: E501
                .format(mgmt_connection_status, allowed_values)
            )

        self._mgmt_connection_status = mgmt_connection_status

    @property
    def control_connection_status(self):
        """Gets the control_connection_status of this TransportNodeStatus.  # noqa: E501

        Control connection status  # noqa: E501

        :return: The control_connection_status of this TransportNodeStatus.  # noqa: E501
        :rtype: StatusCount
        """
        return self._control_connection_status

    @control_connection_status.setter
    def control_connection_status(self, control_connection_status):
        """Sets the control_connection_status of this TransportNodeStatus.

        Control connection status  # noqa: E501

        :param control_connection_status: The control_connection_status of this TransportNodeStatus.  # noqa: E501
        :type: StatusCount
        """

        self._control_connection_status = control_connection_status

    @property
    def pnic_status(self):
        """Gets the pnic_status of this TransportNodeStatus.  # noqa: E501

        pNIC status  # noqa: E501

        :return: The pnic_status of this TransportNodeStatus.  # noqa: E501
        :rtype: StatusCount
        """
        return self._pnic_status

    @pnic_status.setter
    def pnic_status(self, pnic_status):
        """Sets the pnic_status of this TransportNodeStatus.

        pNIC status  # noqa: E501

        :param pnic_status: The pnic_status of this TransportNodeStatus.  # noqa: E501
        :type: StatusCount
        """

        self._pnic_status = pnic_status

    @property
    def node_display_name(self):
        """Gets the node_display_name of this TransportNodeStatus.  # noqa: E501

        Transport node display name  # noqa: E501

        :return: The node_display_name of this TransportNodeStatus.  # noqa: E501
        :rtype: str
        """
        return self._node_display_name

    @node_display_name.setter
    def node_display_name(self, node_display_name):
        """Sets the node_display_name of this TransportNodeStatus.

        Transport node display name  # noqa: E501

        :param node_display_name: The node_display_name of this TransportNodeStatus.  # noqa: E501
        :type: str
        """

        self._node_display_name = node_display_name

    @property
    def tunnel_status(self):
        """Gets the tunnel_status of this TransportNodeStatus.  # noqa: E501

        Tunnel Status  # noqa: E501

        :return: The tunnel_status of this TransportNodeStatus.  # noqa: E501
        :rtype: TunnelStatusCount
        """
        return self._tunnel_status

    @tunnel_status.setter
    def tunnel_status(self, tunnel_status):
        """Sets the tunnel_status of this TransportNodeStatus.

        Tunnel Status  # noqa: E501

        :param tunnel_status: The tunnel_status of this TransportNodeStatus.  # noqa: E501
        :type: TunnelStatusCount
        """

        self._tunnel_status = tunnel_status

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
        if not isinstance(other, TransportNodeStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other