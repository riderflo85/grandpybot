#! /usr/bin/env python
# coding: utf-8

from flask import Flask, render_template

from . import constant as const

app = Flask(__name__)

@app.route('/')
@app.route('/index/')
def index():
    print(type(render_template('index.html')))
    return render_template('index.html')

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

    

if __name__ == "__main__":
    app.run()