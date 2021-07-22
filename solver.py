#sample sudoku board to be used

board = [ 
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

#recursive function
def solve(bo):
    find = find_empty(bo)
    if not find: #base case of the recursion
        return True #means solution has been found
    else:
        row, col = find
    
    for i in range(1,10): #loop goes through 1 to 9 inclusively
        if valid(bo, i, (row, col)): #plugs in value to board if its valid
            bo[row][col] = i 

            if solve(bo): #recursively finishes the solution by recursively calling solve into board using value added until solution is found
                return True

            bo[row][col] = 0 #backtracks to last elememt if its not correct

    return False


#function to find if the sudoku board is valid
def valid(bo, num, pos) : #parameters to consider

    for i in range(len(bo[0])): #checks the row and loops through each column
        if bo[pos[0]][i] == num and pos[1] != i: #checks if each element in the row is equal to the number added in and ignores if its the inserted position                
            return False
        
    for i in range(len(bo)): #checks the column and loops through each row (0 to 8)
        if bo[i][pos[1]] == num and pos[0] != i: #checks if each element in the column is equal to the number added in and ignores if its the inserted position
            return False
        
    #determines which box is active
    box_x = pos[1] // 3 #gives value 0, 1 or 2
    box_y = pos[0] // 3 #gives value 0, 1 or 2

    #loops through each element in the 9 boxes 
    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False #returns false if it finds a duplicate

    return True
        
def print_board(bo) : #function that gives visual presentation of the output
    for i in range(len(bo)) :
        if i % 3 == 0 and i != 0:
            print("-------------------") #prints a line after every 3rd row

        for j in range(len(bo[0])) : #checks if every position is the third element or a multiple of 3 and prints an horizontal line
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            
            if j == 8: #checks if this is the last position  
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="") #end means stay on the same line if this is the last element and position

#function to find an empty square in the board
def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])): # checks if the length is 0
            if bo[i][j] == 0:
                return (i, j) #function returns row then column
    
    return None #triggers <find>

print_board(board)
solve(board)
print(" ") #to add space between the puzzle and solution
print("The solution can be found below: ")
print_board(board)