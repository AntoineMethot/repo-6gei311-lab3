# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestSeancesController(BaseTestCase):
    """SeancesController integration test stubs"""

    def test_delete_seance(self):
        """Test case for delete_seance

        Delete a seance by ID
        """
        response = self.client.open(
            '/cours/{idcours}/seances/{idseance}'.format(idcours=None, idseance=None),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_seances(self):
        """Test case for get_seances

        Get seances pour a cours
        """
        response = self.client.open(
            '/cours/{idcours}/seances'.format(idcours=None),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_seances_by_id(self):
        """Test case for get_seances_by_id

        Get a seance by ID
        """
        response = self.client.open(
            '/cours/{idcours}/seances/{idseance}'.format(idcours=None, idseance=None),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_seances_by_module(self):
        """Test case for get_seances_by_module

        Get liste de seance by module
        """
        query_string = [('module', None)]
        response = self.client.open(
            '/cours/{idcours}/seances/module'.format(idcours=None),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_seances_by_semaine(self):
        """Test case for get_seances_by_semaine

        Get liste de seance by semaine
        """
        query_string = [('semaine', None)]
        response = self.client.open(
            '/cours/{idcours}/seances/semaine'.format(idcours=None),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_seance(self):
        """Test case for post_seance

        Create a new seance in a cours
        """
        response = self.client.open(
            '/cours/{idcours}/seances'.format(idcours=None),
            method='POST')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
