# coding: utf-8

"""
    LABO3

    MANAGE THE FILES  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class DossiersApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def cours_idcours_seances_idseance_dossiers_iddossier_delete(self, idcours, idseance, iddossier, **kwargs):  # noqa: E501
        """Delete a dossier  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.cours_idcours_seances_idseance_dossiers_iddossier_delete(idcours, idseance, iddossier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object idcours: (required)
        :param object idseance: (required)
        :param object iddossier: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.cours_idcours_seances_idseance_dossiers_iddossier_delete_with_http_info(idcours, idseance, iddossier, **kwargs)  # noqa: E501
        else:
            (data) = self.cours_idcours_seances_idseance_dossiers_iddossier_delete_with_http_info(idcours, idseance, iddossier, **kwargs)  # noqa: E501
            return data

    def cours_idcours_seances_idseance_dossiers_iddossier_delete_with_http_info(self, idcours, idseance, iddossier, **kwargs):  # noqa: E501
        """Delete a dossier  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.cours_idcours_seances_idseance_dossiers_iddossier_delete_with_http_info(idcours, idseance, iddossier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object idcours: (required)
        :param object idseance: (required)
        :param object iddossier: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['idcours', 'idseance', 'iddossier']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method cours_idcours_seances_idseance_dossiers_iddossier_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'idcours' is set
        if ('idcours' not in params or
                params['idcours'] is None):
            raise ValueError("Missing the required parameter `idcours` when calling `cours_idcours_seances_idseance_dossiers_iddossier_delete`")  # noqa: E501
        # verify the required parameter 'idseance' is set
        if ('idseance' not in params or
                params['idseance'] is None):
            raise ValueError("Missing the required parameter `idseance` when calling `cours_idcours_seances_idseance_dossiers_iddossier_delete`")  # noqa: E501
        # verify the required parameter 'iddossier' is set
        if ('iddossier' not in params or
                params['iddossier'] is None):
            raise ValueError("Missing the required parameter `iddossier` when calling `cours_idcours_seances_idseance_dossiers_iddossier_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'idcours' in params:
            path_params['idcours'] = params['idcours']  # noqa: E501
        if 'idseance' in params:
            path_params['idseance'] = params['idseance']  # noqa: E501
        if 'iddossier' in params:
            path_params['iddossier'] = params['iddossier']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/cours/{idcours}/seances/{idseance}/dossiers/{iddossier}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_dossier_by_id(self, idcours, idseance, iddossier, **kwargs):  # noqa: E501
        """Get dossier by ID  # noqa: E501

        Get dossier by ID  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_dossier_by_id(idcours, idseance, iddossier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object idcours: (required)
        :param object idseance: (required)
        :param object iddossier: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_dossier_by_id_with_http_info(idcours, idseance, iddossier, **kwargs)  # noqa: E501
        else:
            (data) = self.get_dossier_by_id_with_http_info(idcours, idseance, iddossier, **kwargs)  # noqa: E501
            return data

    def get_dossier_by_id_with_http_info(self, idcours, idseance, iddossier, **kwargs):  # noqa: E501
        """Get dossier by ID  # noqa: E501

        Get dossier by ID  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_dossier_by_id_with_http_info(idcours, idseance, iddossier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object idcours: (required)
        :param object idseance: (required)
        :param object iddossier: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['idcours', 'idseance', 'iddossier']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_dossier_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'idcours' is set
        if ('idcours' not in params or
                params['idcours'] is None):
            raise ValueError("Missing the required parameter `idcours` when calling `get_dossier_by_id`")  # noqa: E501
        # verify the required parameter 'idseance' is set
        if ('idseance' not in params or
                params['idseance'] is None):
            raise ValueError("Missing the required parameter `idseance` when calling `get_dossier_by_id`")  # noqa: E501
        # verify the required parameter 'iddossier' is set
        if ('iddossier' not in params or
                params['iddossier'] is None):
            raise ValueError("Missing the required parameter `iddossier` when calling `get_dossier_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'idcours' in params:
            path_params['idcours'] = params['idcours']  # noqa: E501
        if 'idseance' in params:
            path_params['idseance'] = params['idseance']  # noqa: E501
        if 'iddossier' in params:
            path_params['iddossier'] = params['iddossier']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/cours/{idcours}/seances/{idseance}/dossiers/{iddossier}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_dosssiers(self, idcours, idseance, **kwargs):  # noqa: E501
        """Get liste de dossiers dans seances  # noqa: E501

        Get liste de dossiers dans seances  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_dosssiers(idcours, idseance, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object idcours: (required)
        :param object idseance: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_dosssiers_with_http_info(idcours, idseance, **kwargs)  # noqa: E501
        else:
            (data) = self.get_dosssiers_with_http_info(idcours, idseance, **kwargs)  # noqa: E501
            return data

    def get_dosssiers_with_http_info(self, idcours, idseance, **kwargs):  # noqa: E501
        """Get liste de dossiers dans seances  # noqa: E501

        Get liste de dossiers dans seances  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_dosssiers_with_http_info(idcours, idseance, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object idcours: (required)
        :param object idseance: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['idcours', 'idseance']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_dosssiers" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'idcours' is set
        if ('idcours' not in params or
                params['idcours'] is None):
            raise ValueError("Missing the required parameter `idcours` when calling `get_dosssiers`")  # noqa: E501
        # verify the required parameter 'idseance' is set
        if ('idseance' not in params or
                params['idseance'] is None):
            raise ValueError("Missing the required parameter `idseance` when calling `get_dosssiers`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'idcours' in params:
            path_params['idcours'] = params['idcours']  # noqa: E501
        if 'idseance' in params:
            path_params['idseance'] = params['idseance']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/cours/{idcours}/seances/{idseance}/dossiers', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_dossier(self, idcours, idseance, **kwargs):  # noqa: E501
        """Creer dossier dans une seance  # noqa: E501

        Creer dossier dans une seance  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_dossier(idcours, idseance, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object idcours: (required)
        :param object idseance: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.post_dossier_with_http_info(idcours, idseance, **kwargs)  # noqa: E501
        else:
            (data) = self.post_dossier_with_http_info(idcours, idseance, **kwargs)  # noqa: E501
            return data

    def post_dossier_with_http_info(self, idcours, idseance, **kwargs):  # noqa: E501
        """Creer dossier dans une seance  # noqa: E501

        Creer dossier dans une seance  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_dossier_with_http_info(idcours, idseance, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object idcours: (required)
        :param object idseance: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['idcours', 'idseance']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_dossier" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'idcours' is set
        if ('idcours' not in params or
                params['idcours'] is None):
            raise ValueError("Missing the required parameter `idcours` when calling `post_dossier`")  # noqa: E501
        # verify the required parameter 'idseance' is set
        if ('idseance' not in params or
                params['idseance'] is None):
            raise ValueError("Missing the required parameter `idseance` when calling `post_dossier`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'idcours' in params:
            path_params['idcours'] = params['idcours']  # noqa: E501
        if 'idseance' in params:
            path_params['idseance'] = params['idseance']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/cours/{idcours}/seances/{idseance}/dossiers', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
