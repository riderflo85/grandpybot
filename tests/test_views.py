#! /usr/bin/env python
# coding: utf-8
import googlemaps
import wikipediaapi

from gpbapp.views import index, LocationSearch, infos_wikipedia, parser
from gpbapp.constant import API_KEY

# def test_la_fonction_index_de_views():
#     """
#     Premier test après avoir installer Flask
#     Sert à vérifier que Flask est bien installer correctement
#     """
#     assert index() == "Hello world !"

# def test_la_fonction_index_de_views():
    
#     assert index() == str

def test_la_fonction_parser():
    """
    La fonction parser retourne une liste de mots sans ponctuation
    """
    phrase_a_parser = "Bonjour grandpy, peut tu me trouver l'adresse d'openclassrooms? merci mon pote, je t'aime bien l'ami"

    assert parser(phrase_a_parser) == ["Bonjour", "grandpy", "peut", "tu", "me", "trouver", "l", "adresse", "d", "openclassrooms", "merci", "mon", "pote", "je", "t", "aime", "bien", "l", "ami"]




def test_de_la_methode_de_classe_place_search(monkeypatch):
    """
    La fonction place_search retourn un dictionnaire avec les informations
    d'un lieu.
    """
    result = {
        "formatted_address": "Rennes, France",
        "name": "Rennes",
        "location": {
                "lat": 48.117266,
                "lng": -1.6777926
            },
        }


    def mock_googlemaps(googlemaps):
        return result
    
    monkeypatch.setattr(googlemaps, 'places', mock_googlemaps)

    search = LocationSearch(API_KEY)
    find_rennes = search.places_search("Rennes")

    assert find_rennes == result




def test_de_la_methode_de_classe_place_prediction(monkeypatch):
    """
    La fonction place_prediction, recherche une correspondance avec le
    lieu chercher pour pouvoir déterminer et trouver son adresse
    """
    result = {
        "description": "Openclassrooms, Cité Paradis, Paris, France"
    }

    def mock_place_predicition(googlempas):
        return result
    
    monkeypatch.setattr(googlemaps, 'places_autocomplete_query', mock_place_predicition)
    search = LocationSearch(API_KEY)
    find_openclassrooms = search.place_prediction("openclassrooms")

    assert find_openclassrooms == result



def test_de_la_fonction_infos_wikipedia(monkeypatch):
    result_wiki = {
        "link": "https://fr.wikipedia.org/wiki/Sallertaine", "description": "Sallertaine est une commune française située dans le département de la Vendée en région Pays de la Loire. Ses habitants sont appelés les Sallertainois."
        }

    def mock_wikipedia(wikipediaapi):
        return result_wiki
    
    monkeypatch.setattr(wikipediaapi, 'page', mock_wikipedia)

    search_wiki = infos_wikipedia("sallertaine")

    assert search_wiki == result_wiki