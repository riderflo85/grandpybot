#! /usr/bin/env python
# coding: utf-8

import re, string
import googlemaps

from . import constant as const

class LocationSearch():

    def __init__(self, api):
        self.maps_service = googlemaps.Client(key=api)
    
    def place_prediction(self, place):
        result = self.maps_service.places_autocomplete_query(
            place
        )
        if result != []:
            match = {
                "description" : result[0]['description']
            }
        else:
            match = None
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
        Méthode qui découpe une chaine de caractère en une liste de mots
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

    def address(self, full_address):
        """
        Méthode qui supprime le code postal, la ville et le pays d'une adresse
        """
        address_name = full_address[:full_address.index(',')]
        r = re.compile(r'\d+')
        return r.sub('', address_name)