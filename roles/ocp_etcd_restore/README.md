ocp_etcd_restore
=========

OCP ETCD Restore role performs a ETCD cluster data restore in an OpenShift 4.2 environment from a previous backup.

Role Variables
--------------

As is generally known, Ansible variables could be defined in different files. The following subsections include default variables and required variables which have to be defined in order to perform an ETCD cluster data backup.

### Defaults Vars

The following default variables are defined at role level and they are saved in *./vars/main.yml* file. It is important to bear in mind that these variables could be redefined by the user when role is triggered.

|Variable|Comment|Type|
|---|---|---|
|backup_dst_file|Temporally path in ETCD master server where the backup file is copied|String|

### Required Vars

The following required variables have to be defined when role is triggered.

|Variable|Comment|Type|
|---|---|---|
|backup_src_file|ETCD backup file in client instance which triggers Ansible Playbook|String|


Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: masters
      roles:
         - { role: ocp_etcd_restore, backup_dst_path: /backups/etcd/20200109092851-snapshot.db }

License
-------

BSD

Author Information
------------------

- Asier Cidon @Red Hat
