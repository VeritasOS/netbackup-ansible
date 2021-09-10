nbu-api-diskpool-adv
====================

# Description

A sample Ansible role for configuring a Disk Pool ("AdvancedDisk") on a NetBackup server

# Requirements

This role has the following requirements:

  - Ansible 2.9+
  - NetBackup 9.0+
  - Linux Based NetBackup Media Server ("See note 1")
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

           - default/main.yml

               adv_local_dp_name -  Name of AdvancedDisk Pool Storage Server in NetBackup
               adv_local_dp_path - Local filesystem path for AdvancedDisk Pool Pool
               adv_local_dp_io - Maximum streams for Disk Pool
               adv_local_stu_name - Name of AdvancedDisk Pool Storage unit in NetBackup
               adv_local_stu_io - Maximum streams for Storage Unit

           (*) Its recommended to migrate these secrets into an encrypted vars file or to a secrets management platform

  3. Create a playbook and Inventory file

            Examples are provided below in the next section

  4. Provide an inventory and execute the playbook on the master server or Linux server with access HTTPS access to the NetBackup master server:

           "ansible-playbook <playbook_name> -i <inventory_file> "

# Example Playbook / Inventory

A sample playbook and invetory file is provided below:

  1. Example "playbook.yml" file

           - name: Veritas -> Configure AdvancedDisk Disk Pool on NetBackup Media Server - Local
             hosts: media
             gather_facts: no
             roles:
               - nbu-api-provider-vmware
             vars:    
               NBU_MASTER_SERVER: <Hostname_or_IP_Address> 
               NBU_API_KEY: <API-KEY>
             tags:
               - nbu_adv_create

  2. Example "inventory.yml" file

	        [localhost]
	        locahost ansible_host=localhost

	        [master]
	        <fqdn1> ansible_host=<ip_address>

	        [media]
	        <fqdn1> ansible_host=<ip_address>

# Version

| Directory Name | Version | Description | 
| :--- | :--- |:--- |
| nbu-api-diskpool-adv | 1.0 | Inital release |

# License

The following components are available under the General Public License “GPL” 2.0 and/or the General Public License “GPL 3.0” provided herein. The source code for these GPL component(s) may be obtained at: https://github.com/VeritasOS/netbackup-ansible


