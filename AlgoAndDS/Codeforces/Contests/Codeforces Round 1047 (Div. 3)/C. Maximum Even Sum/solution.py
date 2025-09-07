import sys

t = int(sys.stdin.readline())
for _ in range(t):
    a, b = map(int, sys.stdin.readline().split())
    if b % 2 == 1:
        print(-1 if a % 2 == 0 else a*b + 1)
    else:
        # v2(b)
        t2 = (b & -b).bit_length() - 1  
        if a % 2 == 1 and t2 == 1:
            print(-1)
        else:
            print(a*(b//2) + 2)
