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
    
    nouveauFichier = request.get_json()
    nouveauFichier['idseance']=idseance
    nouveauFichier['iddossier']=iddossier
    
    if seance['fichiers']:
        nouveauID = max(f['idfichier'] for f in seance['fichier'])+1
    
    else:
        nouveauID = 1
    
    nouveauFichier['idficher'] = nouveauID
    seance['fichiers'].append(nouveauFichier)

    writeData(data)
    return jsonify(nouveauFichier),201






def cours_idcours_seances_idseance_fichiers_get(idcours, idseance):  # noqa: E501
    """Retrieve files for a specific session

     # noqa: E501

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
    
    fichiers = seance.get('fichiers',[])

    return jsonify(fichiers), 200

    




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
    # if connexion.request.is_json:
    #     idcours = .from_dict(connexion.request.get_json())  # noqa: E501
    # if connexion.request.is_json:
    #     idseance = .from_dict(connexion.request.get_json())  # noqa: E501
    # if connexion.request.is_json:
    #     idfichier = .from_dict(connexion.request.get_json())  # noqa: E501
    # return 'do some magic!'

    data = readData()
    cours = next((c for c in data['cours'] if c['idcours']==idcours),None)
    if cours is None:
        return jsonify({'message':'cours introuvable'}),404
    
    seance = next((s for s in cours['seance'] if s['idseance']==idseance),None)
    if seance is None:
        return jsonify({'message':'seance introuvable'}),404
    
    fichier = next((f for f in seance.get('fichiers',[]) if f['idfichier']==idfichier),None)
    if fichier is None:
        return jsonify({'message':'fichier introuvable'}),404
    
    seance['fichiers'].remove(fichier)
    writeData(data)    

    return '',204



def cours_idcours_seances_idseance_fichiers_post(idcours, idseance):  # noqa: E501
    """Create a new file for a specific session

     # noqa: E501

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
    
    nouveauFichier = request.get_json()
    nouveauFichier['idseance']=idseance
    
    if seance['fichiers']:
        nouveauID = max(f['idfichier'] for f in seance['fichier'])+1
    
    else:
        nouveauID = 1
    
    nouveauFichier['idficher'] = nouveauID
    seance['fichiers'].append(nouveauFichier)

    writeData(data)
    return jsonify(nouveauFichier),201
