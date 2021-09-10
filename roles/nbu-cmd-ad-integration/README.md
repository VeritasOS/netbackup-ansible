nbu-cmd-ad-integration
======================

# Description

A sample Ansible role for integrating NetBackup with Active Directory Domain

# Requirements

This role has the following requirements:

  - Ansible 2.9+
  - NetBackup 9.0+
  - Linux Based Master Server 
  - SSH keyless access between Ansible host and the NetBackup servers
  - Credentials to login to the NetBackup CLI ("Username" + Password) 
  - Active Directory Domain Information and credentials to login to the NetBackup CLI ("Username" + Password)

# Assumptions

To utilize this role, in-depth knowledge of both Veritas NetBackup and Ansible is required

# How to use the role

This role is part of a collection of roles available in netbackup-ansible project. To use the role:

  1. Clone the repository from GitHub and move to your Ansible Control Host:

           git clone http://www.GitHub/ansible/netbackup-ansible.git

  2. Update the role variables: 

           - default/main.yml

               ldap_domain_name - Domain Name
               ldap_server_url - Domain Server URL
               ldap_user_base_dn - Domain User Base DN
               ldap_group_base_dn - Domain Base Group DN
               ldap_ad_user_dn - <Username to query Active Directory domain> (*)
               ldap_ad_user_password - <User Password to query Active Directory domain> (*)

           (*) Its recommended to migrate these secrets into an encrypted vars file or to a secrets management platform

  3. Create a playbook and Inventory file

            Examples are provided below in the next section

  4. Provide an inventory and execute the playbook on the master server or Linux server with access HTTPS access to the NetBackup master server:

           "ansible-playbook <playbook_name> -i <inventory_file> "

# Example Playbook / Inventory

A sample playbook and invetory file is provided below:

  1. Example "playbook.yml" file

           - name: Veritas -> Integrate NetBackup with Active Directory
             hosts: master
             gather_facts: no
             roles:
               - nbu-cmd-ad-integration

  2. Example "inventory.yml" file

	        [localhost]
	        locahost ansible_host=localhost

	        [master]
	        <fqdn1> ansible_host=<ip_address>

# Version

| Directory Name | Version | Description | 
| :--- | :--- |:--- |
| nbu-cmd-ad-integration | 1.0 | Inital release |

# License

The following components are available under the General Public License “GPL” 2.0 and/or the General Public License “GPL 3.0” provided herein. The source code for these GPL component(s) may be obtained at: https://github.com/VeritasOS/netbackup-ansible


