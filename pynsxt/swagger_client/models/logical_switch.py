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

from swagger_client.models.managed_resource import ManagedResource  # noqa: F401,E501
from swagger_client.models.packet_address_classifier import PacketAddressClassifier  # noqa: F401,E501
from swagger_client.models.resource_link import ResourceLink  # noqa: F401,E501
from swagger_client.models.self_resource_link import SelfResourceLink  # noqa: F401,E501
from swagger_client.models.switching_profile_type_id_entry import SwitchingProfileTypeIdEntry  # noqa: F401,E501
from swagger_client.models.tag import Tag  # noqa: F401,E501


class LogicalSwitch(object):
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
        '_self': 'SelfResourceLink',
        'links': 'list[ResourceLink]',
        'schema': 'str',
        'revision': 'int',
        'system_owned': 'bool',
        'display_name': 'str',
        'description': 'str',
        'tags': 'list[Tag]',
        'create_user': 'str',
        'protection': 'str',
        'create_time': 'int',
        'last_modified_time': 'int',
        'last_modified_user': 'str',
        'id': 'str',
        'resource_type': 'str',
        'replication_mode': 'str',
        'admin_state': 'str',
        'address_bindings': 'list[PacketAddressClassifier]',
        'transport_zone_id': 'str',
        'ip_pool_id': 'str',
        'vlan': 'int',
        'switching_profile_ids': 'list[SwitchingProfileTypeIdEntry]',
        'mac_pool_id': 'str',
        'vni': 'int'
    }

    attribute_map = {
        '_self': '_self',
        'links': '_links',
        'schema': '_schema',
        'revision': '_revision',
        'system_owned': '_system_owned',
        'display_name': 'display_name',
        'description': 'description',
        'tags': 'tags',
        'create_user': '_create_user',
        'protection': '_protection',
        'create_time': '_create_time',
        'last_modified_time': '_last_modified_time',
        'last_modified_user': '_last_modified_user',
        'id': 'id',
        'resource_type': 'resource_type',
        'replication_mode': 'replication_mode',
        'admin_state': 'admin_state',
        'address_bindings': 'address_bindings',
        'transport_zone_id': 'transport_zone_id',
        'ip_pool_id': 'ip_pool_id',
        'vlan': 'vlan',
        'switching_profile_ids': 'switching_profile_ids',
        'mac_pool_id': 'mac_pool_id',
        'vni': 'vni'
    }

    def __init__(self, _self=None, links=None, schema=None, revision=None, system_owned=None, display_name=None, description=None, tags=None, create_user=None, protection=None, create_time=None, last_modified_time=None, last_modified_user=None, id=None, resource_type=None, replication_mode=None, admin_state=None, address_bindings=None, transport_zone_id=None, ip_pool_id=None, vlan=None, switching_profile_ids=None, mac_pool_id=None, vni=None):  # noqa: E501
        """LogicalSwitch - a model defined in Swagger"""  # noqa: E501

        self.__self = None
        self._links = None
        self._schema = None
        self._revision = None
        self._system_owned = None
        self._display_name = None
        self._description = None
        self._tags = None
        self._create_user = None
        self._protection = None
        self._create_time = None
        self._last_modified_time = None
        self._last_modified_user = None
        self._id = None
        self._resource_type = None
        self._replication_mode = None
        self._admin_state = None
        self._address_bindings = None
        self._transport_zone_id = None
        self._ip_pool_id = None
        self._vlan = None
        self._switching_profile_ids = None
        self._mac_pool_id = None
        self._vni = None
        self.discriminator = None

        if _self is not None:
            self._self = _self
        if links is not None:
            self.links = links
        if schema is not None:
            self.schema = schema
        if revision is not None:
            self.revision = revision
        if system_owned is not None:
            self.system_owned = system_owned
        if display_name is not None:
            self.display_name = display_name
        if description is not None:
            self.description = description
        if tags is not None:
            self.tags = tags
        if create_user is not None:
            self.create_user = create_user
        if protection is not None:
            self.protection = protection
        if create_time is not None:
            self.create_time = create_time
        if last_modified_time is not None:
            self.last_modified_time = last_modified_time
        if last_modified_user is not None:
            self.last_modified_user = last_modified_user
        if id is not None:
            self.id = id
        if resource_type is not None:
            self.resource_type = resource_type
        if replication_mode is not None:
            self.replication_mode = replication_mode
        self.admin_state = admin_state
        if address_bindings is not None:
            self.address_bindings = address_bindings
        self.transport_zone_id = transport_zone_id
        if ip_pool_id is not None:
            self.ip_pool_id = ip_pool_id
        if vlan is not None:
            self.vlan = vlan
        if switching_profile_ids is not None:
            self.switching_profile_ids = switching_profile_ids
        if mac_pool_id is not None:
            self.mac_pool_id = mac_pool_id
        if vni is not None:
            self.vni = vni

    @property
    def _self(self):
        """Gets the _self of this LogicalSwitch.  # noqa: E501


        :return: The _self of this LogicalSwitch.  # noqa: E501
        :rtype: SelfResourceLink
        """
        return self.__self

    @_self.setter
    def _self(self, _self):
        """Sets the _self of this LogicalSwitch.


        :param _self: The _self of this LogicalSwitch.  # noqa: E501
        :type: SelfResourceLink
        """

        self.__self = _self

    @property
    def links(self):
        """Gets the links of this LogicalSwitch.  # noqa: E501

        The server will populate this field when returing the resource. Ignored on PUT and POST.  # noqa: E501

        :return: The links of this LogicalSwitch.  # noqa: E501
        :rtype: list[ResourceLink]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this LogicalSwitch.

        The server will populate this field when returing the resource. Ignored on PUT and POST.  # noqa: E501

        :param links: The links of this LogicalSwitch.  # noqa: E501
        :type: list[ResourceLink]
        """

        self._links = links

    @property
    def schema(self):
        """Gets the schema of this LogicalSwitch.  # noqa: E501


        :return: The schema of this LogicalSwitch.  # noqa: E501
        :rtype: str
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        """Sets the schema of this LogicalSwitch.


        :param schema: The schema of this LogicalSwitch.  # noqa: E501
        :type: str
        """

        self._schema = schema

    @property
    def revision(self):
        """Gets the revision of this LogicalSwitch.  # noqa: E501

        The _revision property describes the current revision of the resource. To prevent clients from overwriting each other's changes, PUT operations must include the current _revision of the resource, which clients should obtain by issuing a GET operation. If the _revision provided in a PUT request is missing or stale, the operation will be rejected.  # noqa: E501

        :return: The revision of this LogicalSwitch.  # noqa: E501
        :rtype: int
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        """Sets the revision of this LogicalSwitch.

        The _revision property describes the current revision of the resource. To prevent clients from overwriting each other's changes, PUT operations must include the current _revision of the resource, which clients should obtain by issuing a GET operation. If the _revision provided in a PUT request is missing or stale, the operation will be rejected.  # noqa: E501

        :param revision: The revision of this LogicalSwitch.  # noqa: E501
        :type: int
        """

        self._revision = revision

    @property
    def system_owned(self):
        """Gets the system_owned of this LogicalSwitch.  # noqa: E501

        Indicates system owned resource  # noqa: E501

        :return: The system_owned of this LogicalSwitch.  # noqa: E501
        :rtype: bool
        """
        return self._system_owned

    @system_owned.setter
    def system_owned(self, system_owned):
        """Sets the system_owned of this LogicalSwitch.

        Indicates system owned resource  # noqa: E501

        :param system_owned: The system_owned of this LogicalSwitch.  # noqa: E501
        :type: bool
        """

        self._system_owned = system_owned

    @property
    def display_name(self):
        """Gets the display_name of this LogicalSwitch.  # noqa: E501

        Defaults to ID if not set  # noqa: E501

        :return: The display_name of this LogicalSwitch.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this LogicalSwitch.

        Defaults to ID if not set  # noqa: E501

        :param display_name: The display_name of this LogicalSwitch.  # noqa: E501
        :type: str
        """
        if display_name is not None and len(display_name) > 255:
            raise ValueError("Invalid value for `display_name`, length must be less than or equal to `255`")  # noqa: E501

        self._display_name = display_name

    @property
    def description(self):
        """Gets the description of this LogicalSwitch.  # noqa: E501

        Description of this resource  # noqa: E501

        :return: The description of this LogicalSwitch.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this LogicalSwitch.

        Description of this resource  # noqa: E501

        :param description: The description of this LogicalSwitch.  # noqa: E501
        :type: str
        """
        if description is not None and len(description) > 1024:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `1024`")  # noqa: E501

        self._description = description

    @property
    def tags(self):
        """Gets the tags of this LogicalSwitch.  # noqa: E501

        Opaque identifiers meaningful to the API user  # noqa: E501

        :return: The tags of this LogicalSwitch.  # noqa: E501
        :rtype: list[Tag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this LogicalSwitch.

        Opaque identifiers meaningful to the API user  # noqa: E501

        :param tags: The tags of this LogicalSwitch.  # noqa: E501
        :type: list[Tag]
        """

        self._tags = tags

    @property
    def create_user(self):
        """Gets the create_user of this LogicalSwitch.  # noqa: E501

        ID of the user who created this resource  # noqa: E501

        :return: The create_user of this LogicalSwitch.  # noqa: E501
        :rtype: str
        """
        return self._create_user

    @create_user.setter
    def create_user(self, create_user):
        """Sets the create_user of this LogicalSwitch.

        ID of the user who created this resource  # noqa: E501

        :param create_user: The create_user of this LogicalSwitch.  # noqa: E501
        :type: str
        """

        self._create_user = create_user

    @property
    def protection(self):
        """Gets the protection of this LogicalSwitch.  # noqa: E501

        Protection status is one of the following: PROTECTED - the client who retrieved the entity is not allowed             to modify it. NOT_PROTECTED - the client who retrieved the entity is allowed                 to modify it REQUIRE_OVERRIDE - the client who retrieved the entity is a super                    user and can modify it, but only when providing                    the request header X-Allow-Overwrite=true. UNKNOWN - the _protection field could not be determined for this           entity.   # noqa: E501

        :return: The protection of this LogicalSwitch.  # noqa: E501
        :rtype: str
        """
        return self._protection

    @protection.setter
    def protection(self, protection):
        """Sets the protection of this LogicalSwitch.

        Protection status is one of the following: PROTECTED - the client who retrieved the entity is not allowed             to modify it. NOT_PROTECTED - the client who retrieved the entity is allowed                 to modify it REQUIRE_OVERRIDE - the client who retrieved the entity is a super                    user and can modify it, but only when providing                    the request header X-Allow-Overwrite=true. UNKNOWN - the _protection field could not be determined for this           entity.   # noqa: E501

        :param protection: The protection of this LogicalSwitch.  # noqa: E501
        :type: str
        """

        self._protection = protection

    @property
    def create_time(self):
        """Gets the create_time of this LogicalSwitch.  # noqa: E501

        Timestamp of resource creation  # noqa: E501

        :return: The create_time of this LogicalSwitch.  # noqa: E501
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this LogicalSwitch.

        Timestamp of resource creation  # noqa: E501

        :param create_time: The create_time of this LogicalSwitch.  # noqa: E501
        :type: int
        """

        self._create_time = create_time

    @property
    def last_modified_time(self):
        """Gets the last_modified_time of this LogicalSwitch.  # noqa: E501

        Timestamp of last modification  # noqa: E501

        :return: The last_modified_time of this LogicalSwitch.  # noqa: E501
        :rtype: int
        """
        return self._last_modified_time

    @last_modified_time.setter
    def last_modified_time(self, last_modified_time):
        """Sets the last_modified_time of this LogicalSwitch.

        Timestamp of last modification  # noqa: E501

        :param last_modified_time: The last_modified_time of this LogicalSwitch.  # noqa: E501
        :type: int
        """

        self._last_modified_time = last_modified_time

    @property
    def last_modified_user(self):
        """Gets the last_modified_user of this LogicalSwitch.  # noqa: E501

        ID of the user who last modified this resource  # noqa: E501

        :return: The last_modified_user of this LogicalSwitch.  # noqa: E501
        :rtype: str
        """
        return self._last_modified_user

    @last_modified_user.setter
    def last_modified_user(self, last_modified_user):
        """Sets the last_modified_user of this LogicalSwitch.

        ID of the user who last modified this resource  # noqa: E501

        :param last_modified_user: The last_modified_user of this LogicalSwitch.  # noqa: E501
        :type: str
        """

        self._last_modified_user = last_modified_user

    @property
    def id(self):
        """Gets the id of this LogicalSwitch.  # noqa: E501

        Unique identifier of this resource  # noqa: E501

        :return: The id of this LogicalSwitch.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this LogicalSwitch.

        Unique identifier of this resource  # noqa: E501

        :param id: The id of this LogicalSwitch.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def resource_type(self):
        """Gets the resource_type of this LogicalSwitch.  # noqa: E501

        The type of this resource.  # noqa: E501

        :return: The resource_type of this LogicalSwitch.  # noqa: E501
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this LogicalSwitch.

        The type of this resource.  # noqa: E501

        :param resource_type: The resource_type of this LogicalSwitch.  # noqa: E501
        :type: str
        """

        self._resource_type = resource_type

    @property
    def replication_mode(self):
        """Gets the replication_mode of this LogicalSwitch.  # noqa: E501

        Replication mode of the Logical Switch  # noqa: E501

        :return: The replication_mode of this LogicalSwitch.  # noqa: E501
        :rtype: str
        """
        return self._replication_mode

    @replication_mode.setter
    def replication_mode(self, replication_mode):
        """Sets the replication_mode of this LogicalSwitch.

        Replication mode of the Logical Switch  # noqa: E501

        :param replication_mode: The replication_mode of this LogicalSwitch.  # noqa: E501
        :type: str
        """
        allowed_values = ["MTEP", "SOURCE"]  # noqa: E501
        if replication_mode not in allowed_values:
            raise ValueError(
                "Invalid value for `replication_mode` ({0}), must be one of {1}"  # noqa: E501
                .format(replication_mode, allowed_values)
            )

        self._replication_mode = replication_mode

    @property
    def admin_state(self):
        """Gets the admin_state of this LogicalSwitch.  # noqa: E501

        Represents Desired state of the Logical Switch  # noqa: E501

        :return: The admin_state of this LogicalSwitch.  # noqa: E501
        :rtype: str
        """
        return self._admin_state

    @admin_state.setter
    def admin_state(self, admin_state):
        """Sets the admin_state of this LogicalSwitch.

        Represents Desired state of the Logical Switch  # noqa: E501

        :param admin_state: The admin_state of this LogicalSwitch.  # noqa: E501
        :type: str
        """
        if admin_state is None:
            raise ValueError("Invalid value for `admin_state`, must not be `None`")  # noqa: E501
        allowed_values = ["UP", "DOWN"]  # noqa: E501
        if admin_state not in allowed_values:
            raise ValueError(
                "Invalid value for `admin_state` ({0}), must be one of {1}"  # noqa: E501
                .format(admin_state, allowed_values)
            )

        self._admin_state = admin_state

    @property
    def address_bindings(self):
        """Gets the address_bindings of this LogicalSwitch.  # noqa: E501

        Address bindings for the Logical switch  # noqa: E501

        :return: The address_bindings of this LogicalSwitch.  # noqa: E501
        :rtype: list[PacketAddressClassifier]
        """
        return self._address_bindings

    @address_bindings.setter
    def address_bindings(self, address_bindings):
        """Sets the address_bindings of this LogicalSwitch.

        Address bindings for the Logical switch  # noqa: E501

        :param address_bindings: The address_bindings of this LogicalSwitch.  # noqa: E501
        :type: list[PacketAddressClassifier]
        """

        self._address_bindings = address_bindings

    @property
    def transport_zone_id(self):
        """Gets the transport_zone_id of this LogicalSwitch.  # noqa: E501

        Id of the TransportZone to which this LogicalSwitch is associated  # noqa: E501

        :return: The transport_zone_id of this LogicalSwitch.  # noqa: E501
        :rtype: str
        """
        return self._transport_zone_id

    @transport_zone_id.setter
    def transport_zone_id(self, transport_zone_id):
        """Sets the transport_zone_id of this LogicalSwitch.

        Id of the TransportZone to which this LogicalSwitch is associated  # noqa: E501

        :param transport_zone_id: The transport_zone_id of this LogicalSwitch.  # noqa: E501
        :type: str
        """
        if transport_zone_id is None:
            raise ValueError("Invalid value for `transport_zone_id`, must not be `None`")  # noqa: E501

        self._transport_zone_id = transport_zone_id

    @property
    def ip_pool_id(self):
        """Gets the ip_pool_id of this LogicalSwitch.  # noqa: E501

        IP pool id that associated with a LogicalSwitch.  # noqa: E501

        :return: The ip_pool_id of this LogicalSwitch.  # noqa: E501
        :rtype: str
        """
        return self._ip_pool_id

    @ip_pool_id.setter
    def ip_pool_id(self, ip_pool_id):
        """Sets the ip_pool_id of this LogicalSwitch.

        IP pool id that associated with a LogicalSwitch.  # noqa: E501

        :param ip_pool_id: The ip_pool_id of this LogicalSwitch.  # noqa: E501
        :type: str
        """

        self._ip_pool_id = ip_pool_id

    @property
    def vlan(self):
        """Gets the vlan of this LogicalSwitch.  # noqa: E501


        :return: The vlan of this LogicalSwitch.  # noqa: E501
        :rtype: int
        """
        return self._vlan

    @vlan.setter
    def vlan(self, vlan):
        """Sets the vlan of this LogicalSwitch.


        :param vlan: The vlan of this LogicalSwitch.  # noqa: E501
        :type: int
        """

        self._vlan = vlan

    @property
    def switching_profile_ids(self):
        """Gets the switching_profile_ids of this LogicalSwitch.  # noqa: E501


        :return: The switching_profile_ids of this LogicalSwitch.  # noqa: E501
        :rtype: list[SwitchingProfileTypeIdEntry]
        """
        return self._switching_profile_ids

    @switching_profile_ids.setter
    def switching_profile_ids(self, switching_profile_ids):
        """Sets the switching_profile_ids of this LogicalSwitch.


        :param switching_profile_ids: The switching_profile_ids of this LogicalSwitch.  # noqa: E501
        :type: list[SwitchingProfileTypeIdEntry]
        """

        self._switching_profile_ids = switching_profile_ids

    @property
    def mac_pool_id(self):
        """Gets the mac_pool_id of this LogicalSwitch.  # noqa: E501

        Mac pool id that associated with a LogicalSwitch.  # noqa: E501

        :return: The mac_pool_id of this LogicalSwitch.  # noqa: E501
        :rtype: str
        """
        return self._mac_pool_id

    @mac_pool_id.setter
    def mac_pool_id(self, mac_pool_id):
        """Sets the mac_pool_id of this LogicalSwitch.

        Mac pool id that associated with a LogicalSwitch.  # noqa: E501

        :param mac_pool_id: The mac_pool_id of this LogicalSwitch.  # noqa: E501
        :type: str
        """

        self._mac_pool_id = mac_pool_id

    @property
    def vni(self):
        """Gets the vni of this LogicalSwitch.  # noqa: E501

        VNI for this LogicalSwitch.  # noqa: E501

        :return: The vni of this LogicalSwitch.  # noqa: E501
        :rtype: int
        """
        return self._vni

    @vni.setter
    def vni(self, vni):
        """Sets the vni of this LogicalSwitch.

        VNI for this LogicalSwitch.  # noqa: E501

        :param vni: The vni of this LogicalSwitch.  # noqa: E501
        :type: int
        """

        self._vni = vni

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
        if not isinstance(other, LogicalSwitch):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other