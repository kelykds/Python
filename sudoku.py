def find_n_empty(puzzle):
    # pega um q não tá preenchido
    # retorna
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r, c
    return None, None # não tem vazios

def is_valid(puzzle, guess, row, col):
    #ve quando a guess é valida
    # true se for, false se não

    #row
    row_val = puzzle[row]
    if guess in row_val:
        return False

    #col_val = []
    #for i in range(9):
    #    col_val.append(puzzle[i][col])

    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False

    row_start = (row // 3) * 3
    col_start = (col // 3) * 3

    for r in range(row_start, row_start+3):
        for c in range(col_start, col_start+3):
            if puzzle[r][c] == guess:
                return False

    return True
    
def resudoku(puzzle):
    #backtracking
    #list of lists -> each inner list is a row in the sudoku
    #return whether a solution exists
    
    # escolher um lugar p começar
    row, col = find_n_empty(puzzle)

    # se não tem, we're done
    if row is None:
        return True

    # se tem, fazer uma tentativa entre 1 e 9
    for guess in range(1,10):
        #é válido?
        if is_valid(puzzle, guess, row, col):
            puzzle[row][col] = guess
            #recurse
            if resudoku(puzzle):
                return True
        #backtrack se der errado
        puzzle[row][col] = -1

    return False