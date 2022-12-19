from FP_Superior_dual.David_Python.sudoku.src.checkSudoku import checkSudoku
irregular = [[1,2,3],
             [2,3,1]]

irregular2 = [[1,2,3],
             [2,3,1],
             [3,1]]

def test_incompletos():
    assert checkSudoku(irregular) is False

def test_incompletos2():
    assert checkSudoku(irregular2) is False