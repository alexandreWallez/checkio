from src.checkio.filip import filip

def test_filip() :
    assert filip("734", "893") == "437"
    assert filip("221", "231") == "132"
    assert filip("839", "237") == "938"