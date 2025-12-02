ids = input().split(",")


def invalid(s):
    n = len(s)
    if len(s) % 2 == 1:
        return False
    if s[: n // 2] == s[n // 2 :]:
        return True
    return False


ans = 0
for pair in ids:
    id1, id2 = pair.split("-")
    for i in range(int(id1), int(id2) + 1):
        if invalid(str(i)):
            ans += i
print(ans)
