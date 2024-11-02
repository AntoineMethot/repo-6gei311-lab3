import connexion
import six
from flask import Flask, request, jsonify
import json
import os

from swagger_server import util

app = Flask(__name__)

def readData():
    "Permet de lire les données dans le fichier json"
    if not os.path.exist('cours.json'):
        return{"cours": []}

    
    with open('cours.json', 'r') as file:
        return json.load(file)
        
    
def writeData(data):
    "ecrit les données dans le fichier JSON"
    with open('cours.json', 'w') as file:
        json.dump(data, file, indent=4)



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
    # if connexion.request.is_json:
    #     idcours = .from_dict(connexion.request.get_json())  # noqa: E501
    # if connexion.request.is_json:
    #     idseance = .from_dict(connexion.request.get_json())  # noqa: E501
    # if connexion.request.is_json:
    #     iddossier = .from_dict(connexion.request.get_json())  # noqa: E501
    # return 'do some magic!'

    data = readData()
    cours = next((c for c in data['cours'] if c['idcours']==idcours),None)
    if cours is None:
        return jsonify({'message':'cours introuvable'}),404
    
    seance = next((s for s in cours['seance'] if s['idseance']==idseance),None)
    if seance is None:
        return jsonify({'message':'seance introuvable'}),404
    
    dossier = next((d for d in seance.get('dossiers',[]) if d['iddossier']==iddossier),None)
    if dossier is None:
        return jsonify({'message':'dossier introuvable'}),404
    
    seance['dossiers'].remove(dossier)
    writeData(data)    

    return '',204





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
    # if connexion.request.is_json:
    #     idcours = .from_dict(connexion.request.get_json())  # noqa: E501
    # if connexion.request.is_json:
    #     idseance = .from_dict(connexion.request.get_json())  # noqa: E501
    # if connexion.request.is_json:
    #     iddossier = .from_dict(connexion.request.get_json())  # noqa: E501
    # return 'do some magic!'

    data = readData()

    cours = next((c for c in data['cours'] if c['idcours']==idcours),None)
    if cours is None:
        return jsonify({'message':'coide introuvable'}),404
    
    seance = next((s for s in cours.get('seances', []) if s['idseance']==idseance),None)
    if seance is None:
        return jsonify({'message':'Seance introuvable'}),404
    
    dossier = next((d for d in seance.get('dossiers',[]) if d['iddossier']==iddossier),None)

    if dossier is None:
        return jsonify({'message':'dossier introuvable'}),404
    
    return jsonify(dossier),200


def get_dosssiers(idcours, idseance):  # noqa: E501
    """Get liste de dossiers dans seances

    Get liste de dossiers dans seances # noqa: E501

    :param idcours: 
    :type idcours: dict | bytes
    :param idseance: 
    :type idseance: dict | bytes

    :rtype: None
    """
    # if connexion.request.is_json:
    #     idcours = .from_dict(connexion.request.get_json())  # noqa: E501
    # if connexion.request.is_json:
    #     idseance = .from_dict(connexion.request.get_json())  # noqa: E501
    # return 'do some magic!'

    data = readData()

    cours = next((c for c in data['cours'] if c['idcours']==idcours),None)
    if cours is None:
        return jsonify({'message':'coide introuvable'}),404
    
    seance = next((s for s in cours.get('seances', []) if s['idseance']==idseance),None)
    if seance is None:
        return jsonify({'message':'Seance introuvable'}),404
    
    return jsonify(seance['dossier']),200

def post_dossier_dans_dossier(idcours, idseance, iddossier):
    data = readData()

    cours = next((c for c in data['cours'] if c['idcours']==idcours),None)
    if cours is None:
        return jsonify({'message':'coide introuvable'}),404
    
    seance = next((s for s in cours.get('seances', []) if s['idseance']==idseance),None)
    if seance is None:
        return jsonify({'message':'Seance introuvable'}),404
    
    dossier = next((d for d in seance.get('dossiers',[]) if d['iddossier']==iddossier),None)
    if dossier is None:
        return jsonify({'message':'dossier introuvable'}),404
    
    
    nouveauDossier = request.get_json()
    nouveauDossier['idseance']=idseance
    nouveauDossier['iddossier']=iddossier

    if seance['dossiers']:
        nouveauID = max(d['iddossier'] for d in seance['dossier'])+1
    
    else:
        nouveauID = 1
    
    nouveauDossier['iddossier'] = nouveauID
    seance['dossiers'].append(nouveauDossier)

    writeData(data)
    return jsonify(nouveauDossier),201





def post_dossier(idcours, idseance):  # noqa: E501
    """Creer dossier dans une seance

    Creer dossier dans une seance # noqa: E501

    :param idcours: 
    :type idcours: dict | bytes
    :param idseance: 
    :type idseance: dict | bytes

    :rtype: None
    """
    # if connexion.request.is_json:
    #     idcours = .from_dict(connexion.request.get_json())  # noqa: E501
    # if connexion.request.is_json:
    #     idseance = .from_dict(connexion.request.get_json())  # noqa: E501
    # return 'do some magic!'

    data = readData()

    cours = next((c for c in data['cours'] if c['idcours']==idcours),None)
    if cours is None:
        return jsonify({'message':'coide introuvable'}),404
    
    seance = next((s for s in cours.get('seances', []) if s['idseance']==idseance),None)
    if seance is None:
        return jsonify({'message':'Seance introuvable'}),404
    
    nouveauDossier = request.get_json()
    nouveauDossier['idseance']=idseance

    if seance['dossiers']:
        nouveauID = max(d['iddossier'] for d in seance['dossier'])+1
    
    else:
        nouveauID = 1
    
    nouveauDossier['iddossier'] = nouveauID
    seance['dossiers'].append(nouveauDossier)

    writeData(data)
    return jsonify(nouveauDossier),201

