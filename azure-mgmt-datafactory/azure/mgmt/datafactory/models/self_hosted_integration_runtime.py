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

from .integration_runtime import IntegrationRuntime


class SelfHostedIntegrationRuntime(IntegrationRuntime):
    """Self-hosted integration runtime.

    :param description: Integration runtime description.
    :type description: str
    :param type: Polymorphic Discriminator
    :type type: str
    """

    _validation = {
        'type': {'required': True},
    }

    def __init__(self, description=None):
        super(SelfHostedIntegrationRuntime, self).__init__(description=description)
        self.type = 'SelfHosted'