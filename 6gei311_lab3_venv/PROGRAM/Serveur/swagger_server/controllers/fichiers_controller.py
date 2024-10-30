import connexion
import six

from swagger_server import util


def cours_idcours_seances_idseance_dossiers_iddossier_fichiers_post(idcours, idseance, iddossier):  # noqa: E501
    """Create a new file for a specific session

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


def cours_idcours_seances_idseance_fichiers_get(idcours, idseance):  # noqa: E501
    """Retrieve files for a specific session

     # noqa: E501

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


def cours_idcours_seances_idseance_fichiers_idfichier_delete(idcours, idseance, idfichier):  # noqa: E501
    """Delete a file by ID

    Deletea file by ID # noqa: E501

    :param idcours: 
    :type idcours: dict | bytes
    :param idseance: 
    :type idseance: dict | bytes
    :param idfichier: 
    :type idfichier: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        idcours = .from_dict(connexion.request.get_json())  # noqa: E501
    if connexion.request.is_json:
        idseance = .from_dict(connexion.request.get_json())  # noqa: E501
    if connexion.request.is_json:
        idfichier = .from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def cours_idcours_seances_idseance_fichiers_post(idcours, idseance):  # noqa: E501
    """Create a new file for a specific session

     # noqa: E501

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
