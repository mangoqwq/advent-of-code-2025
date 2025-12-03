import sys

ans = 0
for line in sys.stdin.readlines():
    best = 0
    n = len(line.strip())
    for i in range(0, n):
        for j in range(i + 1, n):
            best = max(best, int(line[i] + line[j]))
    ans += best
print(ans)
