
from uib_inf100_graphics.simple import canvas, display
def point_in_rectangle(x1, y1, x2, y2, xp, yp):

    x_right = max(x1, x2)
    x_left = min(x1, x2)
    y_top = max(y1, y2)
    y_bottom = min(y1, y2)
    
    canvas.create_rectangle(x1, y1, x2, y2)
    display(canvas)
    if xp < x_left or xp > x_right or yp > y_top or yp < y_bottom:
        return(False)  
    else:
        return(True)

point_in_rectangle(x1 = int(input()),
                        y1 = int(input()),
                        x2 = int(input()),
                        y2 = int(input()),
                        xp = int(input()),
                        yp = int(input()))



def test_point_in_rectangle():
    print('Tester point_in_rectangle... ', end='')
    assert point_in_rectangle(0, 0, 5, 5, 3, 3) is True # Midt i
    assert point_in_rectangle(0, 5, 5, 0, 5, 3) is True # På kanten
    assert point_in_rectangle(0, 0, 5, 5, 6, 3) is False # Utenfor
    print('OK')

test_point_in_rectangle()