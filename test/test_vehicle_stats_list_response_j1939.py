# coding: utf-8

"""
    Samsara API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 2020-06-15
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import samsara
from samsara.models.vehicle_stats_list_response_j1939 import VehicleStatsListResponseJ1939  # noqa: E501
from samsara.rest import ApiException

class TestVehicleStatsListResponseJ1939(unittest.TestCase):
    """VehicleStatsListResponseJ1939 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test VehicleStatsListResponseJ1939
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = samsara.models.vehicle_stats_list_response_j1939.VehicleStatsListResponseJ1939()  # noqa: E501
        if include_optional :
            return VehicleStatsListResponseJ1939(
                check_engine_lights = samsara.models.vehicle_stats_list_response_j1939_check_engine_lights.VehicleStatsListResponse_j1939_checkEngineLights(
                    emissions_is_on = True, 
                    protect_is_on = False, 
                    stop_is_on = False, 
                    warning_is_on = False, ), 
                diagnostic_trouble_codes = [
                    samsara.models.vehicle_stats_list_response_j1939_diagnostic_trouble_codes.VehicleStatsListResponse_j1939_diagnosticTroubleCodes(
                        fmi_description = 'Voltage Below Normal', 
                        fmi_id = 9, 
                        mil_status = 1, 
                        occurrence_count = 1, 
                        source_address_name = 'Engine #1', 
                        spn_description = 'System Diagnostic Code #1', 
                        spn_id = 3031, 
                        tx_id = 0, )
                    ]
            )
        else :
            return VehicleStatsListResponseJ1939(
        )

    def testVehicleStatsListResponseJ1939(self):
        """Test VehicleStatsListResponseJ1939"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
