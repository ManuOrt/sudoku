from FP_Superior_dual.David_Python.sudoku.src.checkSudoku import checkSudoku

incorrect5 = [[1, 1.5],
               [1.5, 1]]

def test_decimal():
    assert checkSudoku(incorrect5) is False