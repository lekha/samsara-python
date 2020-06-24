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
from samsara.models.safety_event import SafetyEvent  # noqa: E501
from samsara.rest import ApiException

class TestSafetyEvent(unittest.TestCase):
    """SafetyEvent unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test SafetyEvent
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = samsara.models.safety_event.SafetyEvent()  # noqa: E501
        if include_optional :
            return SafetyEvent(
                behavior_labels = [
                    samsara.models.safety_event_behavior_label.SafetyEventBehaviorLabel(
                        label = 'genericTailgating', 
                        source = 'automated', )
                    ], 
                coaching_state = 'invalid', 
                download_forward_video_url = 'https://s3.console.aws.amazon.com/s3/buckets/samsara-dashcam-videos/21575/212014918400828/1553060687222/huKA7IhpBV-camera-video-segment-1244214895.mp4', 
                download_inward_video_url = 'https://s3.console.aws.amazon.com/s3/buckets/samsara-dashcam-videos/21575/212014918400828/1553060687222/huKA7IhpBV-camera-video-segment-1244214895.mp4', 
                download_tracked_inward_video_url = 'https://s3.console.aws.amazon.com/s3/buckets/samsara-dashcam-videos/21575/212014918400828/1553060687222/huKA7IhpBV-camera-video-segment-1244214895.mp4', 
                driver = samsara.models.driver_tiny_response.driverTinyResponse(
                    id = '88668', 
                    name = 'Susan Bob', ), 
                id = '212014918174029-1550954461759', 
                location = samsara.models.location.location(
                    latitude = 122.142, 
                    longitude = -93.343, ), 
                max_acceleration_g_force = 0.123, 
                time = '2019-06-13T19:08:25.455Z', 
                vehicle = samsara.models.vehicle_tiny_response.vehicleTinyResponse(
                    id = '123456789', 
                    name = 'Midwest Truck #4', )
            )
        else :
            return SafetyEvent(
        )

    def testSafetyEvent(self):
        """Test SafetyEvent"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
