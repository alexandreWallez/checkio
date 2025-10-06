from src.checkio.millifaersla import millifaersla

def test_millifaersla() :
    assert millifaersla(3,9,7) == "Monnei"
    assert millifaersla(323,19,999) == "Fjee"
    assert millifaersla(40,30,20) == "Dolladollabilljoll"