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

from msrest.serialization import Model


class TroubleshootingResult(Model):
    """Troubleshooting information gained from specified resource.

    :param start_time: The start time of the troubleshooting.
    :type start_time: datetime
    :param end_time: The end time of the troubleshooting.
    :type end_time: datetime
    :param code: The result code of the troubleshooting.
    :type code: str
    :param results: Information from troubleshooting.
    :type results:
     list[~azure.mgmt.network.v2018_01_01.models.TroubleshootingDetails]
    """

    _attribute_map = {
        'start_time': {'key': 'startTime', 'type': 'iso-8601'},
        'end_time': {'key': 'endTime', 'type': 'iso-8601'},
        'code': {'key': 'code', 'type': 'str'},
        'results': {'key': 'results', 'type': '[TroubleshootingDetails]'},
    }

    def __init__(self, **kwargs):
        super(TroubleshootingResult, self).__init__(**kwargs)
        self.start_time = kwargs.get('start_time', None)
        self.end_time = kwargs.get('end_time', None)
        self.code = kwargs.get('code', None)
        self.results = kwargs.get('results', None)
