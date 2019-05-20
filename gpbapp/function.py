#! /usr/bin/env python
# coding: utf-8

import wikipediaapi

def infos_wikipedia(place):
    """
    Function that searches and displays the description of a wikipedia page
    """
    wiki_service = wikipediaapi.Wikipedia('fr')
    result_search = wiki_service.page(place)

    if result_search.exists():
        desc = result_search.summary

        if "\n" in desc:
            desc = desc.replace("\n", " ")
            result_infos = {"link": result_search.fullurl, "description": desc}
            return result_infos
        else:
            result_infos = {"link": result_search.fullurl, "description": desc}
            return result_infos

    else:
        return None
