#! /usr/bin/env python
# coding: utf-8

import re, string
import googlemaps
import wikipediaapi
from flask import Flask, render_template

from . import constant as const

app = Flask(__name__)

@app.route('/')
@app.route('/index/')
def index():
    return render_template('index.html')


class LocationSearch():

    def __init__(self, api):
        self.maps_service = googlemaps.Client(key=api)
    
    def place_prediction(self, place):
        result = self.maps_service.places_autocomplete_query(
            place
        )
        match = {
            "description" : result[0]['description']
        }
        return match

    def places_search(self, place):
        result = self.maps_service.places(place)
        infos_util = {
            "formatted_address": result['results'][0]['formatted_address'],
            "name": result['results'][0]['name'],
            "location": {
                "lat": result['results'][0]['geometry']['location']['lat'],
                "lng": result['results'][0]['geometry']['location']['lng']
            },
        }
        return infos_util



class Parser():

    def split_word(self, phrase_a_parser):
        """
        Fonction qui découpe une chaine de caractère en une liste de mots
        et sans ponctuation
        """
        result = re.split(r'(\W+)', phrase_a_parser.lower())

        for punctuation in string.punctuation:
            for word in result:
                if punctuation in word:
                    result.remove(word)

        for word in result:
            if word == " ":
                result.remove(word)

        return result
    
    def util_word(self, list_word):
        """
        Méthode qui retire tout les mots inutile pour garder qu'une adresse
        """
        result = list_word
        for element in const.STOP_WORD:
            for word in result:
                if word == element:
                    result.remove(word)
                else:
                    pass

        return result


def infos_wikipedia(place):
    wiki_service = wikipediaapi.Wikipedia('fr')
    result_search = wiki_service.page(place)

    if result_search.exists():
        desc = result_search.summary

        if "\n" in desc:
            desc = desc.replace("\n", " ")
            result_infos = {"link": result_search.fullurl, "description": desc}
            return result_infos
    
    else:
        return "La page n'existe pas"


if __name__ == "__main__":
    app.run()