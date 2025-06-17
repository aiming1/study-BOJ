import sys

input = sys.stdin.readline

cube = [0] + list(map(int, input().split()))
''' 5678이 앞면, 1234가 윗면임을 상정 '''

def is_it_same_color(obj):
    test = list()
    for i in range(len(obj)):
        test.append(cube[obj[i]])
    if len(set(test)) == 1:
        return True
    return False


def is_it_same_sequence(obj1, obj2):
    """ left 90 """
    if is_it_same_color(obj1[2:4] + obj2[:2]) and \
        is_it_same_color(obj1[4:6] + obj2[2:4]) and \
        is_it_same_color(obj1[6:8] + obj2[4:6]) and \
        is_it_same_color(obj1[:2] + obj2[6:8]):
            return True

    ''' right 90 '''
    if is_it_same_color(obj1[:2] + obj2[2:4]) and \
        is_it_same_color(obj1[2:4] + obj2[4:6]) and \
        is_it_same_color(obj1[4:6] + obj2[6:8]) and \
        is_it_same_color(obj1[6:8] + obj2[:2]):
        return True

    return False


''' main '''
def main():
    ''' case 1 '''
    if is_it_same_color([1, 2, 3, 4]) and is_it_same_color([9, 10, 11, 12]):
        if is_it_same_sequence([13, 14, 5, 6, 17, 18, 21, 22], [15, 16, 7, 8, 19, 20, 23, 24]):
            return 1

    ''' case 2 '''
    if is_it_same_color([5, 6, 7, 8]) and is_it_same_color([21, 22, 23, 24]):
        if is_it_same_sequence([3, 4, 17, 19, 10, 9, 16, 14], [1, 2, 18, 20, 12, 11, 15, 13]):
            return 1

    ''' case 3 '''
    if is_it_same_color([13, 14, 15, 16]) and is_it_same_color([17, 18, 19, 20]):
        if is_it_same_sequence([5, 7, 9, 11, 24, 22, 1, 3], [6, 8, 10, 12, 23, 21, 2, 4]):
            return 1

    return 0


print(main())
