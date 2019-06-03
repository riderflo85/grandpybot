#! /usr/bin/env python
# coding: utf-8
import googlemaps
import wikipediaapi

from gpbapp.classes import LocationSearch, Parser
from gpbapp.function import infos_wikipedia
from gpbapp.constant import API_KEY


def test_la_methode_split_word_de_la_classe_parser():
    """
    The split_word method returns a list of words without punctuation
    """
    phrase_a_parser = "Bonjour grandpy, peut tu me trouver l'adresse\
 d'openclassrooms? merci mon pote, je t'aime bien l'ami"
    test = Parser()
    assert test.split_word(phrase_a_parser) == [
        "bonjour", "grandpy", "peut", "tu", "me", "trouver", "l", "adresse",
        "d", "openclassrooms", "merci", "mon", "pote", "je", "t", "aime",
        "bien", "l", "ami"
    ]


def test_la_methode_util_word_de_la_classe_parser():
    """
    The util_word method returns a useful word list for addresses
    """
    list_word = [
        "bonjour", "grandpy", "peut", "tu", "me", "trouver", "l", "adresse",
        "d", "openclassrooms", "merci", "mon", "pote", "je", "t", "aime",
        "bien", "l", "ami"
    ]
    test = Parser()
    assert test.util_word(list_word) == ['openclassrooms']


def test_la_methode_address_de_la_classe_parser():
    """
    The address method returns an address without the postal code,
    city and country
    """
    adresse_test = "7 Cité Paradis, 75010 Paris, France"
    test = Parser()
    assert test.address(adresse_test) == ' Cité Paradis'


def test_de_la_methode_de_classe_place_search(monkeypatch):
    """
    The place_search function returns a dictionary with the
    information of a place
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
    The place_prediction function, searches for a match with the search
    location to be able to determine and find its address
    """
    result = {
        "description": "Openclassrooms, Cité Paradis, Paris, France"
    }

    def mock_place_predicition(googlemaps):
        return result

    monkeypatch.setattr(
        googlemaps.places, 'places_autocomplete_query', mock_place_predicition
    )

    search = LocationSearch(API_KEY)
    find_openclassrooms = search.place_prediction("openclassrooms")

    assert find_openclassrooms == result


def test_de_la_fonction_infos_wikipedia(monkeypatch):
    """
    The infos_wikipedia function returns a short description of a
    wikipedia page
    """
    class mockclass():

        summary = "Sallertaine est une commune française située dans le\
 département de la Vendée en région Pays de la Loire.\nSes habitants sont\
 appelés les Sallertainois."

        fullurl = "https://fr.wikipedia.org/wiki/Sallertaine"

        def exists(self):
            return True

    def mock_wikipedia(param, place):

        return mockclass()

    monkeypatch.setattr(wikipediaapi.Wikipedia, 'page', mock_wikipedia)

    search_wiki = infos_wikipedia("sallertaine")

    assert search_wiki == {
        "link": mockclass.fullurl,
        "description": "Sallertaine est une commune française située dans le\
 département de la Vendée en région Pays de la Loire. Ses habitants sont\
 appelés les Sallertainois."
    }
