#!/usr/bin/python
# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
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
    - Asier Cidon (@redhat.com)
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

    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        json=dict(type='str', required=True),
    )

    # seed the result dict in the object
    # we primarily care about changed and state
    # change is if this module effectively modified the target
    # state will include any data that you want your module to pass back
    # for consumption, for example, in a subsequent task
    result = dict(
        changed=True,
        message='Test mode ok'
    )

    # the AnsibleModule object will be our abstraction working with Ansible
    # this includes instantiation, a couple of common attr would be the
    # args/params passed to the execution, as well as if the module
    # supports check mode
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    ##
    # ETCD Parser Code
    ##
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

    # if the user is working with this module in only check mode we do not
    # want to make any changes to the environment, just return the current
    # state with no modifications
    if module.check_mode:
        module.exit_json(**result)

    # manipulate or modify the state as needed (this is going to be the
    # part where your module will do what it needs to do)
    
    result['message'] = etcd_members_string

    # during the execution of the module, if there is an exception or a
    # conditional state that effectively causes a failure, run
    # AnsibleModule.fail_json() to pass in the message and the result
    if module.params['json'] == 'Fail':
        module.fail_json(msg='You requested this to fail', **result)

    # in the event of a successful module execution, you will want to
    # simple AnsibleModule.exit_json(), passing the key/value results
    module.exit_json(**result)

def main():

    run_module()

if __name__ == '__main__':

    main()
