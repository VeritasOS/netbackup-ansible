nbu-install-linux
=================

# Description

A sample Ansible role for installing the NetBackup software on a Red Hat server and configuring a NetBackup role. This Ansible role has the ability to configure the following types of NetBckup servers:

  1. Master
  2. Media
  3. Client ("Linux")

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
| 1 | Master Server | RedHat 8.4 | 4GB | disk1 - '/usr/openv' - 50GB | disk2 - /usr/openv/netbackup/db - 100GB |
| 2 | Media Server | RedHat 8.4| 2 | 16GB | disk1 - '/usr/openv' - 50GB | disk2 - /msdp - 100GB |
| 3 | Client ("Linux") | RedHat 8.4| 1 | 1GB | disk1 - '/usr/openv' - 5GB | - |

*Note - The disks must be formatted with a filesystem and mounted accordingly*

# Assumptions

To utilize this role, in-depth knowledge of both Veritas NetBackup and Ansible is required

# How to use the role

This role is part of a collection of roles available in netbackup-ansible project. To use the role:

  1. Clone the repository from GitHub and move to your Ansible Control Host:

           git clone http://www.GitHub/ansible/netbackup-ansible.git

  2. Provision the server(s) as per the specification above

  3. Add local fact file to each server / client - The role utilizes these local facts:

  	 The following facts defined in the local fact file ("/etc/ansible/facts.d/netbackup.fact"):

		Master Server

			[domain]
			name=<master_server_hostname>
			role=master
			truster_master=<remote_master_server_hostname or none>

		Media Server

			[domain]
			name=<master_server_hostname>
			role=media

		Client - Linux

			[domain]
			name=<master_server_hostname>
			role=client_linux

  4. Update the role variables: 

     Master Server:

           - playbook

               nbu_admin_User - Username to login to the NetBackup API (*)
               nbu_admin_password - Password for user to login to the NetBackup API (*)
               nbu_services_user - The user for the NetBackup services to run under
               nbu_services_group - The local group that the nbu_services_user is a member of
               nbu_webservices_user - The local userr account to run the NetBackup web service under.
               nbu_webservices_group - The local group that the nbu_webservices_user is a member of
               nbu_license_key - NetBackup license key to use (""Master and Media Servers Only"") (*)

           - default/main.yml

               nbu_server_software_file: URL for NetBackup server software (e.g. NetBackup_9.1_LinuxR_x86_64.tar.gz) 
               nbu_server_software_dir: /tmp/NetBackup_9.1_LinuxR_x86_64
               nbu_nbpck: URL for NetBackup RPM files - VRTSnbpck.rpm
               nbu_nbpbx: URL for NetBackup RPM files - VRTSpbx.rpm
               nbu_nbclt: URL for NetBackup RPM files - VRTSnbclt.rpm
               nbu_pddea: URL for NetBackup RPM files - VRTSpddea.rpm
               nbu_pddes: URL for NetBackup RPM files - VRTSpddes.rpm
               nbu_pddei: URL for NetBackup RPM files - VRTSpddei.rpm
               nbu_nbcfg: URL for NetBackup RPM files - VRTSnbcfg.rpm
               nbu_netbp: URL for NetBackup RPM files - VRTSnetbp.rpm

     Media Server:

           - playbook

               nbu_admin_User - Username to login to the NetBackup API (*)
               nbu_admin_password - Password for user to login to the NetBackup API (*)
               nbu_role - The NetBackup role to install on Server or Client ("Master Server", "Media Server" or "Client_Linux")
               nbu_license_key - NetBackup license key to use (""Master and Media Servers Only"") (*)

           - default/main.yml

               nbu_nbpck: URL for NetBackup RPM files - VRTSnbpck.rpm
               nbu_nbpbx: URL for NetBackup RPM files - VRTSpbx.rpm
               nbu_nbclt: URL for NetBackup RPM files - VRTSnbclt.rpm
               nbu_pddea: URL for NetBackup RPM files - VRTSpddea.rpm
               nbu_pddes: URL for NetBackup RPM files - VRTSpddes.rpm
               nbu_pddei: URL for NetBackup RPM files - VRTSpddei.rpm
               nbu_nbcfg: URL for NetBackup RPM files - VRTSnbcfg.rpm
               nbu_netbp: URL for NetBackup RPM files - VRTSnetbp.rpm

     Client - Linux:
    
           - playbook

               nbu_admin_User - Username to login to the NetBackup API (*)
               nbu_admin_password - Password for user to login to the NetBackup API (*)
               nbu_role - The NetBackup role to install on Server or Client ("Master Server", "Media Server" or "Client_Linux")

           - default/main.yml

               nbu_nbpck: URL for NetBackup RPM files - VRTSnbpck.rpm
               nbu_nbpbx: URL for NetBackup RPM files - VRTSpbx.rpm
               nbu_nbclt: URL for NetBackup RPM files - VRTSnbclt.rpm
               nbu_pddea: URL for NetBackup RPM files - VRTSpddea.rpm
               nbu_pddes: URL for NetBackup RPM files - VRTSpddes.rpm
               nbu_pddei: URL for NetBackup RPM files - VRTSpddei.rpm
               nbu_nbcfg: URL for NetBackup RPM files - VRTSnbcfg.rpm
               nbu_netbp: URL for NetBackup RPM files - VRTSnetbp.rpm

           (*) Its recommended to migrate these secrets into an encrypted vars file or to a secrets management platform

  5. Create a playbook and Inventory file

            Examples are provided below in the next section

  6. Provide an inventory and execute the playbook on the master server or Linux server with access HTTPS access to the NetBackup master server:

           "ansible-playbook <playbook_name> -i <inventory_file> "

# Example Playbook / Inventory

A sample playbook and invetory file is provided below:

  1. Example "playbook.yml" file

     Master Server:

           - name: Veritas -> Install NetBackup Role
             hosts: master
             gather_facts: no
             roles:
               - nbu-install-linux
             vars:    
               nbu_admin_user: admin
               nbu_admin_password: P@ssw0rd
               nbu_services_user - The user for the NetBackup services to run under
               nbu_services_group - The local group that the nbu_services_user is a member of
               nbu_webservices_user - The local userr account to run the NetBackup web service under.
               nbu_webservices_group - The local group that the nbu_webservices_user is a member of
               nbu_license_key - NetBackup license key to use (""Master and Media Servers Only"") (*)

     Media Server:

           - name: Veritas -> Install NetBackup Role
             hosts: media
             gather_facts: no
             roles:
               - nbu-install-linux
             vars:    
               nbu_admin_User - Username to login to the NetBackup API (*)
               nbu_admin_password - Password for user to login to the NetBackup API (*)
               nbu_license_key - NetBackup license key to use (""Master and Media Servers Only"") (*)

     Client - Linux:

           - name: Veritas -> Install NetBackup Role
             hosts: client_linux
             gather_facts: no
             roles:
               - nbu-install-linux
             vars:    
               nbu_admin_User - Username to login to the NetBackup API (*)
               nbu_admin_password - Password for user to login to the NetBackup API (*)

  2. Example "inventory.yml" file

	        [localhost]
	        locahost ansible_host=localhost

	        [master]
	        <fqdn1> ansible_host=<ip_address>

	        [media]
	        <fqdn1> ansible_host=<ip_address>

	        [client_linux]
	        <fqdn1> ansible_host=<ip_address>

# Version

| Directory Name | Version | Description | 
| :--- | :--- |:--- |
| nbu-install-linux | 1.0 | Inital release |

# License

The following components are available under the General Public License “GPL” 2.0 and/or the General Public License “GPL 3.0” provided herein. The source code for these GPL component(s) may be obtained at: https://github.com/VeritasOS/netbackup-ansible




