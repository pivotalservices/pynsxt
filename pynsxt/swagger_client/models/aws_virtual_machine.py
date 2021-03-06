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

from swagger_client.models.cloud_tag import CloudTag  # noqa: F401,E501
from swagger_client.models.cloud_virtual_machine import CloudVirtualMachine  # noqa: F401,E501
from swagger_client.models.compute_instance_error_message import ComputeInstanceErrorMessage  # noqa: F401,E501
from swagger_client.models.resource_link import ResourceLink  # noqa: F401,E501
from swagger_client.models.self_resource_link import SelfResourceLink  # noqa: F401,E501
from swagger_client.models.tag import Tag  # noqa: F401,E501


class AwsVirtualMachine(object):
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
        'vpc_name': 'str',
        'region': 'str',
        'power_state': 'str',
        'vpc': 'str',
        'availability_zone': 'str'
    }

    attribute_map = {
        'vpc_name': 'vpc_name',
        'region': 'region',
        'power_state': 'power_state',
        'vpc': 'vpc',
        'availability_zone': 'availability_zone'
    }

    def __init__(self, vpc_name=None, region=None, power_state=None, vpc=None, availability_zone=None):  # noqa: E501
        """AwsVirtualMachine - a model defined in Swagger"""  # noqa: E501

        self._vpc_name = None
        self._region = None
        self._power_state = None
        self._vpc = None
        self._availability_zone = None
        self.discriminator = None

        if vpc_name is not None:
            self.vpc_name = vpc_name
        if region is not None:
            self.region = region
        if power_state is not None:
            self.power_state = power_state
        if vpc is not None:
            self.vpc = vpc
        if availability_zone is not None:
            self.availability_zone = availability_zone

    @property
    def vpc_name(self):
        """Gets the vpc_name of this AwsVirtualMachine.  # noqa: E501

        VPC name of the virtual machine  # noqa: E501

        :return: The vpc_name of this AwsVirtualMachine.  # noqa: E501
        :rtype: str
        """
        return self._vpc_name

    @vpc_name.setter
    def vpc_name(self, vpc_name):
        """Sets the vpc_name of this AwsVirtualMachine.

        VPC name of the virtual machine  # noqa: E501

        :param vpc_name: The vpc_name of this AwsVirtualMachine.  # noqa: E501
        :type: str
        """

        self._vpc_name = vpc_name

    @property
    def region(self):
        """Gets the region of this AwsVirtualMachine.  # noqa: E501

        Region of the virtual machine  # noqa: E501

        :return: The region of this AwsVirtualMachine.  # noqa: E501
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this AwsVirtualMachine.

        Region of the virtual machine  # noqa: E501

        :param region: The region of this AwsVirtualMachine.  # noqa: E501
        :type: str
        """

        self._region = region

    @property
    def power_state(self):
        """Gets the power_state of this AwsVirtualMachine.  # noqa: E501

        Indicates the power state of the virutal machine as returned by AWS.   # noqa: E501

        :return: The power_state of this AwsVirtualMachine.  # noqa: E501
        :rtype: str
        """
        return self._power_state

    @power_state.setter
    def power_state(self, power_state):
        """Sets the power_state of this AwsVirtualMachine.

        Indicates the power state of the virutal machine as returned by AWS.   # noqa: E501

        :param power_state: The power_state of this AwsVirtualMachine.  # noqa: E501
        :type: str
        """
        allowed_values = ["PENDING", "RUNNING", "SHUTTING_DOWN", "TERMINATED", "STOPPING", "STOPPED"]  # noqa: E501
        if power_state not in allowed_values:
            raise ValueError(
                "Invalid value for `power_state` ({0}), must be one of {1}"  # noqa: E501
                .format(power_state, allowed_values)
            )

        self._power_state = power_state

    @property
    def vpc(self):
        """Gets the vpc of this AwsVirtualMachine.  # noqa: E501

        VPC id of the virtual machine  # noqa: E501

        :return: The vpc of this AwsVirtualMachine.  # noqa: E501
        :rtype: str
        """
        return self._vpc

    @vpc.setter
    def vpc(self, vpc):
        """Sets the vpc of this AwsVirtualMachine.

        VPC id of the virtual machine  # noqa: E501

        :param vpc: The vpc of this AwsVirtualMachine.  # noqa: E501
        :type: str
        """

        self._vpc = vpc

    @property
    def availability_zone(self):
        """Gets the availability_zone of this AwsVirtualMachine.  # noqa: E501

        Availability Zone of the virtual machine  # noqa: E501

        :return: The availability_zone of this AwsVirtualMachine.  # noqa: E501
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        """Sets the availability_zone of this AwsVirtualMachine.

        Availability Zone of the virtual machine  # noqa: E501

        :param availability_zone: The availability_zone of this AwsVirtualMachine.  # noqa: E501
        :type: str
        """

        self._availability_zone = availability_zone

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
        if not isinstance(other, AwsVirtualMachine):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
