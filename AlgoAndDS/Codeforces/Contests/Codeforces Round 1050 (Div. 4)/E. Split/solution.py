import sys

def solve():
    it = iter(sys.stdin.read().strip().split())
    t = int(next(it))
    out_lines = []
    for _ in range(t):
        n = int(next(it)); k = int(next(it))
        a = [int(next(it)) for _ in range(n)]

        total = {}
        for x in a:
            total[x] = total.get(x, 0) + 1

        ok = True
        lim = {}
        for v, c in total.items():
            if c % k != 0:
                ok = False
                break
            lim[v] = c // k
        if not ok:
            out_lines.append("0")
            continue

        ans = 0
        cnt = {}
        l = 0
        for r, x in enumerate(a):
            cx = cnt.get(x, 0) + 1
            cnt[x] = cx
            while cnt[x] > lim[x]:
                y = a[l]
                cnt[y] -= 1
                if cnt[y] == 0:
                    del cnt[y]
                l += 1
            ans += (r - l + 1)
        out_lines.append(str(ans))

    print("\n".join(out_lines))

if __name__ == "__main__":
    solve()
