
def draw_grid(canvas, x1, y1, x2, y2, color_grid):
    color_grid == []
    rows = len(color_grid)
    col = len(color_grid[0])
    width = x2 - x1
    height = y2 - y1
    rute_width = width / col
    rute_height = height / rows

    for row in range(rows):

        for i in range(col):
            color = color_grid[row][i]
            canvas.create_rectangle(x1 + i *rute_width,
                                    y1 + row *rute_height,
                                    x1 + (i+1)*rute_width,
                                    y1 + (row+1)*rute_height,
                                    fill = color)
