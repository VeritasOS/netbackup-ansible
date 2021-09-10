nbu-api-rbac-member
===================

# Description

A sample Ansible role for adding an Active Directory group to a specific RBAC role. This sample role add an AD group to the previously create RBAC roles:

  1. Admin - Full administrative access
  2. Non-Admin - Restricted access for Non-Administrators

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
               nbu_rbac_role - Either "Admin" or "Non-Admin"
               nbu_member_type - Should be set to "AD_GROUP"

           - defaults/role1_admin.yml

               nbu_group_name - Name of AD Group for Admins
               nbu_group_type - "ldap:<domain_name>"
               nbu_group_domain - <domain_name>

           - defaults/role2_nonadmin.yml

               nbu_group_name - Name of AD Group for Non-Admins
               nbu_group_type - "ldap:<domain_name>"
               nbu_group_domain - <domain_name>

           (*) Its recommended to migrate these secrets into an encrypted vars file or to a secrets management platform

  3. Create a playbook and Inventory file

            Examples are provided below in the next section

  4. Get an API Authorisation Key or utilize an existing API Key for playbook variable

            nbu-api-access-key - This Ansible role will get an API key for a user

  4. Provide an inventory and execute the playbook on the master server or Linux server with access HTTPS access to the NetBackup master server:

           "ansible-playbook <playbook_name> -i <inventory_file> "

# Example Playbook / Inventory

A sample playbook and invetory file is provided below:

  1. Example "playbook.yml" file

        - name: Veritas -> Add user or group to NetBackup Role(s)
          hosts: master
          gather_facts: yes
          roles:
            - { role: nbu-api-rbac-member, 
                nbu_rbac_role: Admins, 
                nbu_rbac_role_ui: 'Admins',
                nbu_member_type: AD_Group }

            - { role: nbu-api-rbac-member, 
                nbu_rbac_role: Non-Admins,
                nbu_rbac_role_ui: 'Non-Admins',
                nbu_member_type: AD_Group }
           vars:
               NBU_MASTER_SERVER - Hostname of master server
               NBU_API_KEY: <API-KEY>

  2. Example "inventory.yml" file

	        [localhost]
	        locahost ansible_host=localhost

	        [master]
	        <fqdn1> ansible_host=<ip_address>

# Version

| Directory Name | Version | Description | 
| :--- | :--- |:--- |
| nbu-api-rbac-member | 1.0 | Inital release |

# License

The following components are available under the General Public License “GPL” 2.0 and/or the General Public License “GPL 3.0” provided herein. The source code for these GPL component(s) may be obtained at: https://github.com/VeritasOS/netbackup-ansible


