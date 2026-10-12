
def draw_board(canvas, x1, y1, x2, y2, board, info_mode):

    board == []
    rows = len(board)
    cols = len(board[0])
    width = x2 - x1
    height = y2 - y1
    rute_width = width/cols
    rute_height = height/rows

    for row in range(rows):

        for col in range(cols):
            color = get_color(board[row][col])
            canvas.create_rectangle(x1 + col*rute_width,
                                    y1 + row*rute_height,
                                    x1 + (col +1)*rute_width,
                                    y1 + (row +1)*rute_height,
                                    fill = color,
                                    )
            if info_mode == True:
                canvas.create_text((x1 +col*rute_width + x1 + (col +1)*rute_width)/2,
                                   (y1 + row*rute_height + y1 + (row +1)*rute_height)/2,
                                    text = f'{row},{col}\n{board[row][col]}')


def get_color(value):
    if value == 0:
        return('lightgray')
    if value > 0:
        return('orange')
    if value < 0:
        return('cyan')



