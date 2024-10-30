# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestFichiersController(BaseTestCase):
    """FichiersController integration test stubs"""

    def test_cours_idcours_seances_idseance_dossiers_iddossier_fichiers_post(self):
        """Test case for cours_idcours_seances_idseance_dossiers_iddossier_fichiers_post

        Create a new file for a specific session
        """
        response = self.client.open(
            '/cours/{idcours}/seances/{idseance}/dossiers/{iddossier}/fichiers'.format(idcours=None, idseance=None, iddossier=None),
            method='POST')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_cours_idcours_seances_idseance_fichiers_get(self):
        """Test case for cours_idcours_seances_idseance_fichiers_get

        Retrieve files for a specific session
        """
        response = self.client.open(
            '/cours/{idcours}/seances/{idseance}/fichiers'.format(idcours=None, idseance=None),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_cours_idcours_seances_idseance_fichiers_idfichier_delete(self):
        """Test case for cours_idcours_seances_idseance_fichiers_idfichier_delete

        Delete a file by ID
        """
        response = self.client.open(
            '/cours/{idcours}/seances/{idseance}/fichiers/{idfichier}'.format(idcours=None, idseance=None, idfichier=None),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_cours_idcours_seances_idseance_fichiers_post(self):
        """Test case for cours_idcours_seances_idseance_fichiers_post

        Create a new file for a specific session
        """
        response = self.client.open(
            '/cours/{idcours}/seances/{idseance}/fichiers'.format(idcours=None, idseance=None),
            method='POST')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
