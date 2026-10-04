
def duplicate(numbers):
    numbers == []
    i = 0
    n = len(numbers)
    for i in range(n):
        numbers[i] = numbers[i]*2
        i += 1
    


def duplicated(numbers):
    numbers == []
    numbers_2 = []
    i = 0
    n = len(numbers)
    for i in range(n):
        numbers_2.append(numbers[i]*2)
        i += 1
    return numbers_2



def duplicate_2d(grid):
    grid == []
    n = len(grid)
    i = 0

    for i in range(n):
        col = len(grid[i])
        

        for cols in range(col):
            grid[i][cols] = grid[i][cols]*2
        i +=1




def duplicated_2d(grid):
    grid == []
    grid_2 = []
    n = len(grid)
    i = 0

    for i in range(n):
        col = len(grid[i])
        grid_2.append([])
        

        for cols in range(col):
            grid_2[i].append(grid[i][cols]*2)
        i +=1
    return(grid_2)
    
