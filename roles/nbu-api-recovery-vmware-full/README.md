nbu-api-recovery-vmware-full
============================

# Description

A sample Ansible role for performing a Full VMware VM recovery using NetBackup API

# Requirements

This role has the following requirements:

  - Ansible 2.9+
  - NetBackup 9.0+
  - Linux Based Master Server ("See note 1")
  - SSH keyless access between Ansible host and the NetBackup servers
  - API Key for Administrative NetBackup user

Notes:

  1. All tasks utilize the Ansible URI module - This module is developed for Unix based systems. For Windows based master servers, utilize the WIN_URI module instead. 

# Assumptions

To utilize this role, in-depth knowledge of both Veritas NetBackup and Ansible is required

# How to use the role

This role is part of a collection of roles available in netbackup-ansible project. To use the role:

  1. Clone the repository from GitHub and move to your Ansible Control Host:

           git clone http://www.GitHub/ansible/netbackup-ansible.git

  2. Update the role variables: 

           - playbook

               NBU_MASTER_SERVER - Hostname of the NetBackup Master Server
               NBU_API_KEY - User's API key for authenticating with NetBackup API (*)

           - vars/main.yml

               nbu_vm_hostname: <source_vmname>
               nbu_vm_hostname_recovered: <recovered_vmname>
               nbu_vm_datastore_source: <path for source datastore>
               nbu_vm_datastore_target: <path for target datastore>
               vcenter_hostname: vCenter host to recover to
               vcenter_esxhostname: ESX host to recover to
               vcenter_datacenter: Datacenter to recover to
               vcenter_vmfolder: VM folder to recover to
               vcenter_resourcepool: Resource Pool to recover to
               vcenter_datatore: <source_datastore>
               vcenter_tmpdatastore: <target_datastore>
               vcenter_network: <network>
               nbu_recoveryhost: <media_server>
               nbu_mediaserver: <media_server>


           (*) Its recommended to migrate these secrets into an encrypted vars file or to a secrets management platform

  3. Create a playbook and Inventory file

            Examples are provided below in the next section

  4. Get an API Authorisation Key or utilize an existing API Key for playbook variable

            nbu-api-access-key - This Ansible role will get an API key for a user

  5. Provide an inventory and execute the playbook on the master server or Linux server with access HTTPS access to the NetBackup master server:

           "ansible-playbook <playbook_name> -i <inventory_file> "

# Example Playbook / Inventory

A sample playbook and invetory file is provided below:

  1. Example "playbook.yml" file

           - name: Veritas -> Recover VMware virtual machine
             hosts: master
             gather_facts: no
             roles:
               - nbu-api-recovery-vmware-full
             vars:    
               NBU_API_KEY: <API-KEY>
             tags:
               - nbu_create_pp

  2. Example "inventory.yml" file

	        [localhost]
	        locahost ansible_host=localhost

	        [master]
	        <fqdn1> ansible_host=<ip_address>

# Version

| Directory Name | Version | Description | 
| :--- | :--- |:--- |
| nbu-api-recovery-vmware-full | 1.0 | Inital release |

# License

The following components are available under the General Public License “GPL” 2.0 and/or the General Public License “GPL 3.0” provided herein. The source code for these GPL component(s) may be obtained at: https://github.com/VeritasOS/netbackup-ansible


