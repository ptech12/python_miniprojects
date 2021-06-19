def sub(matrix, n, x):
    dp = [[0 for x in range(n + 1)]
          for y in range(n + 1)]
    for i in range(n):
        for j in range(n):
            dp[i + 1][j + 1] = matrix[i][j]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            dp[i][j] += (dp[i - 1][j] +
                         dp[i][j - 1] -
                         dp[i - 1][j - 1])
    c = 0
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            lo = 1
            hi = min(n - i, n - j) + 1
            found = False
            while (lo <= hi):
                mid = (lo + hi) // 2
                ni = i + mid - 1
                nj = j + mid - 1
                sum = (dp[ni][nj] -
                       dp[ni][j - 1] -
                       dp[i - 1][nj] +
                       dp[i - 1][j - 1])
                if (sum >= x):
                    if (sum == x):
                        found = True
                    hi = mid - 1
                else:
                    lo = mid + 1
            if (found == True):
                c += 1
    return c


n = int(input())
matrix = []
for i in range(n):
    c = []
    for j in range(n):
        j = int(input())
        c.append(j)
    matrix.append(c)
x = int(input())
print(sub(matrix, n, x))
