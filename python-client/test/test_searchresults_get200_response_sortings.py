"""
    Bundes-Klinik-Atlas API

    Die API des Bundes-Klinik-Atlas stellt eine Vielzahl von Informationen über deutsche Kliniken und deren Ausstattung bereit.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: poststelle@bmg.bund.de
    Generated by: https://openapi-generator.tech
"""

import sys
import unittest

from deutschland.klinikatlas.model.searchresults_get200_response_sortings_fields_inner import (
    SearchresultsGet200ResponseSortingsFieldsInner,
)

from deutschland import klinikatlas

globals()[
    "SearchresultsGet200ResponseSortingsFieldsInner"
] = SearchresultsGet200ResponseSortingsFieldsInner
from deutschland.klinikatlas.model.searchresults_get200_response_sortings import (
    SearchresultsGet200ResponseSortings,
)


class TestSearchresultsGet200ResponseSortings(unittest.TestCase):
    """SearchresultsGet200ResponseSortings unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSearchresultsGet200ResponseSortings(self):
        """Test SearchresultsGet200ResponseSortings"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SearchresultsGet200ResponseSortings()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()