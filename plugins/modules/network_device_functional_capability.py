#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: network_device_functional_capability
short_description: Manage NetworkDeviceFunctionalCapability objects of Devices
description:
- Returns the functional-capability for given devices.
- Returns functional capability with given Id.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  device_id:
    description:
    - >
       Accepts comma separated deviceid's and return list of functional-capabilities for the given id's. If
       invalid or not-found id's are provided, null entry will be returned in the list.
    type: str
    required: True
  function_name:
    description:
    - FunctionName query parameter.
    type: str
  id:
    description:
    - Functional Capability UUID.
    type: str
    required: True

requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.network_device_functional_capability
# Reference by Internet resource
- name: NetworkDeviceFunctionalCapability reference
  description: Complete reference of the NetworkDeviceFunctionalCapability object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: NetworkDeviceFunctionalCapability reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
"""

EXAMPLES = r"""
- name: get_functional_capability_for_devices
  cisco.dnac.network_device_functional_capability:
    state: query  # required
    device_id: SomeValue  # string, required
    function_name: SomeValue  # string
  register: nm_get_functional_capability_for_devices

- name: get_functional_capability_by_id
  cisco.dnac.network_device_functional_capability:
    state: query  # required
    id: SomeValue  # string, required
  register: nm_get_functional_capability_by_id

"""

RETURN = r"""
dnac_response:
  description: A dictionary with the response returned by the DNA Center Python SDK
  returned: always
  type: dict
  sample: {"response": 29, "version": "1.0"}
sdk_function:
  description: The DNA Center SDK function used to execute the task
  returned: always
  type: str
  sample: devices.get_functional_capability_by_id
missing_params:
  description: Provided arguments do not comply with the schema of the DNA Center Python SDK function
  returned: when the function request schema is not satisfied
  type: list
  sample:
"""
