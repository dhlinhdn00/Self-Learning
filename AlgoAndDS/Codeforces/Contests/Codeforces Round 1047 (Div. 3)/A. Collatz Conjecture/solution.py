t = int(input())
for _ in range(t):
    k, x = map(int, input().split())
    for _ in range(k):
        x *= 2
    print(x)
