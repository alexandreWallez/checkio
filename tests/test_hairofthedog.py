from src.checkio.hairofthedog import hairofthedog

def test_hairofthedog() :
    assert hairofthedog(5,["sober","drunk","drunk","sober","sober"]) == 1
    assert hairofthedog(5,["sober","drunk","sober","drunk","sober"]) == 2