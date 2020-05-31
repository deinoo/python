import  random,time
matrix = []
def createMatrix(width, height):
    for col  in range(height):
        wiersz = []
        for row in range(width):
            if random.randint(0,1) == 1:
                wiersz.append('#')
            else:
                wiersz.append(' ')
        matrix.append(wiersz)


def updateState(matrix, width, height):
    while True:
        for column in range(width):
            for row in range(height):
                # Get neighbouring coordinates:
                # `% WIDTH` ensures leftCoord is always between 0 and WIDTH - 1
                cellCurrent = matrix[column][row]
                leftCoord = (column - 1) % width
                rightCoord = (column + 1) % width
                aboveCoord = (row - 1) % height
                belowCoord = (row + 1) % height
                #print(f'leftCoord:{leftCoord},rightCoord:{rightCoord} ,aboveCord:{aboveCoord},belowCoord:{belowCoord}')
                # Count number of living neighbors:
                aliveCount = 0
                #print(matrix[leftCoord][aboveCoord])
                if matrix[leftCoord][aboveCoord] == '#':
                    aliveCount += 1  # Top-left neighbour is alive.
                #print(matrix[column][aboveCoord])
                if matrix[column][aboveCoord] == '#':
                    aliveCount += 1  # Top neighbour is alive.
                #print(matrix[rightCoord][aboveCoord])
                if matrix[rightCoord][aboveCoord] == '#':
                    aliveCount += 1  # Top-right neighbour is alive.
                #print(matrix[leftCoord][row])
                if matrix[leftCoord][row] == '#':
                    aliveCount += 1  # Left neighbour is alive.
                #print(matrix[rightCoord][row])
                if matrix[rightCoord][row] == '#':
                    aliveCount += 1  # Right neighbour is alive.
                #print(matrix[leftCoord][belowCoord])
                if matrix[leftCoord][belowCoord] == '#':
                    aliveCount += 1  # Bottom-left neighbour is alive.
                #print(matrix[column][belowCoord])
                if matrix[column][belowCoord] == '#':
                    aliveCount += 1  # Bottom neighbour is alive.
                #print(matrix[rightCoord][belowCoord])
                if matrix[rightCoord][belowCoord] == '#':
                    aliveCount += 1  # Bottom-right neighbour is alive.

                if cellCurrent == '#':
                    if (aliveCount == 2 or aliveCount == 3):
                        continue
                    else:
                        matrix[column][row] = ' '
                        #print(f'from \'#\' to \' \'')
                else:
                    if aliveCount == 3:
                        matrix[column][row] = '#'
                        #print(f'from \' \' to \'#\'')
        printMatrix(matrix, width, height)



def printMatrix(matrix,height,width):
    for  column in range(width):
        for row in range(height):
            print (matrix[column][row], end='')
        print ('')
    time.sleep(1)  # Add a 1-second pause to reduce flickering.
    print ('\n\n\n\n\n\n')


frame = [10,10]
width, height = frame
createMatrix(height,width)
printMatrix(matrix,height,width)
updateState(matrix,height,width)