from src.checkio.shandy import shandy

def test_shandy() :
    assert shandy(1,1) == 2
    assert shandy(2,1) == 2
    assert shandy(2,0) == 0
    assert shandy(61,25) == 50