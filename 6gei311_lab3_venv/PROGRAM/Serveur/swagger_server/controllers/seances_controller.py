import connexion
import six

from swagger_server import util


def delete_seance(idcours, idseance):  # noqa: E501
    """Delete a seance by ID

    Delete a seance by ID # noqa: E501

    :param idcours: 
    :type idcours: dict | bytes
    :param idseance: 
    :type idseance: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        idcours = .from_dict(connexion.request.get_json())  # noqa: E501
    if connexion.request.is_json:
        idseance = .from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_seances(idcours):  # noqa: E501
    """Get seances pour a cours

    Get seances pour a cours # noqa: E501

    :param idcours: 
    :type idcours: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        idcours = .from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_seances_by_id(idcours, idseance):  # noqa: E501
    """Get a seance by ID

    Get a seance by ID # noqa: E501

    :param idcours: 
    :type idcours: dict | bytes
    :param idseance: 
    :type idseance: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        idcours = .from_dict(connexion.request.get_json())  # noqa: E501
    if connexion.request.is_json:
        idseance = .from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_seances_by_module(idcours, module):  # noqa: E501
    """Get liste de seance by module

    Get liste de seance by module # noqa: E501

    :param idcours: 
    :type idcours: dict | bytes
    :param module: 
    :type module: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        idcours = .from_dict(connexion.request.get_json())  # noqa: E501
    if connexion.request.is_json:
        module = .from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_seances_by_semaine(idcours, semaine):  # noqa: E501
    """Get liste de seance by semaine

    Get liste de seance by semaine # noqa: E501

    :param idcours: 
    :type idcours: dict | bytes
    :param semaine: 
    :type semaine: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        idcours = .from_dict(connexion.request.get_json())  # noqa: E501
    if connexion.request.is_json:
        semaine = .from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def post_seance(idcours):  # noqa: E501
    """Create a new seance in a cours

    Create a new seance in a cours # noqa: E501

    :param idcours: 
    :type idcours: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        idcours = .from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
