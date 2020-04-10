
# printing the data as problem nested list
def print_problem(problem):
    lines = '[\n'
    for row in range(9):
        lines += '    ['
        for col in range(9):
            word = (problem[row][0][col])
            if col < 8 :
                lines += word + ', '
            elif col == 8 :
                lines += word + '],'
        lines += '\n'
    return lines
    
def dataFormat(filetxt, filepy):
    with open(filetxt, 'r') as sol:
        ls = sol.read()
        # replacing the '.' with '0' in the list
        ls = ls.replace('.', '0').split('\n')
        ls.pop()
        print(len(ls))
        with open(filepy, 'a') as fd:
            for i in range(len(ls)):
                prob0 = ls[i]
                p1 = []
                for n in range(0, 10):
                    temp = prob0[9*n:9*(n+1)]
                    p1.append([temp])
                p1.pop()
                lines = 'problem' + str(i) + '='
                data = print_problem(p1)
                lines += data + ']\n\n'
                fd.write(lines)
        
for num in range(1, 7):
    filetxt = 'problemBank0'+str(num) + '.txt'
    filepy = 'problemBank0'+str(num) + '.py'
    dataFormat(filetxt, filepy)