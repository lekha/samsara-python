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
from samsara.models.vehicle_stats_fault_codes import VehicleStatsFaultCodes  # noqa: E501
from samsara.rest import ApiException

class TestVehicleStatsFaultCodes(unittest.TestCase):
    """VehicleStatsFaultCodes unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test VehicleStatsFaultCodes
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = samsara.models.vehicle_stats_fault_codes.VehicleStatsFaultCodes()  # noqa: E501
        if include_optional :
            return VehicleStatsFaultCodes(
                can_bus_type = 'CANBUS_J1939_500', 
                j1939 = samsara.models.vehicle_stats_fault_codes_j1939.VehicleStatsFaultCodesJ1939(
                    check_engine_lights = samsara.models.vehicle_stats_fault_codes_j1939_lights.VehicleStatsFaultCodesJ1939Lights(
                        emissions_is_on = True, 
                        protect_is_on = False, 
                        stop_is_on = False, 
                        warning_is_on = False, ), 
                    diagnostic_trouble_codes = [
                        samsara.models.vehicle_stats_fault_codes_j1939_trouble_code.VehicleStatsFaultCodesJ1939TroubleCode(
                            fmi_description = 'Voltage Below Normal', 
                            fmi_id = 9, 
                            mil_status = 1, 
                            occurrence_count = 1, 
                            source_address_name = 'Engine #1', 
                            spn_description = 'System Diagnostic Code #1', 
                            spn_id = 3031, 
                            tx_id = 0, )
                        ], ), 
                obdii = samsara.models.vehicle_stats_fault_codes_obdii.VehicleStatsFaultCodesOBDII(
                    check_engine_light_is_on = True, 
                    diagnostic_trouble_codes = [
                        samsara.models.vehicle_stats_fault_codes_obdii_trouble_code.VehicleStatsFaultCodesOBDIITroubleCode(
                            confirmed_dtcs = [
                                samsara.models.vehicle_stats_fault_codes_passenger_dtc.VehicleStatsFaultCodesPassengerDtc(
                                    dtc_description = 'Fuel Rail/System Pressure - Too Low Bank 1', 
                                    dtc_id = 135, 
                                    dtc_short_code = 'P0087', )
                                ], 
                            ignition_type = 'spark', 
                            mil_status = True, 
                            monitor_status = samsara.models.vehicle_stats_fault_codes_passenger_monitor_status.VehicleStatsFaultCodesPassengerMonitorStatus(
                                catalyst = 'N', 
                                comprehensive = 'N', 
                                egr = 'N', 
                                evap_system = 'N', 
                                fuel = 'N', 
                                heated_catalyst = 'N', 
                                heated_o2_sensor = 'N', 
                                iso_sae_reserved = 'N', 
                                misfire = 'N', 
                                not_ready_count = 56, 
                                o2_sensor = 'N', 
                                secondary_air = 'N', ), 
                            pending_dtcs = [
                                samsara.models.vehicle_stats_fault_codes_passenger_dtc.VehicleStatsFaultCodesPassengerDtc(
                                    dtc_description = 'Fuel Rail/System Pressure - Too Low Bank 1', 
                                    dtc_id = 135, 
                                    dtc_short_code = 'P0087', )
                                ], 
                            permanent_dtcs = [
                                samsara.models.vehicle_stats_fault_codes_passenger_dtc.VehicleStatsFaultCodesPassengerDtc(
                                    dtc_description = 'Fuel Rail/System Pressure - Too Low Bank 1', 
                                    dtc_id = 135, 
                                    dtc_short_code = 'P0087', )
                                ], 
                            tx_id = 0, )
                        ], ), 
                time = '2020-01-27T07:06:25Z'
            )
        else :
            return VehicleStatsFaultCodes(
                time = '2020-01-27T07:06:25Z',
        )

    def testVehicleStatsFaultCodes(self):
        """Test VehicleStatsFaultCodes"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
