ocp_etcd_backup
=========

OCP ETCD Backup role performs a ETCD cluster data backup in an OpenShift 4.2 environment.

Role Variables
--------------

As is generally known, Ansible variables could be defined in different files. The following subsections include default variables and required variables which have to be defined in order to perform an ETCD cluster data backup.

### Defaults Vars

The following default variables are defined at role level and they are saved in *./vars/main.yml* file. It is important to bear in mind that these variables could be redefined by the user when role is triggered.

|Variable|Comment|Type|
|---|---|---|
|backup_dst_file_latest|Destination ETCD backup file path in client instance which triggers Ansible Playbook|String|
|backup_src_path|Temporally path in ETCD master server where the backup is performed|String|

### Required Vars

The following required variables have to be defined when role is triggered.

|Variable|Comment|Type|
|---|---|---|
|backup_dst_path|Destination ETCD backup folder path in client instance which triggers Ansible Playbook|String|


Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: masters
      roles:
         - { role: ocp_etcd_backup, backup_dst_path: /tmp/openshift42_backup }

License
-------

BSD

Author Information
------------------

- Asier Cidon @Red Hat
