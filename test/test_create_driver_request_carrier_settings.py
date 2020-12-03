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
from samsara.models.create_driver_request_carrier_settings import CreateDriverRequestCarrierSettings  # noqa: E501
from samsara.rest import ApiException

class TestCreateDriverRequestCarrierSettings(unittest.TestCase):
    """CreateDriverRequestCarrierSettings unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CreateDriverRequestCarrierSettings
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = samsara.models.create_driver_request_carrier_settings.CreateDriverRequestCarrierSettings()  # noqa: E501
        if include_optional :
            return CreateDriverRequestCarrierSettings(
                carrier_name = 'Acme Inc.', 
                dot_number = 98231, 
                main_office_address = '1234 Pear St., Scranton, PA 62814'
            )
        else :
            return CreateDriverRequestCarrierSettings(
        )

    def testCreateDriverRequestCarrierSettings(self):
        """Test CreateDriverRequestCarrierSettings"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
