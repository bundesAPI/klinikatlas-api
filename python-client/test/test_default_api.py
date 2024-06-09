"""
    Bundes-Klinik-Atlas API

    Die API des Bundes-Klinik-Atlas stellt eine Vielzahl von Informationen über deutsche Kliniken und deren Ausstattung bereit.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: poststelle@bmg.bund.de
    Generated by: https://openapi-generator.tech
"""

import unittest

from deutschland.klinikatlas.api.default_api import DefaultApi  # noqa: E501

from deutschland import klinikatlas


class TestDefaultApi(unittest.TestCase):
    """DefaultApi unit test stubs"""

    def setUp(self):
        self.api = DefaultApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_fileadmin_json_german_places_json_get(self):
        """Test case for fileadmin_json_german_places_json_get

        Liste deutscher Orte abrufen  # noqa: E501
        """
        pass

    def test_fileadmin_json_german_states_json_get(self):
        """Test case for fileadmin_json_german_states_json_get

        Liste deutscher Bundesländer mit Koordinaten abrufen  # noqa: E501
        """
        pass

    def test_fileadmin_json_icd_codes_json_get(self):
        """Test case for fileadmin_json_icd_codes_json_get

        Liste der ICD-Codes abrufen  # noqa: E501
        """
        pass

    def test_fileadmin_json_locations_json_get(self):
        """Test case for fileadmin_json_locations_json_get

        Liste deutscher Kliniken abrufen  # noqa: E501
        """
        pass

    def test_fileadmin_json_ops_codes_json_get(self):
        """Test case for fileadmin_json_ops_codes_json_get

        Liste der OPS-Codes abrufen  # noqa: E501
        """
        pass

    def test_fileadmin_json_states_json_get(self):
        """Test case for fileadmin_json_states_json_get

        Liste deutscher Bundesländer abrufen  # noqa: E501
        """
        pass

    def test_krankenhaussuche_krankenhaus_id_get(self):
        """Test case for krankenhaussuche_krankenhaus_id_get

        Details zu einem spezifischen Krankenhaus abrufen  # noqa: E501
        """
        pass

    def test_searchresults_get(self):
        """Test case for searchresults_get

        Suche nach Krankenhäusern basierend auf spezifischen Kriterien  # noqa: E501
        """
        pass


if __name__ == "__main__":
    unittest.main()
