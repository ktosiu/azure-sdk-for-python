# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ManagementPolicyRule(Model):
    """An object that wraps the Lifecycle rule. Each rule is uniquely defined by
    name.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :param enabled: Rule is enabled if set to true.
    :type enabled: bool
    :param name: Required. A rule name can contain any combination of alpha
     numeric characters. Rule name is case-sensitive. It must be unique within
     a policy.
    :type name: str
    :ivar type: Required. The valid value is Lifecycle. Default value:
     "Lifecycle" .
    :vartype type: str
    :param definition: Required. An object that defines the Lifecycle rule.
    :type definition:
     ~azure.mgmt.storage.v2018_11_01.models.ManagementPolicyDefinition
    """

    _validation = {
        'name': {'required': True},
        'type': {'required': True, 'constant': True},
        'definition': {'required': True},
    }

    _attribute_map = {
        'enabled': {'key': 'enabled', 'type': 'bool'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'definition': {'key': 'definition', 'type': 'ManagementPolicyDefinition'},
    }

    type = "Lifecycle"

    def __init__(self, *, name: str, definition, enabled: bool=None, **kwargs) -> None:
        super(ManagementPolicyRule, self).__init__(**kwargs)
        self.enabled = enabled
        self.name = name
        self.definition = definition
