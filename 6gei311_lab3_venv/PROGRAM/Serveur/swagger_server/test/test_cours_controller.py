# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestCoursController(BaseTestCase):
    """CoursController integration test stubs"""

    def test_delete_cours(self):
        """Test case for delete_cours

        Delete a cours by ID
        """
        response = self.client.open(
            '/cours/{idcours}'.format(idcours=None),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_cours(self):
        """Test case for get_cours

        Retrieve a list of all courses
        """
        response = self.client.open(
            '/cours',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_cours_by_id(self):
        """Test case for get_cours_by_id

        Retrieve a cours by ID
        """
        response = self.client.open(
            '/cours/{idcours}'.format(idcours=None),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_cours_by_tag(self):
        """Test case for get_cours_by_tag

        Retrieve a Cours by Tag
        """
        response = self.client.open(
            '/cours/{tag}'.format(tag=None),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_cours(self):
        """Test case for post_cours

        Create a new cours
        """
        response = self.client.open(
            '/cours',
            method='POST')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
