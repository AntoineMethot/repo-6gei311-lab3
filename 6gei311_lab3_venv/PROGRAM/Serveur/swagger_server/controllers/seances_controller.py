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


def delete_seance(idcours, idseance):  # noqa: E501
    """Delete a seance by ID

    Delete a seance by ID # noqa: E501

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
        return jsonify({'message':'cours introuvable'}),404
    
    seance = next((s for s in cours['seance'] if s['idseance']==idseance),None)
    if seance is None:
        return jsonify({'message':'seance introuvable'}),404
    data['seances'].remove(seance)
    writeData(data)    

    return '',204
    


   



def get_seances(idcours):  # noqa: E501
    """Get seances pour a cours

    Get seances pour a cours # noqa: E501

    :param idcours: 
    :type idcours: dict | bytes

    :rtype: None
    """
    # if connexion.request.is_json:
    #     idcours = .from_dict(connexion.request.get_json())  # noqa: E501
    # return 'do some magic!'
    data = readData()

    cours = next((c for c in data['cours'] if c['idcours']==idcours),None)
    if cours is None:
        return jsonify({'message': 'Cours introuvable'}),404
    return jsonify(cours['seances']),200


def get_seances_by_id(idcours, idseance):  # noqa: E501
    """Get a seance by ID

    Get a seance by ID # noqa: E501

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
    
    return jsonify(seance),200


def get_seances_by_module(idcours, module):  # noqa: E501
    """Get liste de seance by module

    Get liste de seance by module # noqa: E501

    :param idcours: 
    :type idcours: dict | bytes
    :param module: 
    :type module: dict | bytes

    :rtype: None
    """
    # if connexion.request.is_json:
    #     idcours = .from_dict(connexion.request.get_json())  # noqa: E501
    # if connexion.request.is_json:
    #     module = .from_dict(connexion.request.get_json())  # noqa: E501
    # return 'do some magic!'

    data = readData()

    cours = next((c for c in data['cours'] if c['idcours']==idcours),None)
    if cours is None:
        return jsonify({'message':'coide introuvable'}),404
    
    seance = next((s for s in cours.get('seances', []) if s['module']==module),None)
    if seance is None:
        return jsonify({'message':'Seance introuvable'}),404
    
    return jsonify(seance),200


def get_seances_by_semaine(idcours, semaine):  # noqa: E501
    """Get liste de seance by semaine

    Get liste de seance by semaine # noqa: E501

    :param idcours: 
    :type idcours: dict | bytes
    :param semaine: 
    :type semaine: dict | bytes

    :rtype: None
    """
    # if connexion.request.is_json:
    #     idcours = .from_dict(connexion.request.get_json())  # noqa: E501
    # if connexion.request.is_json:
    #     semaine = .from_dict(connexion.request.get_json())  # noqa: E501
    # return 'do some magic!'

    data = readData()

    cours = next((c for c in data['cours'] if c['idcours']==idcours),None)
    if cours is None:
        return jsonify({'message':'coide introuvable'}),404
    
    seance = next((s for s in cours.get('seances', []) if s['semaine']==semaine),None)
    if seance is None:
        return jsonify({'message':'Seance introuvable'}),404
    
    return jsonify(seance),200


def post_seance(idcours):  # noqa: E501
    """Create a new seance in a cours

    Create a new seance in a cours # noqa: E501

    :param idcours: 
    :type idcours: dict | bytes

    :rtype: None
    """
    # if connexion.request.is_json:
    #     idcours = .from_dict(connexion.request.get_json())  # noqa: E501
    # return 'do some magic!'

    data = readData()
    cours = next((c for c in data['cours'] if c['idcours'] == idcours), None)
    if cours is None:
        return jsonify({"message": "Cours introuvable"}), 404

    nouvelleSeance = request.json

    if cours['seances']:
        nouveauID = max(s['idseance'] for s in cours['seances'])+1
    
    else:
        nouveauID = 1
    
    nouvelleSeance['idseance'] = nouveauID
    cours['seance'].append(nouvelleSeance)

    writeData(data)
    return jsonify(nouvelleSeance),201
