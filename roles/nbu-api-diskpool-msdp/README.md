nbu-api-diskpool-msdp
=====================

# Description

A sample Ansible role for configuring a Disk Pool ("MSDP-Local","MSDP-Cloud-AWS)" on a NetBackup Server

# Requirements

This role has the following requirements:

  - Ansible 2.9+
  - NetBackup 9.0+
  - Linux Based NetBackup Media Server ("See note 1")
  - SSH keyless access between Ansible host and the NetBackup servers
  - API Key for Administrative NetBackup user
  - KMS enabled on NetBackup master server (Can be disabled - Minor updates required)
  - AWS access and secret key information (Cloud Disk Pool Only)

Notes:

  1. All tasks utilize the Ansible URI module - This module is developed for Unix based systems. For Windows based master servers, utilize the WIN_URI module instead. 

# Assumptions

To utilize this role, in-depth knowledge of both Veritas NetBackup and Ansible is required

# How to use the role

This role is part of a collection of roles available in netbackup-ansible project. To use the role:

  1. Clone the repository from GitHub and move to your Ansible Control Host:

           git clone http://www.GitHub/ansible/netbackup-ansible.git

  2. Update the role variables:
  
      Local

           - playbook

               NBU_MASTER_SERVER - Hostname of the NetBackup Master Server
               NBU_API_KEY - User's API key for authenticating with NetBackup API

           - default/main.yml
               
               msdp_local_ss_kmskeygroup - NetBackup KMS Key Group (*)
               msdp_local_ss_username - NetBackup MSDP Storage Server Username (*)
               msdp_local_ss_password - NetBackup MSDP Storage Server Password (*)
               msdp_local_ss_dir_db - Local filesystem path for MSDP Pool Database
               msdp_local_ss_dir_data - Local filesystem path for MSDP Pool Data
               msdp_local_dp_name -  Name of MSDP Pool Storage Server in NetBackup
               msdp_local_dp_io - Maximum streams for Disk Pool
               msdp_local_stu_name - Name of MSDP Pool Storage unit in NetBackup
               msdp_local_stu_io - Maximum streams for Storage Unit

      Cloud-AWS

           - playbook

               NBU_MASTER_SERVER - Hostname of the NetBackup Master Server
               NBU_API_USER_NAME - Username to login to the NetBackup API (*)
               NBU_API_USER_PASSWORD - Password for user to login to the NetBackup API (*)
               aws_access_key: <AWS Access Key> (*)
               aws_access_secret: <AWS Secret Key> (*)
               aws_bucket_name: <S3_bucket_name>
               aws_bucket_volume: <S3 bucket volume name shown in NetBackup>

           - default/main.yml
               
               msdp_cloud_ss_kmskeygroup - NetBackup KMS Key Group (*)
               msdp_cloud_ss_username - NetBackup MSDP Storage Server Username (*)
               msdp_cloud_ss_password - NetBackup MSDP Storage Server Password (*)
               msdp_cloud_dp_name -  Name of MSDP Pool Storage Server in NetBackup
               msdp_cloud_dp_io - Maximum streams for Disk Pool
               msdp_cloud_stu_name - Name of MSDP Pool Storage unit in NetBackup
               msdp_cloud_stu_io - Maximum streams for Storage Unit

           (*) Its recommended to migrate these secrets into an encrypted vars file or to a secrets management platform

  3. Create a playbook and Inventory file

            Examples are provided below in the next section

  4. Provide an inventory and execute the playbook on the master server or Linux server with access HTTPS access to the NetBackup master server:

           "ansible-playbook <playbook_name> -i <inventory_file> "

# Example Playbook / Inventory

A sample playbook and invetory file is provided below:

  1. Example "playbook.yml" file(s)

           - name: Veritas -> Configure MSDP Disk Pool on NetBackup Media Server - Local
             hosts: media
             gather_facts: no
             roles:
               - nbu-api-provider-vmware
             vars:    
                NBU_MASTER_SERVER: <Hostname_master_server>
                NBU_API_KEY: <API-KEY>
             tags:
               - nbu_msdp_create

           - name: Veritas -> Configure MSDP Disk Pool on NetBackup Media Server - Cloud ("AWS")
             hosts: media
             gather_facts: no
             roles:
               - nbu-api-provider-vmware
             vars:    
                NBU_MASTER_SERVER: <Hostname_master_server>
                NBU_API_KEY: <API-KEY>
                nbu_dp_type: "MSDP-Cloud-AWS"
                aws_access_key: '{{ aws_access_key }}'
                aws_access_secret: '{{ aws_secret_key }}'
                aws_bucket_name: <S3_bucket_name>
                aws_bucket_volume: <S3 bucket volume name shown in NetBackup>
             tags:
               - nbu_msdp_create

            Note - You must deploy the MSDP local disk pool before configuring an MSDP Cloud Disk Pool

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
| nbu-api-diskpool-msdp | 1.0 | Inital release |

# License

The following components are available under the General Public License “GPL” 2.0 and/or the General Public License “GPL 3.0” provided herein. The source code for these GPL component(s) may be obtained at: https://github.com/VeritasOS/netbackup-ansible


