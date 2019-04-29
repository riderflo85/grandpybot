#! /usr/bin/env python
# coding: utf-8

from gpbapp.views import index, parser

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