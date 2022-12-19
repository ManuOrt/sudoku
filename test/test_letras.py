from FP_Superior_dual.David_Python.sudoku.src.checkSudoku import checkSudoku
incorrect4 = [['a','b','c'],
              ['b','c','a'],
              ['c','a','b']]

def test_letras():
    assert checkSudoku(incorrect4) is False

