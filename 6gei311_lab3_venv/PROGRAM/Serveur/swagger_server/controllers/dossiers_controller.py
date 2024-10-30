import connexion
import six

from swagger_server import util


def cours_idcours_seances_idseance_dossiers_iddossier_delete(idcours, idseance, iddossier):  # noqa: E501
    """Delete a dossier

     # noqa: E501

    :param idcours: 
    :type idcours: dict | bytes
    :param idseance: 
    :type idseance: dict | bytes
    :param iddossier: 
    :type iddossier: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        idcours = .from_dict(connexion.request.get_json())  # noqa: E501
    if connexion.request.is_json:
        idseance = .from_dict(connexion.request.get_json())  # noqa: E501
    if connexion.request.is_json:
        iddossier = .from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_dossier_by_id(idcours, idseance, iddossier):  # noqa: E501
    """Get dossier by ID

    Get dossier by ID # noqa: E501

    :param idcours: 
    :type idcours: dict | bytes
    :param idseance: 
    :type idseance: dict | bytes
    :param iddossier: 
    :type iddossier: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        idcours = .from_dict(connexion.request.get_json())  # noqa: E501
    if connexion.request.is_json:
        idseance = .from_dict(connexion.request.get_json())  # noqa: E501
    if connexion.request.is_json:
        iddossier = .from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_dosssiers(idcours, idseance):  # noqa: E501
    """Get liste de dossiers dans seances

    Get liste de dossiers dans seances # noqa: E501

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


def post_dossier(idcours, idseance):  # noqa: E501
    """Creer dossier dans une seance

    Creer dossier dans une seance # noqa: E501

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
