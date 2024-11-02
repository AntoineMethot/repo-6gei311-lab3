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


def delete_cours(idcours):  # noqa: E501
    """Delete a cours by ID

    Delete a cours by ID # noqa: E501

    :param idcours: 
    :type idcours: dict | bytes

    :rtype: None
    """

    data = readData()
    cours = next((c for c in data['cours'] if c['idcours'] == idcours), None)

    if cours is None:
        return jsonify({"message": "Cours non trouvé"}),404
    
    data['cours'].remove(cours)
    writeData(data)

    return '',204


    # if connexion.request.is_json:
    #     idcours = .from_dict(connexion.request.get_json())  # noqa: E501
    # return 'do some magic!'


def get_cours():  # noqa: E501
    """Retrieve a list of all courses

    Retrieve a list of all courses # noqa: E501


    :rtype: None
    """
    data = readData()
    return jsonify(data['cours']),200



def get_cours_by_id(idcours):  # noqa: E501
    """Retrieve a cours by ID

    Retrieve a cours by ID # noqa: E501

    :param idcours: ID of cours to return
    :type idcours: dict | bytes
    :rtype: None
    """
    # if connexion.request.is_json:
    #     idcours = .from_dict(connexion.request.get_json())  # noqa: E501
    data= readData()
    cours = next((c for c in data['cours'] if c['idcours']==idcours),None)

    if cours is None:
        return jsonify({'message':'code non trouve'}),404
    
    return jsonify(cours),200



def get_cours_by_tag(tag):  # noqa: E501
    """Retrieve a Cours by Tag

    Retrieve a Cours by Tag # noqa: E501

    :param tag: Tags to filter by
    :type tag: dict | bytes

    :rtype: None
    """
    # if connexion.request.is_json:
    #     tag = .from_dict(connexion.request.get_json())  # noqa: 
    data = readData()
    cours_with_tag = [c for c in data['cours'] if tag in c.get('tags', [])]
    
    if not cours_with_tag:
        return jsonify({"message": "Aucun cours trouvé avec ce tag"}), 404
    
    return jsonify(cours_with_tag), 200



def post_cours():  # noqa: E501
    """Create a new cours

    Create a new cours # noqa: E501


    :rtype: None
    """

    nouveauCours = request.json
    data = readData()

    if data['cours']:
        nouveauID = max(c['idcours'] for c in data['cours'])+1
    
    else:
        nouveauID = 1
    
    nouveauCours['idcours'] = nouveauID
    data['cours'].append(nouveauCours)
    writeData(data)


    return jsonify(nouveauCours),201
