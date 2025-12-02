import sys

cur = 50
ans = 0
for line in sys.stdin.readlines():
    cmd = line[0]
    val = int(line[1:])
    for i in range(val):
        if cmd == "L":
            cur += 1
        else:
            cur -= 1
        if cur % 100 == 0:
            ans += 1
print(ans)
