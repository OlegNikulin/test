import copy


def appearance(intervals):
    list_lesson = copy.deepcopy(intervals['lesson'])
    list_student = copy.deepcopy(intervals['pupil'])
    list_teacher = copy.deepcopy(intervals['tutor'])
    if list_student[0] < list_lesson[0]:
        list_student[0] = list_lesson[0]
    elif list_student[-1] > list_lesson[1]:
        list_student[-1] = list_lesson[1]
    if list_teacher[0] < list_lesson[0]:
        list_teacher[0] = list_lesson[0]
    elif list_teacher[-1] > list_lesson[1]:
        list_teacher[-1] = list_lesson[1]
    student_even = sum([list_student[i1] for i1 in range(len(list_student)) if i1 % 2 == 0])
    student_odd = sum([list_student[i1] for i1 in range(len(list_student)) if i1 % 2 != 0])
    teacher_even = sum([list_teacher[i1] for i1 in range(len(list_teacher)) if i1 % 2 == 0])
    teacher_odd = sum([list_teacher[i1] for i1 in range(len(list_teacher)) if i1 % 2 != 0])
    return (teacher_odd - teacher_even) + (student_odd-student_even)


tests = [
    {'data': {'lesson': [1594663200, 1594666800],
              'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
              'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
     'answer': 3117
     },
    {'data': {'lesson': [1594702800, 1594706400],
              'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150,
                        1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480,
                        1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503,
                        1594706524, 1594706524, 1594706579, 1594706641],
              'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
     'answer': 3577
     },
    {'data': {'lesson': [1594692000, 1594695600],
              'pupil': [1594692033, 1594696347],
              'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
     'answer': 3565
     },
]

if __name__ == '__main__':

    for i, test in enumerate(tests):
        print(appearance(test['data']))


