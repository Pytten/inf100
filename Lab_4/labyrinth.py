
def rotate(grid, clockwise):
    grid == []
    n = len(grid)
    m = len(grid[0])
    runde = 1
    i = 0

    new_grid = []

    for _ in range(m):
        new_grid.append([])


    for rad in range(n):

        for col in range(m):
            if clockwise == True:
                new_grid[col].append(grid[n - 1 - i][col])

            if clockwise != True:
                new_grid[col].append(grid[rad][m - 1 -col])

        i +=1
        runde +=1

    return(new_grid)




if __name__ == '__main__':
    import labyrinth_test
    labyrinth_test.run_all()
