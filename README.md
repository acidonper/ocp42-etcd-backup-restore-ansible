# Backup and restore ETCD Cluster Data using Ansible (OpenShift 4.2)

ETCD is the key-value store for OpenShift Container Platform, which persists the state of all resource objects.

This repository implements a set of Ansible Playbooks in order to perform a backup and restore of the ETCD cluster data of an OpenShift Operational Cluster verison 4.2. Please, carefully review the contents in the following subsections in order to understand and be able to execute backup and restore procedures.

## ETCD cluster data Backup

You can perform the etcd data backup process on any master host that has connectivity to the etcd cluster, where the proper certificates are provided.

On the other hand, You should only save a snapshot from a single master host. You do not need a snapshot from each master host in the cluster.

### Prerequisites

-   Firstly, It is necessary to have an operational ETCD cluster with a quorum required and sanity checks passed.
-   SSH access to a master host.

### Procedure Overview

**Automatic Process (Ansible Playbook -> ocp42-backup-etcd.yml)**

-   Access a master host as the root user.
-   Run the etcd-snapshot-backup.sh script and pass in the location to save the etcd snapshot to.

## ETCD cluster data Restore

It is important to bear in mind that this solution handles situations where you want to restore your cluster to a previous state, for example, if an administrator deletes something critical. As long as you have taken an etcd backup, you can follow this procedure to restore your cluster to a previous state.

### Prerequisites

-   Firstly, It is necessary to have an operational ETCD cluster with a quorum required and sanity checks passed.
-   Access to the cluster as a user with the cluster-admin role
-   SSH access to master hosts
-   A backed-up etcd snapshot

**IMPORTANT**: You must use the same etcd snapshot file on all master hosts in the cluster.

### Procedure Overview

**\*Automatic Process (Ansible Playbook -> ocp42-restore-etcd.yml )**

-   Prepare each master host in your cluster to be restored.
-   Run the restore script on all of your master hosts.

**Manual Process(\*)**

Please follow **verify** subsection/s included in OpenShift 4.2 Official Documentation (https://docs.openshift.com/container-platform/4.2/backup_and_restore/disaster_recovery/scenario-2-restoring-cluster-state.html#dr-restoring-cluster-state)

## Example Automation Process Execution

### Backup

-   Perform a backup locating "`<date>`-snapshot.db" file in "/tmp/openshift42_backups" folder

```
$ ansible-playbook -i inventory ocp42-backup-etcd.yml --extra-vars="backup_dst_path=/tmp/openshift42_backup"
```

### Restore

-   Perform a ETCD recovery from a backup file "/tmp/openshift42_backup/20200109092851-snapshot.db"

```
$ ansible-playbook -i inventory ocp42-restore-etcd.yml --extra-vars="backup_src_file=/tmp/openshift42_backup/20200109092851-snapshot.db"
```

## Official Sources

### Backup

-   https://docs.openshift.com/container-platform/4.2/backup_and_restore/backing-up-etcd.html

### Restore

-   https://docs.openshift.com/container-platform/4.2/backup_and_restore/disaster_recovery/scenario-2-restoring-cluster-state.html#dr-restoring-cluster-state

## License

BSD

## Author Information

-   Asier Cidon @Red Hat
