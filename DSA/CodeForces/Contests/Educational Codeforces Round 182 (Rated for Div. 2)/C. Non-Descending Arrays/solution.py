import sys

MOD = 998244353

def solve():
    data = sys.stdin.read().strip().split()
    it = iter(data)
    t = int(next(it))
    out = []

    for _ in range(t):
        n = int(next(it))
        a = [int(next(it)) for _ in range(n)]
        b = [int(next(it)) for _ in range(n)]


        dp0 = 1 
        dp1 = 1  

        prev0 = (a[0], b[0])
        prev1 = (b[0], a[0])

        for i in range(1, n):
            cur0 = (a[i], b[i])
            cur1 = (b[i], a[i])

            ndp0 = 0
            ndp1 = 0

            if prev0[0] <= cur0[0] and prev0[1] <= cur0[1]:
                ndp0 = (ndp0 + dp0) % MOD
            if prev1[0] <= cur0[0] and prev1[1] <= cur0[1]:
                ndp0 = (ndp0 + dp1) % MOD

            if prev0[0] <= cur1[0] and prev0[1] <= cur1[1]:
                ndp1 = (ndp1 + dp0) % MOD
            if prev1[0] <= cur1[0] and prev1[1] <= cur1[1]:
                ndp1 = (ndp1 + dp1) % MOD

            dp0, dp1 = ndp0, ndp1
            prev0, prev1 = cur0, cur1

        out.append(str((dp0 + dp1) % MOD))

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()
