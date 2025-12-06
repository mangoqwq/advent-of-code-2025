import sys

g = [line.strip() for line in sys.stdin.readlines()]
n, m = len(g), len(g[0])


def within(i: int, j: int) -> bool:
    return 0 <= i < n and 0 <= j < m


def adj(i: int, j: int) -> int:
    res = 0
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            ni, nj = i + dx, j + dy
            if within(ni, nj) and g[ni][nj] == "@":
                res += 1
    return res


ans = 0
for i in range(n):
    for j in range(m):
        if g[i][j] == "@" and adj(i, j) < 4:
            ans += 1
print(ans)
