
# smiley_grid.py
from smiley import draw_smiley

# def main():
#     from uib_inf100_graphics.simple import canvas, display

#     draw_smiley_line(canvas, 0, 60, 5)
#     draw_smiley_line(canvas, 60, 100, 3)
#     draw_smiley_line(canvas, 160, 60, 5)

#     display(canvas)


def draw_smiley_line(canvas, y, size, n):
    for i in range(n):
        x= i*size
        draw_smiley(canvas, x, y, size)

# if __name__ == '__main__':
#     main()

def main():
    from uib_inf100_graphics.simple import canvas, display
    draw_smiley_grid(canvas, 70, 5)
    display(canvas)


def draw_smiley_grid(canvas, size, n):
        
        for i in range(n):
            y = i*size
            draw_smiley_line(canvas, y, size, n)
            
            # y = 1*size
            # draw_smiley(canvas, x, y, size)
            # y = 2*size
            # draw_smiley(canvas, x, y, size)
            # y = 3*size
            # draw_smiley(canvas, x, y, size)
            # y = 4*size
            # draw_smiley(canvas, x, y, size)
if __name__ == '__main__':
    main()