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
from samsara.models.inline_response200 import InlineResponse200  # noqa: E501
from samsara.rest import ApiException

class TestInlineResponse200(unittest.TestCase):
    """InlineResponse200 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test InlineResponse200
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = samsara.models.inline_response200.InlineResponse200()  # noqa: E501
        if include_optional :
            return InlineResponse200(
                data = [
                    samsara.models.carrier_proposed_assignment.CarrierProposedAssignment(
                        accepted_time = samsara.models.accepted_time.acceptedTime(), 
                        active_time = samsara.models.active_time.activeTime(), 
                        driver = samsara.models.driver.driver(), 
                        first_seen_time = samsara.models.first_seen_time.firstSeenTime(), 
                        id = '08b3aeada5f4ab3010c0b4efa28d2d1890dbf8d48d2d', 
                        rejected_time = samsara.models.rejected_time.rejectedTime(), 
                        shipping_docs = 'Delivery 123, chips and soda', 
                        trailers = [
                            samsara.models.trailer_name_only_response.trailerNameOnlyResponse(
                                name = 'Midwest Trailer #5', )
                            ], 
                        vehicle = samsara.models.vehicle.vehicle(), )
                    ], 
                pagination = None
            )
        else :
            return InlineResponse200(
        )

    def testInlineResponse200(self):
        """Test InlineResponse200"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()