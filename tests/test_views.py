#! /usr/bin/env python
# coding: utf-8

from gpbapp.views import index

def test_la_fonction_index_de_views():
    """
    Premier test après avoir installer Flask
    Sert à vérifier que Flask est bien installer correctement
    """
    assert index() == "Hello world !"
