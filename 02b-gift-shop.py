ids = input().split(",")


def invalid(s):
    n = len(s)
    for m in range(1, n):
        if n % m != 0:
            continue
        parts = set()
        for i in range(0, n, m):
            parts.add(s[i : i + m])
        if len(parts) == 1:
            return True
    return False


ans = 0
for pair in ids:
    id1, id2 = pair.split("-")
    for i in range(int(id1), int(id2) + 1):
        if invalid(str(i)):
            ans += i
print(ans)
