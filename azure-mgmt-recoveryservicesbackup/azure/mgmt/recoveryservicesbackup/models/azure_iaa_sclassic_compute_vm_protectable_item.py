# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .iaa_svm_protectable_item import IaaSVMProtectableItem


class AzureIaaSClassicComputeVMProtectableItem(IaaSVMProtectableItem):
    """IaaS VM workload-specific backup item representing the Classic Compute VM.

    :param backup_management_type: Type of backup managemenent to backup an
     item.
    :type backup_management_type: str
    :param friendly_name: Friendly name of the backup item.
    :type friendly_name: str
    :param protection_state: State of the back up item. Possible values
     include: 'Invalid', 'NotProtected', 'Protecting', 'Protected'
    :type protection_state: str or :class:`ProtectionStatus
     <azure.mgmt.recoveryservicesbackup.models.ProtectionStatus>`
    :param protectable_item_type: Polymorphic Discriminator
    :type protectable_item_type: str
    :param virtual_machine_id: Fully qualified ARM ID of the virtual machine.
    :type virtual_machine_id: str
    """

    _validation = {
        'protectable_item_type': {'required': True},
    }

    def __init__(self, backup_management_type=None, friendly_name=None, protection_state=None, virtual_machine_id=None):
        super(AzureIaaSClassicComputeVMProtectableItem, self).__init__(backup_management_type=backup_management_type, friendly_name=friendly_name, protection_state=protection_state, virtual_machine_id=virtual_machine_id)
        self.protectable_item_type = 'Microsoft.ClassicCompute/virtualMachines'