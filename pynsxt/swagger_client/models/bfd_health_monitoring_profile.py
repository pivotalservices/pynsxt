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

from swagger_client.models.resource_link import ResourceLink  # noqa: F401,E501
from swagger_client.models.self_resource_link import SelfResourceLink  # noqa: F401,E501
from swagger_client.models.tag import Tag  # noqa: F401,E501
from swagger_client.models.transport_zone_profile import TransportZoneProfile  # noqa: F401,E501


class BfdHealthMonitoringProfile(object):
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
        'probe_interval': 'int',
        'enabled': 'bool'
    }

    attribute_map = {
        'probe_interval': 'probe_interval',
        'enabled': 'enabled'
    }

    def __init__(self, probe_interval=1000, enabled=None):  # noqa: E501
        """BfdHealthMonitoringProfile - a model defined in Swagger"""  # noqa: E501

        self._probe_interval = None
        self._enabled = None
        self.discriminator = None

        if probe_interval is not None:
            self.probe_interval = probe_interval
        self.enabled = enabled

    @property
    def probe_interval(self):
        """Gets the probe_interval of this BfdHealthMonitoringProfile.  # noqa: E501

        The time interval (in millisec) between probe packets for tunnels between transport nodes.  # noqa: E501

        :return: The probe_interval of this BfdHealthMonitoringProfile.  # noqa: E501
        :rtype: int
        """
        return self._probe_interval

    @probe_interval.setter
    def probe_interval(self, probe_interval):
        """Sets the probe_interval of this BfdHealthMonitoringProfile.

        The time interval (in millisec) between probe packets for tunnels between transport nodes.  # noqa: E501

        :param probe_interval: The probe_interval of this BfdHealthMonitoringProfile.  # noqa: E501
        :type: int
        """
        if probe_interval is not None and probe_interval < 300:  # noqa: E501
            raise ValueError("Invalid value for `probe_interval`, must be a value greater than or equal to `300`")  # noqa: E501

        self._probe_interval = probe_interval

    @property
    def enabled(self):
        """Gets the enabled of this BfdHealthMonitoringProfile.  # noqa: E501

        Whether the heartbeat is enabled. A POST or PUT request with \"enabled\" false (with no probe intervals) will set (POST) or reset (PUT) the probe_interval to their default value.  # noqa: E501

        :return: The enabled of this BfdHealthMonitoringProfile.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this BfdHealthMonitoringProfile.

        Whether the heartbeat is enabled. A POST or PUT request with \"enabled\" false (with no probe intervals) will set (POST) or reset (PUT) the probe_interval to their default value.  # noqa: E501

        :param enabled: The enabled of this BfdHealthMonitoringProfile.  # noqa: E501
        :type: bool
        """
        if enabled is None:
            raise ValueError("Invalid value for `enabled`, must not be `None`")  # noqa: E501

        self._enabled = enabled

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
        if not isinstance(other, BfdHealthMonitoringProfile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other