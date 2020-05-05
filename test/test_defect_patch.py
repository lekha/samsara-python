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
from samsara.models.defect_patch import DefectPatch  # noqa: E501
from samsara.rest import ApiException

class TestDefectPatch(unittest.TestCase):
    """DefectPatch unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test DefectPatch
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = samsara.models.defect_patch.DefectPatch()  # noqa: E501
        if include_optional :
            return DefectPatch(
                is_resolved = True, 
                resolved_at_time = '2020-01-27T07:06:25Z', 
                resolved_by = samsara.models.resolved_by.ResolvedBy(
                    id = '11', 
                    type = '0', )
            )
        else :
            return DefectPatch(
                is_resolved = True,
                resolved_by = samsara.models.resolved_by.ResolvedBy(
                    id = '11', 
                    type = '0', ),
        )

    def testDefectPatch(self):
        """Test DefectPatch"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()