from checkio import asciikassi

def test_asciikassi() :
    assert asciikassi.asciikassi(0) == "++\n++"
    assert asciikassi.asciikassi(1) == "+-+\n| |\n+-+"
    assert asciikassi.asciikassi(2) == "+--+\n|  |\n|  |\n+--+"