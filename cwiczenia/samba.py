A = [1,0,1,0,1,1]


def solution(A):
    A = [0, 1, 1, 0]
    flips = 0
    for i in range(len(A)-1):
            if A[i] == A[i+1]:
                flips += 1
    print(flips)


solution(A)