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

from swagger_client.models.logical_router_port_counters import LogicalRouterPortCounters  # noqa: F401,E501


class AggregatedLogicalRouterPortCounters(object):
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
        'last_update_timestamp': 'int',
        'rx': 'LogicalRouterPortCounters',
        'tx': 'LogicalRouterPortCounters'
    }

    attribute_map = {
        'last_update_timestamp': 'last_update_timestamp',
        'rx': 'rx',
        'tx': 'tx'
    }

    def __init__(self, last_update_timestamp=None, rx=None, tx=None):  # noqa: E501
        """AggregatedLogicalRouterPortCounters - a model defined in Swagger"""  # noqa: E501

        self._last_update_timestamp = None
        self._rx = None
        self._tx = None
        self.discriminator = None

        if last_update_timestamp is not None:
            self.last_update_timestamp = last_update_timestamp
        if rx is not None:
            self.rx = rx
        if tx is not None:
            self.tx = tx

    @property
    def last_update_timestamp(self):
        """Gets the last_update_timestamp of this AggregatedLogicalRouterPortCounters.  # noqa: E501

        Timestamp when the data was last updated; unset if data source has never updated the data.  # noqa: E501

        :return: The last_update_timestamp of this AggregatedLogicalRouterPortCounters.  # noqa: E501
        :rtype: int
        """
        return self._last_update_timestamp

    @last_update_timestamp.setter
    def last_update_timestamp(self, last_update_timestamp):
        """Sets the last_update_timestamp of this AggregatedLogicalRouterPortCounters.

        Timestamp when the data was last updated; unset if data source has never updated the data.  # noqa: E501

        :param last_update_timestamp: The last_update_timestamp of this AggregatedLogicalRouterPortCounters.  # noqa: E501
        :type: int
        """

        self._last_update_timestamp = last_update_timestamp

    @property
    def rx(self):
        """Gets the rx of this AggregatedLogicalRouterPortCounters.  # noqa: E501


        :return: The rx of this AggregatedLogicalRouterPortCounters.  # noqa: E501
        :rtype: LogicalRouterPortCounters
        """
        return self._rx

    @rx.setter
    def rx(self, rx):
        """Sets the rx of this AggregatedLogicalRouterPortCounters.


        :param rx: The rx of this AggregatedLogicalRouterPortCounters.  # noqa: E501
        :type: LogicalRouterPortCounters
        """

        self._rx = rx

    @property
    def tx(self):
        """Gets the tx of this AggregatedLogicalRouterPortCounters.  # noqa: E501


        :return: The tx of this AggregatedLogicalRouterPortCounters.  # noqa: E501
        :rtype: LogicalRouterPortCounters
        """
        return self._tx

    @tx.setter
    def tx(self, tx):
        """Sets the tx of this AggregatedLogicalRouterPortCounters.


        :param tx: The tx of this AggregatedLogicalRouterPortCounters.  # noqa: E501
        :type: LogicalRouterPortCounters
        """

        self._tx = tx

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
        if not isinstance(other, AggregatedLogicalRouterPortCounters):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
