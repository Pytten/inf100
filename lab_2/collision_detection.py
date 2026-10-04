

from point_in_rectangle import point_in_rectangle
# import sys
# sys.path.append("Lab_1")
# import distance
from circles_overlap import distance

def rectangles_overlap(x1, y1, x2, y2, x3, y3, x4, y4):
    rectangle_1x = [x1, x2]
    rectangle_1y = [y1, y2]

    rectangle_2x = [x3, x4]
    rectangle_2y = [y3, y4]

    # rectangle 1 left/right
    left_rectangle_1 = min(rectangle_1x)
    right_rectangle_1 = max(rectangle_1x)

    # rektangle 2 left/right
    left_rectangle_2 = min(rectangle_2x)
    right_rectangle_2 = max(rectangle_2x)

    # rectangle 1 top/bottom
    top_rectangle_1 = min(rectangle_1y)
    bottom_rectangle_1 = max(rectangle_1y)

    # rectangle 2 top/bottom
    top_rectangle_2 = min(rectangle_2y)
    bottom_rectangle_2 = max(rectangle_2y)

    if left_rectangle_1 >= right_rectangle_2 or right_rectangle_1 >= left_rectangle_2 and top_rectangle_1 >= bottom_rectangle_2 or bottom_rectangle_1 >= top_rectangle_2:
        return (True)
    else:
        return (False)


# def test_rectangles_overlap():
#     print('Tester rectangles_overlap... ', end='')
#     assert rectangles_overlap(
#         0, 0, 5, 5, 2, 2, 6, 6) is True  # Delvis overlapp
#     assert rectangles_overlap(
#         0, 5, 5, 0, 1, 1, 4, 4) is True  # Fullstendig overlapp
#     assert rectangles_overlap(
#         0, 1, 7, 2, 1, 0, 2, 7) is True  # Kryssende rektangler
#     assert rectangles_overlap(
#         0, 5, 5, 0, 5, 5, 7, 7) is True  # Deler et hjørne
#     assert rectangles_overlap(0, 0, 5, 5, 3, 6, 5, 8) is False  # Utenfor
#     print('OK')


# test_rectangles_overlap()


def circle_overlaps_rectangle(x1, y1, x2, y2, xp, yp, rc):
    rectangle_x = [x1, x2]
    rectangle_y = [y1, y2]

    left_rectangle = min(rectangle_x)
    right_rectangle = max(rectangle_x)

    top_rectangle = min(rectangle_y)
    bottom_rectangle = max(rectangle_y)

    if point_in_rectangle(x1, y1, x2, y2, xp, yp) is True:
        return (True)

    elif not point_in_rectangle(min(x1, x2) - rc, min(y1, y2) - rc, max(x1, x2) + rc, max(y1,y2) + rc, xp, yp) is True:
        return (False)

    elif left_rectangle <= xp and xp <= right_rectangle:
        return (True)

    elif top_rectangle <= yp  and yp <= bottom_rectangle:
        return (True)

    elif distance(x1, y1, xp, yp,)**2 <= rc**2:
        return (True)

    elif distance(x2, y2, xp, yp)**2 <= rc**2:
        return (True)

    elif distance(x2, y1, xp, yp)**2 <= rc**2:
        return (True)

    elif distance(x2, y2, xp, yp)**2 <= rc**2:
        return (True)

    else:
        return(False)

# circle_overlaps_rectangle(
#     x1=float(input()),
#     y1=float(input()),
#     x2=float(input()),
#     y2=float(input()),
#     xp=float(input()),
#     yp=float(input()),
#     rc=float(input())
# )



def test_circle_overlaps_rectangle():
    print('Tester circle_overlaps_rectangle... ', end='')
    assert circle_overlaps_rectangle(
        0, 0, 5, 5, 2.5, 2.5, 2) is True  # på midten
    assert circle_overlaps_rectangle(
        0, 5, 5, 0, 8, 3, 2) is False  # langt utenfor
    assert circle_overlaps_rectangle(
        0, 0, 5, 5, 2.5, 7, 2.01) is True  # på kanten
    assert circle_overlaps_rectangle(
        0, 5, 5, 0, 5.1, 5.1, 1) is True  # på hjørnet
    assert circle_overlaps_rectangle(
        0, 0, 5, 5, 8, 8.99, 5) is True  # på hjørnet
    assert circle_overlaps_rectangle(
        0, 0, 5, 5, 8, 9.01, 5) is False  # bare nesten
    assert circle_overlaps_rectangle(
            2, 2, 5, 5, 1, 1, 2) is True
    print('OK')


test_circle_overlaps_rectangle()
