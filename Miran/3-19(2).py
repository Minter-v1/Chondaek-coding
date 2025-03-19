N = int(input())
result = -1

for five_kg_count in range(N // 5, -1, -1):
    remain = N - (five_kg_count * 5)
    if remain % 3 == 0:
        three_kg_count = remain // 3
        result = five_kg_count + three_kg_count
        break

print(result)