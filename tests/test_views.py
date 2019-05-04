#! /usr/bin/env python
# coding: utf-8
import googlemaps
import wikipediaapi

from gpbapp.views import index, LocationSearch, Parser, infos_wikipedia
from gpbapp.constant import API_KEY

# def test_la_fonction_index_de_views():
#     """
#     Premier test après avoir installer Flask
#     Sert à vérifier que Flask est bien installer correctement
#     """
#     assert index() == "Hello world !"

# def test_la_fonction_index_de_views():
    
#     assert index() == str

def test_la_methode_split_word_de_la_classe_parser():
    """
    La methode split_word retourne une liste de mots sans ponctuation
    """
    phrase_a_parser = "Bonjour grandpy, peut tu me trouver l'adresse d'openclassrooms? merci mon pote, je t'aime bien l'ami"
    test = Parser()
    assert test.split_word(phrase_a_parser) == ["bonjour", "grandpy", "peut", "tu", "me", "trouver", "l", "adresse", "d", "openclassrooms", "merci", "mon", "pote", "je", "t", "aime", "bien", "l", "ami"]


def test_la_methode_util_word_de_la_classe_parser():
    """
    La methode util_word retourne une liste de mots util pour les adresses
    """
    list_word = ["bonjour", "grandpy", "peut", "tu", "me", "trouver", "l", "adresse", "d", "openclassrooms", "merci", "mon", "pote", "je", "t", "aime", "bien", "l", "ami"]
    test = Parser()
    assert test.util_word(list_word) == ['openclassrooms'] 

def test_la_methode_address_de_la_classe_parser():
    """
    La methode address retourne une adresse sans le code postal, la ville et le pays
    """
    adresse_test = "7 Cité Paradis, 75010 Paris, France"
    test = Parser()
    assert test.address(adresse_test) == ' Cité Paradis'

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

    def mock_place_predicition(googlemaps):
        return result
    
    monkeypatch.setattr(googlemaps.places, 'places_autocomplete_query', mock_place_predicition)
    search = LocationSearch(API_KEY)
    find_openclassrooms = search.place_prediction("openclassrooms")

    assert find_openclassrooms == result



def test_de_la_fonction_infos_wikipedia(monkeypatch):
    """
    La fonction infos_wikipedia renvoi une courte description d'une
    page wikipedia
    """

    class mockclass():

        summary = "Sallertaine est une commune française située dans le département de la Vendée en région Pays de la Loire.\nSes habitants sont appelés les Sallertainois."
        fullurl = "https://fr.wikipedia.org/wiki/Sallertaine"
        

        def exists(self):
            return True
        

    def mock_wikipedia(param, place):

        return mockclass()
    
    monkeypatch.setattr(wikipediaapi.Wikipedia, 'page', mock_wikipedia)

    search_wiki = infos_wikipedia("sallertaine")

    assert search_wiki == {"link": mockclass.fullurl, "description": "Sallertaine est une commune française située dans le département de la Vendée en région Pays de la Loire. Ses habitants sont appelés les Sallertainois."}