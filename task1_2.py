from math import sqrt


def square(x11, y11, x33, y33):

    a = sqrt((x11-x11)**2 + (y33 - y11)**2)
    b = sqrt((x33-x11)**2 + (y33 - y33)**2)

    print('The intersection area is equal to', a*b)
    return 'YES'


def task(x1, y1, x2, y2, x3, y3, x4, y4):

    list2 = [(x3, y3), (x4, y4), (x3, y4), (x4, y3)]

    for i in list2:
        if (x2 > i[0] > x1 and y1 > i[1] > y2) or (x1 > i[0] > x2 and y2 > i[1] > y1):
            return square(x3, y3, x2, y1)
        if x2 >= i[0] >= x1 or x1 >= i[0] >= x2:
            if i[1] == y1 or i[1] == y2:
                return 'There is a contact'
        if y2 >= i[0] >= y1 or y1 >= i[0] >= y2:
            if i[0] == x1 or i[0] == x2:
                return 'There is a contact'
    else:
        return 'NO'


if __name__ == '__main__':
    print(task(0, 2, 2, 0, 1, 1, 3, 3))
    print('_______________________')
    print(task(0, 2, 2, 0, 2, 2, 4, 4))
