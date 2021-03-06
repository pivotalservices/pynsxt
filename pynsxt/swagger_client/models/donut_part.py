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

from swagger_client.models.label import Label  # noqa: F401,E501
from swagger_client.models.render_configuration import RenderConfiguration  # noqa: F401,E501
from swagger_client.models.tooltip import Tooltip  # noqa: F401,E501


class DonutPart(object):
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
        'field': 'str',
        'render_configuration': 'list[RenderConfiguration]',
        'tooltip': 'list[Tooltip]',
        'label': 'Label'
    }

    attribute_map = {
        'field': 'field',
        'render_configuration': 'render_configuration',
        'tooltip': 'tooltip',
        'label': 'label'
    }

    def __init__(self, field=None, render_configuration=None, tooltip=None, label=None):  # noqa: E501
        """DonutPart - a model defined in Swagger"""  # noqa: E501

        self._field = None
        self._render_configuration = None
        self._tooltip = None
        self._label = None
        self.discriminator = None

        self.field = field
        if render_configuration is not None:
            self.render_configuration = render_configuration
        if tooltip is not None:
            self.tooltip = tooltip
        if label is not None:
            self.label = label

    @property
    def field(self):
        """Gets the field of this DonutPart.  # noqa: E501

        A numerical value that represents the portion or entity of the donut chart.  # noqa: E501

        :return: The field of this DonutPart.  # noqa: E501
        :rtype: str
        """
        return self._field

    @field.setter
    def field(self, field):
        """Sets the field of this DonutPart.

        A numerical value that represents the portion or entity of the donut chart.  # noqa: E501

        :param field: The field of this DonutPart.  # noqa: E501
        :type: str
        """
        if field is None:
            raise ValueError("Invalid value for `field`, must not be `None`")  # noqa: E501

        self._field = field

    @property
    def render_configuration(self):
        """Gets the render_configuration of this DonutPart.  # noqa: E501

        Additional rendering or conditional evaluation of the field values to be performed, if any.  # noqa: E501

        :return: The render_configuration of this DonutPart.  # noqa: E501
        :rtype: list[RenderConfiguration]
        """
        return self._render_configuration

    @render_configuration.setter
    def render_configuration(self, render_configuration):
        """Sets the render_configuration of this DonutPart.

        Additional rendering or conditional evaluation of the field values to be performed, if any.  # noqa: E501

        :param render_configuration: The render_configuration of this DonutPart.  # noqa: E501
        :type: list[RenderConfiguration]
        """

        self._render_configuration = render_configuration

    @property
    def tooltip(self):
        """Gets the tooltip of this DonutPart.  # noqa: E501

        Multi-line text to be shown on tooltip while hovering over the portion.  # noqa: E501

        :return: The tooltip of this DonutPart.  # noqa: E501
        :rtype: list[Tooltip]
        """
        return self._tooltip

    @tooltip.setter
    def tooltip(self, tooltip):
        """Sets the tooltip of this DonutPart.

        Multi-line text to be shown on tooltip while hovering over the portion.  # noqa: E501

        :param tooltip: The tooltip of this DonutPart.  # noqa: E501
        :type: list[Tooltip]
        """

        self._tooltip = tooltip

    @property
    def label(self):
        """Gets the label of this DonutPart.  # noqa: E501

        If a section 'template' holds this donut part, then the label is auto-generated from the fetched field values after applying the template.  # noqa: E501

        :return: The label of this DonutPart.  # noqa: E501
        :rtype: Label
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this DonutPart.

        If a section 'template' holds this donut part, then the label is auto-generated from the fetched field values after applying the template.  # noqa: E501

        :param label: The label of this DonutPart.  # noqa: E501
        :type: Label
        """

        self._label = label

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
        if not isinstance(other, DonutPart):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
