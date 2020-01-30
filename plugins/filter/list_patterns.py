# Copyright (c) 2020 Ansible Project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)


from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


ANSIBLE_METADATA = {
    'metadata_version': '1.0',
    'status': ['preview'],
    'supported_by': 'community'
}


from ansible.errors import AnsibleFilterError
from ansible.module_utils.six.moves.urllib.parse import urlsplit
from ansible.utils import helpers


def list_patterns(value, query):

    if query == '':
        raise AnsibleFilterError('No query included')
    else:
        if isinstance(value, list):
            matching = [s for s in value if query in s]
            return matching
        else:
            raise AnsibleFilterError('Object is not a List')

class FilterModule(object):
    ''' Find string patterns in a string list'''

    def filters(self):
        return {
            'list_patterns': list_patterns
        }