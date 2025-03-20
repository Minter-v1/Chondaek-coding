N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]

matrix.sort(key = lambda x : (x[1], x[0]))

for x in range(N):
    for y in range(len(matrix[x])):
        print(matrix[x][y], end = " ")
    print()