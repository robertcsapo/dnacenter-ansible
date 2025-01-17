#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: device_detail
short_description: Manage DeviceDetail objects of Devices
description:
- Returns detailed Network Device information retrieved by Mac Address, Device Name or UUID for any given point of time.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  identifier:
    description:
    - One of keywords macAddress or uuid or nwDeviceName.
    type: str
    required: True
  search_by:
    description:
    - MAC Address or Device Name value or UUID of the network device.
    type: str
    required: True
  timestamp:
    description:
    - Epoch time(in milliseconds) when the device data is required.
    type: int

requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.device_detail
# Reference by Internet resource
- name: DeviceDetail reference
  description: Complete reference of the DeviceDetail object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: DeviceDetail reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
"""

EXAMPLES = r"""
- name: get_device_detail
  cisco.dnac.device_detail:
    state: query  # required
    identifier: SomeValue  # string, required
    search_by: SomeValue  # string, required
    timestamp: 1  #  integer
  register: nm_get_device_detail

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
  sample: devices.get_device_detail
missing_params:
  description: Provided arguments do not comply with the schema of the DNA Center Python SDK function
  returned: when the function request schema is not satisfied
  type: list
  sample:
"""
