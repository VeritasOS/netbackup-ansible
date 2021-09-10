#!/usr/bin/python

ANSIBLE_METADATA = {
    'metadata_version': '1.0',
    'status': 'preview',
    'supported_by': 'community'
}

DOCUMENTATION = '''
---
module: nbu_globalattributes.py

short_description: Veritas NetBackup Ansible Module to update Master Server global attributes 

version_added: "2.6"

description:
    - nbu_globalattributes.py is a test module

options:
    jobretry:
            description:
                - Set Job Retry value parameter in minutes e.g. 10
            required: true
    policyupdate:
            description:
                - Set Policy Update parameter in minutes e.g. 10
            required: true
    maxjobs:
            description:
                - Set Global MaxJobsPerClient Parameter e.g. 20
            required: true
    backupattempts:
            description:
                - Set number of attempts Set Global MaxJobsPerClient Parameter e.g. 2 2
            required: true
    compressdb:
            description:
                - Set number of days before compressing DB image e.g. 7
            required: true

author:
    - Veritas Technologies, LLC

license:

## Disclaimer
The information contained in this publication is subject to change without notice. Veritas Corporation makes no warranty of any kind with regard to this manual, including, but not limited to, the implied warranties of merchantability and fitness for a particular purpose. Veritas Corporation shall not be liable for errors contained herein or for incidental or consequential damages in connection with the furnishing, performance, or use of this manual.
The software described in this book is furnished under a license agreement and may be used only in accordance with the terms of the agreement.

## Legal Notice
Last updated: 2021-07-23
Legal Notice
Copyright © 2021 Veritas Technologies LLC. All rights reserved.
Veritas, the Veritas Logo, and NetBackup are trademarks or registered trademarks of Veritas Technologies LLC or its affiliates in the U.S. and other countries. Other names may be trademarks of their respective owners.
This product may contain third-party software for which Veritas is required to provide attribution to the third party (“Third-party Programs”). Some of the Third-party Programs are available under open source or free software licenses. The License Agreement accompanying the Software does not alter any rights or obligations you may have under those open source or free software licenses. Refer to the Third-party Legal Notices document accompanying this Veritas product or available at: https://www.veritas.com/about/legal/license-agreements
The product described in this document is distributed under licenses restricting its use, copying, distribution, and decompilation/reverse engineering. No part of this document may be reproduced in any form by any means without prior written authorization of Veritas Technologies LLC and its licensors, if any.
THE DOCUMENTATION IS PROVIDED "AS IS" AND ALL EXPRESS OR IMPLIED CONDITIONS, REPRESENTATIONS AND WARRANTIES, INCLUDING ANY IMPLIED WARRANTY OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE OR NON-INFRINGEMENT, ARE DISCLAIMED, EXCEPT TO THE EXTENT THAT SUCH DISCLAIMERS ARE HELD TO BE LEGALLY INVALID. VERITAS TECHNOLOGIES LLC SHALL NOT BE LIABLE FOR INCIDENTAL OR CONSEQUENTIAL DAMAGES IN
CONNECTION WITH THE FURNISHING, PERFORMANCE, OR USE OF THIS
DOCUMENTATION. THE INFORMATION CONTAINED IN THIS DOCUMENTATION IS SUBJECT TO CHANGE WITHOUT NOTICE.

The Licensed Software and Documentation are deemed to be commercial computer software as defined in FAR 12.212 and subject to restricted rights as defined in FAR Section 52.227-19 "Commercial Computer Software - Restricted Rights" and DFARS 227.7202, et seq. "Commercial Computer Software and Commercial Computer Software Documentation," as applicable, and any successor regulations, whether delivered by Veritas as on premises or hosted services. Any use, modification, reproduction release, performance, display or disclosure
of the Licensed Software and Documentation by the U.S. Government shall be solely in accordance with the terms of this Agreement.
Veritas Technologies LLC
2625 Augustine Drive
Santa Clara, CA 95054
http://www.veritas.com

## Third-Party Legal Notices
This Veritas product may contain third party software for which Veritas is required to provide attribution (“Third Party Programs”). Some of the Third Party Programs are available under open source or free software licenses. The License Agreement accompanying the Licensed Software does not alter any rights or obligations you may have under those open source or free software licenses. This document or appendix contains proprietary notices for the Third Party Programs and the licenses for the Third Party Programs, where applicable.
The following copyright statements and licenses apply to various open source software components (or portions thereof) that are distributed with the Licensed Software.
The Licensed Software that inclu

'''

EXAMPLES = '''

   - name: Set the default configuration across NetBackup master servers
     nbu_globalattributes:
       maxjobs: 40
       jobretry: 15
       compressdb: 172800
       policyupdate: 5
       backupattempts: 2 2
'''

# Import Ansible Module

from ansible.module_utils.basic import AnsibleModule

# Initialise Module

def run_module():

    # Set options

    module_args = dict(
      jobretry=dict(type='int', required=True),
      policyupdate=dict(type='int', required=True),
      backupattempts=dict(type='str', required=False),
      batries=dict(type='int', required=False),
      bahours=dict(type='int', required=False),
      maxjobs=dict(type='int', required=True),
      compressdb=dict(type='int', required=False)
    )

    # seed the result dict
    result = dict(
        changed=False,
        message='',
        rc=''
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False
    )

    # Track changes to Configuration

    changes_log = list()

    # Get the current configuration

    bpconfig_current = module.run_command(['/usr/openv/netbackup/bin/admincmd/bpconfig'])
    bpconfig_current_raw = bpconfig_current[1]
    bpconfig_current_list = bpconfig_current_raw.split()
    bpconfig_current_jobretry = bpconfig_current_list[1]
    bpconfig_current_policyupdate = bpconfig_current_list[15]
    bpconfig_current_batries = bpconfig_current_list[4]
    bpconfig_current_bahours = bpconfig_current_list[2]
    bpconfig_current_maxjobs = bpconfig_current_list[3]
    bpconfig_current_compressdb = bpconfig_current_list[7]

    # Job Retry

    if not bool(module.params['jobretry']):                                                     # Check input value provided
      module.fail_json(msg="ERROR - No value was provided (Job Retry)",**result)

    if not 1 <= module.params['jobretry'] <= 60:                                                # Check number is valid
      module.fail_json(msg="ERROR - Value provided is not valid (Job Retry)",**result)

    if module.params['jobretry'] == int(bpconfig_current_jobretry):                             # Matches current, no changes required
      result['message_jobretry'] = "Changed: No"

    if module.params['jobretry'] != int(bpconfig_current_jobretry):                             # New value, update configuration
      cmdtorun = '/usr/openv/netbackup/bin/admincmd/bpconfig ' + '-wi ' + str(module.params['jobretry'])
      module.run_command(cmdtorun)
      result['message_jobretry'] = "Changed: Yes"
      changes_log.append("JobsRetry")                                                          # Increment change log

    # Policy Update

    if not bool(module.params['policyupdate']):                                                # Check input value provided
      module.fail_json(msg="ERROR - No value was provided (Policy Update)",**result)

    if not 1 <= module.params['policyupdate'] <= 60:                                           # Check number is valid
      module.fail_json(msg="ERROR - Value provided is not valid (Policy Update)",**result)

    if module.params['policyupdate'] == int(bpconfig_current_policyupdate):                    # Matches current, no changes required
      result['message_policyupdate'] = "Changed: No"

    if module.params['policyupdate'] != int(bpconfig_current_policyupdate):                    # New value, update configuration
      cmdtorun = '/usr/openv/netbackup/bin/admincmd/bpconfig ' + '-pui ' + str(module.params['policyupdate'])
      module.run_command(cmdtorun)
      result['message_policyupdate'] = "Changed: Yes"
      changes_log.append("PolicyUpdate")                                                       # Increment change log

    # Max Jobs per Client

    if not bool(module.params['maxjobs']):                                                     # Check input value provided
      module.fail_json(msg="ERROR - No value was provided (Max Jobs Per Client)",**result)

    if not 1 <= module.params['maxjobs'] <= 99:                                                # Check number is valid (1-99)
      module.fail_json(msg="ERROR - Value provided is not valid (Max Jobs Per Client)",**result)

    if module.params['maxjobs'] == int(bpconfig_current_maxjobs):                              # Matches current, no changes required
      result['message_maxjobs'] = "Changed: No"

    if module.params['maxjobs'] != int(bpconfig_current_maxjobs):                              # New value, update configuration
      cmdtorun = '/usr/openv/netbackup/bin/admincmd/bpconfig ' + '-mj ' + str(module.params['maxjobs'])
      module.run_command(cmdtorun)
      result['message_maxjobs'] = "Changed: Yes"
      result['message_maxjobs_old'] = bpconfig_current_maxjobs
      result['message_maxjobs_new'] = module.params['maxjobs']
      changes_log.append("MaxJobsPerClient")                                                   # Increment change log

    # Compress Image DB

    if not bool(module.params['compressdb']):                                                  # Check input value provided
      module.fail_json(msg="ERROR - No value was provided (Compress Image DB)",**result)

    if not 0 <= module.params['compressdb'] <= 2147472000:                                     # Check number is valid (1-99)
      module.fail_json(msg="ERROR - Value provided is not valid (Compress Image DB)",**result)

    if module.params['compressdb'] == int(bpconfig_current_compressdb):                        # Matches current, no changes required
      result['message_compressdb'] = "Changed: No"

    if module.params['compressdb'] != int(bpconfig_current_compressdb):                        # New value, update configuration
      cmdtorun = '/usr/openv/netbackup/bin/admincmd/bpconfig ' + '-cd ' + str(module.params['compressdb'])
      module.run_command(cmdtorun)
      result['message_maxjobs'] = "Changed: Yes"
      changes_log.append("CompressImageDBt")

    # Backup Retries

    backupattempt_list = module.params['backupattempts'].split()
    backupattempt_tries = backupattempt_list[0]
    backupattempt_hours = backupattempt_list[1]
    result['message_maxjobs1'] = backupattempt_list[0]
    result['message_maxjobs2'] = backupattempt_list[1]

    if not bool(module.params['backupattempts']):                                              # Check input value provided
      module.fail_json(msg="ERROR - No value was provided (Backup Attempts)",**result)

    if not 1 <= int(backupattempt_tries) <= 1000:                                              # Check number is valid
      module.fail_json(msg="ERROR - Value provided is not valid (Backup Attempt - Tries)",**result)

    if not 1 <= int(backupattempt_hours) <= 24:                                                # Check number is valid
      module.fail_json(msg="ERROR - Value provided is not valid (Backup Attempt - Hours)",**result)

    if int(backupattempt_tries) == int(bpconfig_current_batries):                              # Matches current, no changes required
      result['message_bacckupattempts_tries'] = "Changed: No"

    if int(backupattempt_hours) == int(bpconfig_current_bahours):                              # Matches current, no changes required
      result['message_bacckupattempts_tries'] = "Changed: No"

    if int(backupattempt_tries) != int(bpconfig_current_batries):                              # New value, update configuration
      cmdtorun = '/usr/openv/netbackup/bin/admincmd/bpconfig ' + '-tries ' + str(backupattempt_tries)
      module.run_command(cmdtorun)
      result['message_backupattempts_tries'] = "Changed: Yes"
      changes_log.append("BackupAttempts_Tries")

    if int(backupattempt_hours) != int(bpconfig_current_bahours):                              # New value, update configuration
      cmdtorun = '/usr/openv/netbackup/bin/admincmd/bpconfig ' + '-period ' + str(backupattempt_hours)
      module.run_command(cmdtorun)
      result['message_backupattempts_hours'] = "Changed: Yes"
      changes_log.append("BackupAttempts_Hours")

    # Provide result to Ansible

    if len(changes_log) == 0:
      result['message'] = "No changes detected"

      result['changed'] = False
      result['rc'] = 0
      module.exit_json(**result)

    if len(changes_log) != 0:
      result['message'] = "Configuration has Changed"
      result['changed'] = True
      result['rc'] = 0
      module.exit_json(**result)

# Run Module

def main():
    run_module()

if __name__ == '__main__':
    main()
