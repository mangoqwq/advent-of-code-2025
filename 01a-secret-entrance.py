import sys

cur = 50
ans = 0
for line in sys.stdin.readlines():
    cmd = line[0]
    val = int(line[1:])
    if cmd == "L":
        cur += val
    else:
        cur -= val
    if cur % 100 == 0:
        ans += 1
print(ans)
