from src.checkio.spavanac import spavanac

def test_spavanac() :
    assert spavanac(10,10) == (9,25)
    assert spavanac(0,30) == (23,45)
    assert spavanac(23,40) == (22,55)