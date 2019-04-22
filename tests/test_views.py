from gpbapp.views import index

def test_la_fonction_index_de_views():
    assert index() == "Hello world !"
