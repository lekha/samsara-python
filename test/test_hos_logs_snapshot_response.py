# coding: utf-8

"""
    Samsara API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 2019-12-12
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import samsara
from samsara.models.hos_logs_snapshot_response import HosLogsSnapshotResponse  # noqa: E501
from samsara.rest import ApiException

class TestHosLogsSnapshotResponse(unittest.TestCase):
    """HosLogsSnapshotResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test HosLogsSnapshotResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = samsara.models.hos_logs_snapshot_response.HosLogsSnapshotResponse()  # noqa: E501
        if include_optional :
            return HosLogsSnapshotResponse(
                data = [
                    samsara.models.hos_log_for_driver.HosLogForDriver(
                        driver = samsara.models.driver_tiny_response.driverTinyResponse(
                            id = '88668', 
                            name = 'Susan Bob', ), 
                        hos_log = samsara.models.hos_log_entry.HosLogEntry(
                            codrivers = [
                                samsara.models.driver_tiny_response.driverTinyResponse(
                                    id = '88668', 
                                    name = 'Susan Bob', )
                                ], 
                            end_time = '2020-01-27T07:06:25Z', 
                            hos_status_type = 'OFF_DUTY', 
                            id = 578.0, 
                            log_recorded_location = samsara.models.location.location(
                                latitude = 122.142, 
                                longitude = -93.343, ), 
                            remark = 'Lunch Break', 
                            start_time = '2020-01-27T07:06:25Z', 
                            vehicle = samsara.models.vehicle_tiny_response.vehicleTinyResponse(
                                id = '123456789', 
                                name = 'Midwest Truck #4', ), ), )
                    ], 
                pagination = samsara.models.pagination_response.paginationResponse(
                    end_cursor = 'MjkY', 
                    has_next_page = True, )
            )
        else :
            return HosLogsSnapshotResponse(
                data = [
                    samsara.models.hos_log_for_driver.HosLogForDriver(
                        driver = samsara.models.driver_tiny_response.driverTinyResponse(
                            id = '88668', 
                            name = 'Susan Bob', ), 
                        hos_log = samsara.models.hos_log_entry.HosLogEntry(
                            codrivers = [
                                samsara.models.driver_tiny_response.driverTinyResponse(
                                    id = '88668', 
                                    name = 'Susan Bob', )
                                ], 
                            end_time = '2020-01-27T07:06:25Z', 
                            hos_status_type = 'OFF_DUTY', 
                            id = 578.0, 
                            log_recorded_location = samsara.models.location.location(
                                latitude = 122.142, 
                                longitude = -93.343, ), 
                            remark = 'Lunch Break', 
                            start_time = '2020-01-27T07:06:25Z', 
                            vehicle = samsara.models.vehicle_tiny_response.vehicleTinyResponse(
                                id = '123456789', 
                                name = 'Midwest Truck #4', ), ), )
                    ],
                pagination = samsara.models.pagination_response.paginationResponse(
                    end_cursor = 'MjkY', 
                    has_next_page = True, ),
        )

    def testHosLogsSnapshotResponse(self):
        """Test HosLogsSnapshotResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
