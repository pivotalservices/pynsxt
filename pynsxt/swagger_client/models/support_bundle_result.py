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

from swagger_client.models.failed_node_support_bundle_result import FailedNodeSupportBundleResult  # noqa: F401,E501
from swagger_client.models.remaining_support_bundle_node import RemainingSupportBundleNode  # noqa: F401,E501
from swagger_client.models.success_node_support_bundle_result import SuccessNodeSupportBundleResult  # noqa: F401,E501
from swagger_client.models.support_bundle_request import SupportBundleRequest  # noqa: F401,E501


class SupportBundleResult(object):
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
        'request_properties': 'SupportBundleRequest',
        'remaining_nodes': 'list[RemainingSupportBundleNode]',
        'success_nodes': 'list[SuccessNodeSupportBundleResult]',
        'failed_nodes': 'list[FailedNodeSupportBundleResult]'
    }

    attribute_map = {
        'request_properties': 'request_properties',
        'remaining_nodes': 'remaining_nodes',
        'success_nodes': 'success_nodes',
        'failed_nodes': 'failed_nodes'
    }

    def __init__(self, request_properties=None, remaining_nodes=None, success_nodes=None, failed_nodes=None):  # noqa: E501
        """SupportBundleResult - a model defined in Swagger"""  # noqa: E501

        self._request_properties = None
        self._remaining_nodes = None
        self._success_nodes = None
        self._failed_nodes = None
        self.discriminator = None

        if request_properties is not None:
            self.request_properties = request_properties
        if remaining_nodes is not None:
            self.remaining_nodes = remaining_nodes
        if success_nodes is not None:
            self.success_nodes = success_nodes
        if failed_nodes is not None:
            self.failed_nodes = failed_nodes

    @property
    def request_properties(self):
        """Gets the request_properties of this SupportBundleResult.  # noqa: E501

        Request properties  # noqa: E501

        :return: The request_properties of this SupportBundleResult.  # noqa: E501
        :rtype: SupportBundleRequest
        """
        return self._request_properties

    @request_properties.setter
    def request_properties(self, request_properties):
        """Sets the request_properties of this SupportBundleResult.

        Request properties  # noqa: E501

        :param request_properties: The request_properties of this SupportBundleResult.  # noqa: E501
        :type: SupportBundleRequest
        """

        self._request_properties = request_properties

    @property
    def remaining_nodes(self):
        """Gets the remaining_nodes of this SupportBundleResult.  # noqa: E501

        Nodes where bundle generation is pending or in progress  # noqa: E501

        :return: The remaining_nodes of this SupportBundleResult.  # noqa: E501
        :rtype: list[RemainingSupportBundleNode]
        """
        return self._remaining_nodes

    @remaining_nodes.setter
    def remaining_nodes(self, remaining_nodes):
        """Sets the remaining_nodes of this SupportBundleResult.

        Nodes where bundle generation is pending or in progress  # noqa: E501

        :param remaining_nodes: The remaining_nodes of this SupportBundleResult.  # noqa: E501
        :type: list[RemainingSupportBundleNode]
        """

        self._remaining_nodes = remaining_nodes

    @property
    def success_nodes(self):
        """Gets the success_nodes of this SupportBundleResult.  # noqa: E501

        Nodes whose bundles were successfully copied to remote file server  # noqa: E501

        :return: The success_nodes of this SupportBundleResult.  # noqa: E501
        :rtype: list[SuccessNodeSupportBundleResult]
        """
        return self._success_nodes

    @success_nodes.setter
    def success_nodes(self, success_nodes):
        """Sets the success_nodes of this SupportBundleResult.

        Nodes whose bundles were successfully copied to remote file server  # noqa: E501

        :param success_nodes: The success_nodes of this SupportBundleResult.  # noqa: E501
        :type: list[SuccessNodeSupportBundleResult]
        """

        self._success_nodes = success_nodes

    @property
    def failed_nodes(self):
        """Gets the failed_nodes of this SupportBundleResult.  # noqa: E501

        Nodes where bundles were not generated or not copied to remote server  # noqa: E501

        :return: The failed_nodes of this SupportBundleResult.  # noqa: E501
        :rtype: list[FailedNodeSupportBundleResult]
        """
        return self._failed_nodes

    @failed_nodes.setter
    def failed_nodes(self, failed_nodes):
        """Sets the failed_nodes of this SupportBundleResult.

        Nodes where bundles were not generated or not copied to remote server  # noqa: E501

        :param failed_nodes: The failed_nodes of this SupportBundleResult.  # noqa: E501
        :type: list[FailedNodeSupportBundleResult]
        """

        self._failed_nodes = failed_nodes

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
        if not isinstance(other, SupportBundleResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other