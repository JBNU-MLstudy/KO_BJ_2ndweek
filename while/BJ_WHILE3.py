"""
BJ_WHILE3
더하기 사이클
"""

N = int(input())



cycle = 0
a = N
while(True):
    cycle = cycle + 1
    a = ((a//10 + a%10) % 10) + (a%10)*10 
    if a==N: break
print(cycle)