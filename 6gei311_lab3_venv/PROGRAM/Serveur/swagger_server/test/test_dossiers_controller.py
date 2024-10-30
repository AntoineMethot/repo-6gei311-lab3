# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestDossiersController(BaseTestCase):
    """DossiersController integration test stubs"""

    def test_cours_idcours_seances_idseance_dossiers_iddossier_delete(self):
        """Test case for cours_idcours_seances_idseance_dossiers_iddossier_delete

        Delete a dossier
        """
        response = self.client.open(
            '/cours/{idcours}/seances/{idseance}/dossiers/{iddossier}'.format(idcours=None, idseance=None, iddossier=None),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_dossier_by_id(self):
        """Test case for get_dossier_by_id

        Get dossier by ID
        """
        response = self.client.open(
            '/cours/{idcours}/seances/{idseance}/dossiers/{iddossier}'.format(idcours=None, idseance=None, iddossier=None),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_dosssiers(self):
        """Test case for get_dosssiers

        Get liste de dossiers dans seances
        """
        response = self.client.open(
            '/cours/{idcours}/seances/{idseance}/dossiers'.format(idcours=None, idseance=None),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_dossier(self):
        """Test case for post_dossier

        Creer dossier dans une seance
        """
        response = self.client.open(
            '/cours/{idcours}/seances/{idseance}/dossiers'.format(idcours=None, idseance=None),
            method='POST')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
