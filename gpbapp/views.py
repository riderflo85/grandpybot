#! /usr/bin/env python
# coding: utf-8

import json, random
from flask import Flask, render_template, request

from . import constant as const
from gpbapp.classes import LocationSearch, Parser
from gpbapp.function import infos_wikipedia

app = Flask(__name__)

@app.route('/')
@app.route('/index/')
def index():
    return render_template('index.html', API_KEY = const.API_KEY)

@app.route('/search', methods=['GET'])
def search():
    phrase = request.args.get('phrase')

    data = Parser()
    geolocation = LocationSearch(const.API_KEY)

    # cuts the sentence into words
    data_user = data.split_word(phrase)
    phrase_parser = data.util_word(data_user)
    complete_string = " ".join(phrase_parser)

    # Look for the place
    prediction = geolocation.place_prediction(complete_string)

    if not prediction:
        details = "Lieu non trouver"
        history = "La page n'existe pas"
    else:
        details = geolocation.places_search(prediction['description'])

        if not infos_wikipedia(complete_string):
            address_for_wiki = data.address(details['formatted_address'])

            if not infos_wikipedia(address_for_wiki):
                history = "La page n'existe pas"

            else:
                history = infos_wikipedia(address_for_wiki)

        else:
            history = infos_wikipedia(complete_string)

    return json.dumps({
        'status': 'OK',
        'result': details,
        'history': history,
        'story': random.choice(const.STORY)
        })

if __name__ == "__main__":
    app.run()