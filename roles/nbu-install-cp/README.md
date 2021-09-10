nbu-install-cp
==============

# Description

A sample Ansible role for installing the NetBackup CloudPoint software on a Red Hat server and configuring the CloudPoint role.

# Requirements

This role has the following requirements:

  - Ansible 2.9+
  - NetBackup 9.0+
  - Linux Based Master Server ("See note 1")
  - SSH keyless access between Ansible host and the NetBackup servers
  - API Key for Administrative NetBackup user
  - NetBackup servers provisioned with the specification detail in the subsquent section of this README.md file. ("See note 2")

Notes:

  1. All tasks utilize the Ansible URI module - This module is developed for Unix based systems. For Windows based master servers, utilize the WIN_URI module instead. 
  2. The media server and Client ("Linux") deployment requires the NetBackup master server to be operational

# Example Server / Client Specifications

The Ansible role expects the NetBackup servers to have the following baseline specification: 

| # | Server Role | Platform | CPU | RAM | Disk1 | Disk 2 |
| :--- | :--- |:--- |:--- |:--- |:--- |:--- |
| 1 | CloudPoint | RedHat 8.4 | 1 | 8GB | disk1 - '/cloudpoint' - 50GB | - |

*Note - The disks must be formatted with a filesystem and mounted accordingly*

# Assumptions

To utilize this role, in-depth knowledge of both Veritas NetBackup and Ansible is required

# How to use the role

This role is part of a collection of roles available in netbackup-ansible project. To use the role:

  1. Clone the repository from GitHub and move to your Ansible Control Host:

           git clone http://www.GitHub/ansible/netbackup-ansible.git

  2. Provision the server(s) as per the specification above

  3. Add local fact file to CloudPoint server  - The role utilizes these local facts:

  	 The following facts defined in the local fact file ("/etc/ansible/facts.d/netbackup.fact"):

		CloudPoint

			[domain]
			name=<master_server_hostname>
			role=cloudpoint
			truster_master=<remote_master_server_hostname or none>

  4. Update the role variables: 

     Master Server:

           - playbook
               
               cp_admin_user - Username for CloudPoint Admin (*)
               cp_admin_password - Password for CloudPoint Admin (*)

           - default/main.yml

               nbu_cp: URL for NetBackup CloudPoint software (e.g. VRTScloudpoint-podman-9.0.1.0.9336.tar.gz) 

           (*) Its recommended to migrate these secrets into an encrypted vars file or to a secrets management platform

  5. Create a playbook and Inventory file

            Examples are provided below in the next section

  6. Provide an inventory and execute the playbook on CloudPoint server:

           "ansible-playbook <playbook_name> -i <inventory_file> "

# Example Playbook / Inventory

A sample playbook and invetory file is provided below:

  1. Example "playbook.yml" file

     CloudPoint:

           - name: Veritas -> Install NetBackup Role
             hosts: cloudpoint
             gather_facts: no
             roles:
               - nbu-install-cloudpoint
             vars:    
               cp_admin_user - Username for CloudPoint Admin (*)
               cp_admin_password - Password for CloudPoint Admin (*)

  2. Example "inventory.yml" file

	        [localhost]
	        locahost ansible_host=localhost

	        [master]
	        <fqdn1> ansible_host=<ip_address>

	        [cloudpoint]
	        <fqdn1> ansible_host=<ip_address>

# Version

| Directory Name | Version | Description | 
| :--- | :--- |:--- |
| nbu-install-cp | 1.0 | Inital release |

# License

The following components are available under the General Public License “GPL” 2.0 and/or the General Public License “GPL 3.0” provided herein. The source code for these GPL component(s) may be obtained at: https://github.com/VeritasOS/netbackup-ansible




