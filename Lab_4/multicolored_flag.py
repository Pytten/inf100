


def draw_multicolored_flag(canvas, x1, y1, x2, y2, colors):
    colors == []
    n = len(colors)
    width = x2 - x1
    i = 0
    for i in range(n):
        start_x = (width/n) *i
        end_x = (width/n) *(i+1)
        canvas.create_rectangle(x1 + start_x, y1, x1 + end_x, y2, fill= colors[i], outline = '')
        i +=1