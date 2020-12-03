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
from samsara.models.vehicle_response import VehicleResponse  # noqa: E501
from samsara.rest import ApiException

class TestVehicleResponse(unittest.TestCase):
    """VehicleResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test VehicleResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = samsara.models.vehicle_response.VehicleResponse()  # noqa: E501
        if include_optional :
            return VehicleResponse(
                data = samsara.models.vehicle.Vehicle(
                    aux_input_type1 = 'boom', 
                    aux_input_type10 = 'boom', 
                    aux_input_type2 = 'boom', 
                    aux_input_type3 = 'boom', 
                    aux_input_type4 = 'boom', 
                    aux_input_type5 = 'boom', 
                    aux_input_type6 = 'boom', 
                    aux_input_type7 = 'boom', 
                    aux_input_type8 = 'boom', 
                    aux_input_type9 = 'boom', 
                    camera_serial = 'CNCK-VT8-XA8', 
                    external_ids = {maintenanceId=250020, payrollId=ABFS18600}, 
                    harsh_acceleration_setting_type = 'off', 
                    id = '112', 
                    license_plate = 'XHK1234', 
                    make = 'Ford', 
                    model = 'F150', 
                    name = 'Truck A7', 
                    notes = 'These are notes about this given vehicle.', 
                    serial = 'VG12345', 
                    static_assigned_driver = samsara.models.driver_tiny_response.driverTinyResponse(
                        id = '88668', 
                        name = 'Susan Bob', ), 
                    tags = [
                        samsara.models.tag_tiny_response.tagTinyResponse(
                            id = '3914', 
                            name = 'East Coast', 
                            parent_tag_id = '4815', )
                        ], 
                    vin = '1FUJA6BD31LJ09646', 
                    year = '2008', )
            )
        else :
            return VehicleResponse(
                data = samsara.models.vehicle.Vehicle(
                    aux_input_type1 = 'boom', 
                    aux_input_type10 = 'boom', 
                    aux_input_type2 = 'boom', 
                    aux_input_type3 = 'boom', 
                    aux_input_type4 = 'boom', 
                    aux_input_type5 = 'boom', 
                    aux_input_type6 = 'boom', 
                    aux_input_type7 = 'boom', 
                    aux_input_type8 = 'boom', 
                    aux_input_type9 = 'boom', 
                    camera_serial = 'CNCK-VT8-XA8', 
                    external_ids = {maintenanceId=250020, payrollId=ABFS18600}, 
                    harsh_acceleration_setting_type = 'off', 
                    id = '112', 
                    license_plate = 'XHK1234', 
                    make = 'Ford', 
                    model = 'F150', 
                    name = 'Truck A7', 
                    notes = 'These are notes about this given vehicle.', 
                    serial = 'VG12345', 
                    static_assigned_driver = samsara.models.driver_tiny_response.driverTinyResponse(
                        id = '88668', 
                        name = 'Susan Bob', ), 
                    tags = [
                        samsara.models.tag_tiny_response.tagTinyResponse(
                            id = '3914', 
                            name = 'East Coast', 
                            parent_tag_id = '4815', )
                        ], 
                    vin = '1FUJA6BD31LJ09646', 
                    year = '2008', ),
        )

    def testVehicleResponse(self):
        """Test VehicleResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
