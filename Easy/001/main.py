n = int(input())
res = 0
while n > 0:
    res += 1 if str(input()).lower() == "rayancode" else 0
    n -= 1
print(res)
