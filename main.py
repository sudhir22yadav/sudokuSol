import problemBank02 as pb


# Reference Sudoku problem https://www.websudoku.com/?level=1&set_id=890454051
problem = [
    [4, 0, 0, 0, 0, 0, 8, 0, 5],
    [0, 3, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 7, 0, 0, 0, 0, 0],
    [0, 2, 0, 0, 0, 0, 0, 6, 0],
    [0, 0, 0, 0, 8, 0, 4, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 6, 0, 3, 0, 7, 0],
    [5, 0, 0, 2, 0, 0, 0, 0, 0],
    [1, 0, 4, 0, 0, 0, 0, 0, 0], 
]

#problem = pb.problem1
def print_problem(problem):
    lines = ''
    for row in range(9):
        for col in range(9):
            word = str(problem[row][col])
            lines += word + ' '
            if col ==2 or col == 5:
                lines += '| '
        if row == 2 or row ==5 or row == 8:
            lines += '\n------+-------+------'
        lines += '\n'
    print(lines)


def check_field(problem):
    for row in range(9):
        for col in range(9):
            if problem[row][col] == 0:
                return row, col
    return None


def validity(row, col, num):
    # checking if num exists in the row or column corresponding to our field
    for i in range(9):
        if problem[i][col] == num:
            return False
        for i in range(9):
            if problem[row][i] == num:
                return False
    # checking if num exists the square
    
    r0 = row//3*3
    c0 = col//3*3
    for i in range(3):
        for j in range(3):
            if problem[r0+i][c0+j] == num:
                return False
    return True
    '''
    if row < 3:
        if col < 3:
            for i in range(3):
                for j in range(3):
                    if problem[i][j] == num:
                        return False
        elif col > 2 or col < 6:
            for i in range(3, 6):
                for j in range(3, 6):
                    if problem[i][j] == num:
                        return False
        elif col > 5:
            for i in range(6, 9):
                for j in range(6, 9):
                    if problem[i][j] == num:
                        return False
    elif row > 2 or row < 6:
        if col < 3:
            for i in range(3):
                for j in range(3):
                    if problem[i][j] == num:
                        return False
        elif col > 2 or col < 6:
            for i in range(3, 6):
                for j in range(3, 6):
                    if problem[i][j] == num:
                        return False
        elif col > 5:
            for i in range(6, 9):
                for j in range(6, 9):
                    if problem[i][j] == num:
                        return False
    elif row > 5:
        if col < 3:
            for i in range(3):
                for j in range(3):
                    if problem[i][j] == num:
                        return False
        elif col > 2 or col < 6:
            for i in range(3, 6):
                for j in range(3, 6):
                    if problem[i][j] == num:
                        return False
        elif col > 5:
            for i in range(6, 9):
                for j in range(6, 9):
                    if problem[i][j] == num:
                        return False
'''

def solution(problem):
    #print_problem(problem)
    if not check_field(problem):
        return True
    else:
        row, col = check_field(problem)
    
    for num in range(1, 10):
        if validity(row, col, num):
            problem[row][col] = num
            if solution(problem):
                return True
            problem[row][col] = 0
    return False
    

print_problem(problem)
solution(problem)
print('solution below \n')
print_problem(problem)
