N = int(input())
word = [input() for _ in range(N)]
cnt = 0

for w in word:
    check_word = []
    check = True
    for i in range(len(w)):
        if w[i] not in check_word:
            check_word.append(w[i])
        elif w[i] in check_word and w[i-1] != w[i]:
            check = False
            break
    if check is True:
        cnt += 2

print(cnt)