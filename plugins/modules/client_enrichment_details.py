#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: client_enrichment_details
short_description: Manage ClientEnrichmentDetails objects of Clients
description:
- >
   Enriches a given network End User context (a network user-id or end user's device Mac Address) with details about
   the user, the devices that the user is connected to and the assurance issues that the user is impacted by.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  headers:
    description:
    - Adds the header parameters.
    type: dict
    required: True

requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.client_enrichment_details
# Reference by Internet resource
- name: ClientEnrichmentDetails reference
  description: Complete reference of the ClientEnrichmentDetails object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: ClientEnrichmentDetails reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
"""

EXAMPLES = r"""
- name: get_client_enrichment_details
  cisco.dnac.client_enrichment_details:
    state: query  # required
    headers:  # required
  register: nm_get_client_enrichment_details

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
  sample: clients.get_client_enrichment_details
missing_params:
  description: Provided arguments do not comply with the schema of the DNA Center Python SDK function
  returned: when the function request schema is not satisfied
  type: list
  sample:
"""
