import connexion
import six

from swagger_server import util


def delete_cours(idcours):  # noqa: E501
    """Delete a cours by ID

    Delete a cours by ID # noqa: E501

    :param idcours: 
    :type idcours: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        idcours = .from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_cours():  # noqa: E501
    """Retrieve a list of all courses

    Retrieve a list of all courses # noqa: E501


    :rtype: None
    """
    return 'do some magic!'


def get_cours_by_id(idcours):  # noqa: E501
    """Retrieve a cours by ID

    Retrieve a cours by ID # noqa: E501

    :param idcours: ID of cours to return
    :type idcours: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        idcours = .from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_cours_by_tag(tag):  # noqa: E501
    """Retrieve a Cours by Tag

    Retrieve a Cours by Tag # noqa: E501

    :param tag: Tags to filter by
    :type tag: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tag = .from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def post_cours():  # noqa: E501
    """Create a new cours

    Create a new cours # noqa: E501


    :rtype: None
    """
    return 'do some magic!'
