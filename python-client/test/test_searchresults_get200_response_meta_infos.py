"""
    Bundes-Klinik-Atlas API

    Die API des Bundes-Klinik-Atlas stellt eine Vielzahl von Informationen über deutsche Kliniken und deren Ausstattung bereit.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: poststelle@bmg.bund.de
    Generated by: https://openapi-generator.tech
"""

import sys
import unittest

from deutschland.klinikatlas.model.searchresults_get200_response_meta_infos_search_arguments import (
    SearchresultsGet200ResponseMetaInfosSearchArguments,
)

from deutschland import klinikatlas

globals()[
    "SearchresultsGet200ResponseMetaInfosSearchArguments"
] = SearchresultsGet200ResponseMetaInfosSearchArguments
from deutschland.klinikatlas.model.searchresults_get200_response_meta_infos import (
    SearchresultsGet200ResponseMetaInfos,
)


class TestSearchresultsGet200ResponseMetaInfos(unittest.TestCase):
    """SearchresultsGet200ResponseMetaInfos unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSearchresultsGet200ResponseMetaInfos(self):
        """Test SearchresultsGet200ResponseMetaInfos"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SearchresultsGet200ResponseMetaInfos()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()