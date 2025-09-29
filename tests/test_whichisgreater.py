from checkio.whichisgreater import whichisgreater

def test_whichisgreater() :
    assert whichisgreater(1,19) == 0
    assert whichisgreater(4,4) == 0
    assert whichisgreater(23,14) == 1