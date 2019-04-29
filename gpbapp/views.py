#! /usr/bin/env python
# coding: utf-8

import googlemaps
import wikipediaapi
from flask import Flask, render_template

from . import constant as const

app = Flask(__name__)

@app.route('/')
@app.route('/index/')
def index():
    print(type(render_template('index.html')))
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




def parser(phrase_a_parser):
    """
    Fonction qui découpe une chaine de caractère en une liste de mots
    et sans ponctuation
    """
    result = phrase_a_parser.split()
    phrase_temp = []
    complete_phrase = []

    nb = len(const.SIGN_LIST)

    loop = nb - nb
    for s in const.SIGN_LIST:
        sign = s
        
        if loop == 0:
            for i in result:
                if sign in i:
                    second_parse = i.split(sign)
                    for w in second_parse:
                        complete_phrase.append(w)
                else:
                    complete_phrase.append(i)
            phrase_temp = complete_phrase
            loop += 1

        else:
            for i in complete_phrase:
                if sign in i:
                    second_parse = i.split(sign)
                    for w in second_parse:
                        phrase_temp.append(w)
                else:
                    phrase_temp.append(i)
        
        if loop < nb:
            complete_phrase = []
            complete_phrase = phrase_temp
            phrase_temp = []
            loop += 1
        
        else:
            complete_phrase = phrase_temp
            phrase_temp = []

    for e in complete_phrase[:]:
        if e == "":
            complete_phrase.remove(e)

    return complete_phrase



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