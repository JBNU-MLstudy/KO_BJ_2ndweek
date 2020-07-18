"""
BJ_WHILE2
A+B
"""
#EOF가 나올때 까지 덧셈을 무한 반복 하는 프로그램

try:
    while True:
        a, b = map(int, input().split())
        print(a + b)
except:
    exit()
#try-except문을 사용하여 오류가 나거나 EOF이 나오면 종료