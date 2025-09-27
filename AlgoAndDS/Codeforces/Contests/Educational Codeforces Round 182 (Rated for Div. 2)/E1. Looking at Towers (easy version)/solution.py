import sys
MOD = 998244353

def solve():
    it = iter(sys.stdin.read().strip().split())
    t = int(next(it))
    out = []
    for _ in range(t):
        n = int(next(it))
        a = [int(next(it)) for _ in range(n)]

        Lpos = []
        mx = -1
        for i in range(n):
            if a[i] > mx:
                mx = a[i]
                Lpos.append(i)

        Rpos = []
        mx = -1
        for i in range(n-1, -1, -1):
            if a[i] > mx:
                mx = a[i]
                Rpos.append(i)
        Rpos = Rpos[::-1]

        mandatory = set(Lpos) | set(Rpos)

        pref = [0]*n
        mx = -1
        for i in range(n):
            mx = max(mx, a[i])
            pref[i] = mx
        suff = [0]*n
        mx = -1
        for i in range(n-1, -1, -1):
            mx = max(mx, a[i])
            suff[i] = mx

        safe = 0
        for i in range(n):
            if i in mandatory: 
                continue
            if a[i] <= pref[i-1] and a[i] <= suff[i+1]:
                safe += 1

        out.append(str(pow(2, safe, MOD)))
    print("\n".join(out))

if __name__ == "__main__":
    solve()
