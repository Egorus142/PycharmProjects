marks = map(int, input().split())
cntMarks = [0] * 101


def CountSort(A):
    for mark in marks:
        cntMarks[mark] += 1
    for nowMark in range(101):
        print((str(nowMark) + ' ') * cntMarks[nowMark], end='')


CountSort(marks)
