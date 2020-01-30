#!/usr/bin/python
# Copyright: (c) 2020, Asier Cidon <acidonpe@redhat.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

ANSIBLE_METADATA = {
'metadata_version': '1.0',
'status': ['preview'],
'supported_by': 'community'
}

DOCUMENTATION = '''
---
module: etcd_members_parser
short_description: "This procedure converts a list of etcd members in JSON format to a list of etcd members in the format of <name>=<url>"
version_added: "1.0"
description:
    - "This module parsers 'etcdctl member list -w json' command output in order to generate a list of members in a specific format which is used by 'Restoring to a previous cluster state' procedure"
options:
    json:
        description:
            - List of etcd members in JSON format
        required: true
author:
    - Asier Cidon (acidonpe@redhat.com)
'''

EXAMPLES = '''
# Parse JSON
- name: Test with a message
  etcd_members_parser:
    json:   
'''

RETURN = '''
message:
    description: List of etcd members in the format of <name>=<url>
    type: str
    returned: always
'''

from ansible.module_utils.basic import AnsibleModule
import json

def run_module():

    module_args = dict(
        json=dict(type='str', required=True),
    )

    result = dict(
        changed=True,
        message='Test mode ok'
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    json_src = module.params['json']
    json_src = json_src.replace("\'", "\"")
    etcd_members_dict=json.loads(json_src)
    etcd_members_list=[]

    for member in etcd_members_dict['members']:

        # Security checks
        assert (member['name'] != ""), "Member Name is empty"
        assert (len(member['peerURLs']) > 0), "Member URL Array is empty"
        assert (member['peerURLs'][0] != ""), "Member URL variable is empty"

        # Generate member string
        member_string=member['name'] + "=" + member['peerURLs'][0]
        etcd_members_list.append(member_string)

    etcd_members_string=','.join(etcd_members_list)

    if module.check_mode:
        module.exit_json(**result)
    
    result['message'] = etcd_members_string

    if module.params['json'] == 'Fail':
        module.fail_json(msg='You requested this to fail', **result)

    module.exit_json(**result)

def main():

    run_module()

if __name__ == '__main__':

    main()
