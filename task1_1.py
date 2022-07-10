def task1(array):
    count1 = 0
    if len(array) == 1:
        array = str(array[0])
    for i in array:
        if i == 0 or i == '0':
            return count1
        count1 += 1
    else:
        return 'This element does not exist!'


if __name__ == '__main__':

    list1 = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
    list2 = '1111100000'
    list3 = [1111100000]

    print('Index of element =', task1(list1))
    print('Index of element =', task1(list2))
    print('Index of element =', task1(list3))
    print('Index of element =', task1('1111100000'))
