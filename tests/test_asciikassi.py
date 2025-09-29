from checkio.asciikassi import asciikassi

def test_asciikassi() :
    assert asciikassi(0) == "++\n++"
    assert asciikassi(1) == "+-+\n| |\n+-+"
    assert asciikassi(2) == "+--+\n|  |\n|  |\n+--+"