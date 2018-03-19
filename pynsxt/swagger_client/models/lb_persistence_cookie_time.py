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

from swagger_client.models.lb_cookie_time import LbCookieTime  # noqa: F401,E501


class LbPersistenceCookieTime(object):
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
        'cookie_max_idle': 'int'
    }

    attribute_map = {
        'cookie_max_idle': 'cookie_max_idle'
    }

    def __init__(self, cookie_max_idle=None):  # noqa: E501
        """LbPersistenceCookieTime - a model defined in Swagger"""  # noqa: E501

        self._cookie_max_idle = None
        self.discriminator = None

        self.cookie_max_idle = cookie_max_idle

    @property
    def cookie_max_idle(self):
        """Gets the cookie_max_idle of this LbPersistenceCookieTime.  # noqa: E501

        HTTP cookie max-age to expire cookie, only available for insert mode.   # noqa: E501

        :return: The cookie_max_idle of this LbPersistenceCookieTime.  # noqa: E501
        :rtype: int
        """
        return self._cookie_max_idle

    @cookie_max_idle.setter
    def cookie_max_idle(self, cookie_max_idle):
        """Sets the cookie_max_idle of this LbPersistenceCookieTime.

        HTTP cookie max-age to expire cookie, only available for insert mode.   # noqa: E501

        :param cookie_max_idle: The cookie_max_idle of this LbPersistenceCookieTime.  # noqa: E501
        :type: int
        """
        if cookie_max_idle is None:
            raise ValueError("Invalid value for `cookie_max_idle`, must not be `None`")  # noqa: E501
        if cookie_max_idle is not None and cookie_max_idle > 2147483647:  # noqa: E501
            raise ValueError("Invalid value for `cookie_max_idle`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if cookie_max_idle is not None and cookie_max_idle < 1:  # noqa: E501
            raise ValueError("Invalid value for `cookie_max_idle`, must be a value greater than or equal to `1`")  # noqa: E501

        self._cookie_max_idle = cookie_max_idle

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
        if not isinstance(other, LbPersistenceCookieTime):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other