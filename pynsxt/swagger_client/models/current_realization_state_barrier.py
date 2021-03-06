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


class CurrentRealizationStateBarrier(object):
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
        'current_barrier_number': 'int'
    }

    attribute_map = {
        'current_barrier_number': 'current_barrier_number'
    }

    def __init__(self, current_barrier_number=None):  # noqa: E501
        """CurrentRealizationStateBarrier - a model defined in Swagger"""  # noqa: E501

        self._current_barrier_number = None
        self.discriminator = None

        if current_barrier_number is not None:
            self.current_barrier_number = current_barrier_number

    @property
    def current_barrier_number(self):
        """Gets the current_barrier_number of this CurrentRealizationStateBarrier.  # noqa: E501

        Gives the current global barrier number for NSX  # noqa: E501

        :return: The current_barrier_number of this CurrentRealizationStateBarrier.  # noqa: E501
        :rtype: int
        """
        return self._current_barrier_number

    @current_barrier_number.setter
    def current_barrier_number(self, current_barrier_number):
        """Sets the current_barrier_number of this CurrentRealizationStateBarrier.

        Gives the current global barrier number for NSX  # noqa: E501

        :param current_barrier_number: The current_barrier_number of this CurrentRealizationStateBarrier.  # noqa: E501
        :type: int
        """

        self._current_barrier_number = current_barrier_number

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
        if not isinstance(other, CurrentRealizationStateBarrier):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
