#######################################
###### Q U E S T I O N - 1 ############
#######################################

desk_r = 8
desk_c = 8
a = [['.' for i in range(desk_r)] for j in range(desk_c)]
dirs = [[1,1],[1,-1],[-1,1],[-1,-1]]


x1 = int(input('position a : '))
x2 = int(input('position b : '))

for j in range(len(dirs)):
    tempx1 = x1
    tempx2 = x2
    while 0 <= tempx1 < 8 and 0 <= tempx2 < 8 :
        a[tempx1][tempx2] = 'x'
        tempx1 += dirs[j][0]
        tempx2 += dirs[j][1]
    a[x1][x2] = 'B'

print('question 1')
print('\n')
for row in a : 
    print(' '.join(map(str,row))) 


#######################################
###### Q U E S T I O N - 2 ############
#######################################


b_size = 4

def can_be_attacked(col, queens): 
    left = right = col
    for r, c in reversed(queens): 
        left, right = left-1, right+1
        if c in (left, col, right):
            return True
    return False

def solve(n):
    if n == 0: return [[]]
    solutions = solve(n-1)
    return [solution+[[n,i+1]]
        for i in range(b_size)
            for solution in solutions
                if not can_be_attacked(i+1, solution)]


for x in solve(b_size):
    board = [['.' for i in range(b_size)] for j in range(b_size)]

    for i in range (b_size) :
        for j in range (1) :
            board[ x[i][0]-1][ x[i][1]-1] = 'Q'
    
    print('---- Solution ----')
    for row in board : 
        print(' '.join(map(str,row))) 


#######################################
###### Q U E S T I O N - 3 ############
#######################################