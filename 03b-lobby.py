import sys

ans = 0
for line in sys.stdin.readlines():
    n = len(line.strip())
    dp = [[0 for _ in range(13)] for _ in range(n + 1)]
    for i in range(n - 1, -1, -1):
        for j in range(0, 13):
            dp[i][j] = dp[i + 1][j]
            if j > 0:
                dp[i][j] = max(int(line[i] + str(dp[i + 1][j - 1])), dp[i][j])
    ans += dp[0][12]
print(ans // 10)
