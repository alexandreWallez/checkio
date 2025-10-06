from src.checkio.cutthenegativity import cutthenegativity

def test_cutthenegativity() :
    assert cutthenegativity(4,[[-1, 1, -1, 2],[9 ,-1 ,-1 ,-1],[-1 ,3 ,-1 ,4],[7 ,1 ,2, -1]]) == "8\n1 2 1\n1 4 2\n2 1 9\n3 2 3\n3 4 4\n4 1 7\n4 2 1\n4 3 2\n"
    assert cutthenegativity(3,[[-1, -1 ,-1],[15 ,-1 ,-1],[2, 2, -1]]) == "3\n2 1 15\n3 1 2\n3 2 2\n"