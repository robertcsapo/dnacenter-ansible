#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: integration_event
short_description: Manage IntegrationEvent objects of Itsm
description:
- Used to retrieve the list of integration events that failed to create tickets in ITSM.
- >
   Allows retry of multiple failed ITSM event instances. The retry request payload can be given as a list of strings
   ["instance1","instance2","instance3",..] A minimum of one instance Id is mandatory. The list of failed event
   instance Ids can be retrieved using the 'Get Failed ITSM Events' API in the 'instanceId' attribute.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  instance_id:
    description:
    - Instance Id of the failed event as in the Runtime Dashboard.
    type: str
  payload:
    description:
    - An object to send in the Request body.
    - Required for state create.
    type: list

requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.integration_event
# Reference by Internet resource
- name: IntegrationEvent reference
  description: Complete reference of the IntegrationEvent object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: IntegrationEvent reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
"""

EXAMPLES = r"""
- name: get_failed_itsm_events
  cisco.dnac.integration_event:
    state: query  # required
    instance_id: SomeValue  # string
  register: nm_get_failed_itsm_events

- name: retry_integration_events
  cisco.dnac.integration_event:
    state: create  # required
    payload:  # required
    - SomeValue  # string

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
  sample: itsm.get_failed_itsm_events
missing_params:
  description: Provided arguments do not comply with the schema of the DNA Center Python SDK function
  returned: when the function request schema is not satisfied
  type: list
  sample:
"""
