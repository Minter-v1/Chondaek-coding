N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]

matrix.sort()

for x in range(N):
    for y in range(len(matrix[x])):
        print(matrix[x][y], end = " ")
    print()