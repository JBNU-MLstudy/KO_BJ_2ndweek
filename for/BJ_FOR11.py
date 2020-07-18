"""
BJ_FOR11
X보다 작은 수
"""

N, X = map(int,input().split())
A = list(map(int,input().split())) #인풋을 받아 객체들을 리스트로 만든 뒤 int형으로 변환
for i in range(N):
    if A[i]<X:
        print(A[i])