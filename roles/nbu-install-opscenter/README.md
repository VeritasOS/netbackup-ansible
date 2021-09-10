nbu-install-opscenter
=====================

# Description

A sample Ansible role for installing the NetBackup OpsCenter software on a Windows Server

# Requirements

This role has the following requirements:

  - Ansible 2.9+
  - NetBackup 9.0+
  - Windows Based Server for OpsCenter
  - Credentials to RDP to OpsCenter server 
  - NetBackup server provisioned with the specification detail in the subsquent section of this README.md file. ("See note 2")

# Example Server / Client Specifications

The Ansible role expects the NetBackup servers to have the following baseline specification: 

| # | Server Role | Platform | CPU | RAM | Disk1 | Disk 2 |
| :--- | :--- |:--- |:--- |:--- |:--- |:--- |
| 1 | OpsCenter Server | Windows 2016/2019 | 2 | 4GB | disk1 - 'C:\' - 100GB | - |

# Assumptions

To utilize this role, in-depth knowledge of both Veritas NetBackup and Ansible is required

# How to use the role

This role is part of a collection of roles available in netbackup-ansible project. To use the role:

  1. Clone the repository from GitHub and move to your Ansible Control Host:

           git clone http://www.GitHub/ansible/netbackup-ansible.git

  2. Provision the server(s) as per the specification above

  3. Add local fact file to each server / client - The role utilizes these local facts:

  	  The following facts defined in the local fact file ("C:\.Ansible\netbackup.ps1"):

		OpsCenter

			@{
				domain = @{
				name = '<master_server_hostname>'
				role = 'opscenter'
				}
			}

  4. Update the role variables: 

     OpsCenter

           - default/main.yml

               opscenter_pkg - URL for NetBackup OpsCenter Software (e.g. psCenter_9.1_Win.zip)

           (*) Its recommended to migrate these secrets into an encrypted vars file or to a secrets management platform

  5. Create a playbook and Inventory file

            Examples are provided below in the next section

  6. Provide an inventory and execute the playbook on the master server or Linux server with access HTTPS access to the NetBackup master server:

           "ansible-playbook <playbook_name> -i <inventory_file> "

# Example Playbook / Inventory

A sample playbook and invetory file is provided below:

  1. Example "playbook.yml" file

     OpsCenter:

          - name: Veritas -> Install NetBackup Role
            hosts: master
            gather_facts: no
            roles:
              - nbu-install-opscenter

  2. Example "inventory.yml" file

	        [localhost]
	        locahost ansible_host=localhost

	        [master]
	        <fqdn1> ansible_host=<ip_address>

	        [opscenter]
	        <fqdn1> ansible_host=<ip_address>

# Version

| Directory Name | Version | Description | 
| :--- | :--- |:--- |
| nbu-install-opscenter | 1.0 | Inital release |

# License

The following components are available under the General Public License “GPL” 2.0 and/or the General Public License “GPL 3.0” provided herein. The source code for these GPL component(s) may be obtained at: https://github.com/VeritasOS/netbackup-ansible




