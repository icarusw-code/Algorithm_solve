TC = int(input())

for t in range(1, TC+1):
    n = int(input())
    result = []
    for i in range(n):
        temp = []
        for j in range(i+1):
            if j == 0 or j == i:
                temp.append(1)
            else:
                temp.append(result[i-1][j] + result[i-1][j-1])
        result.append(temp)

    print(f"#{t} ")
    for i in result:
        print(*i)
