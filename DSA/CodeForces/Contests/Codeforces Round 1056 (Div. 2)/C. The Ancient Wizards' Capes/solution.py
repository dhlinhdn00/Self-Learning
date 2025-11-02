import sys

def solve():
    data = sys.stdin.read().strip().split()
    it = iter(data)
    t = int(next(it))
    out_lines = []
    MOD = 676767677
    for _ in range(t):
        n = int(next(it))
        p = [int(next(it)) for _ in range(n)]
        ans = 0
        if n == 1:
            if p[0] == 1:
                ans = 2
            out_lines.append(str(ans % MOD))
            continue
        d = [p[i + 1] - p[i] + 1 for i in range(n - 1)]
        for choice in [0, 1]:
            x = [0] * n
            x[0] = choice
            valid = True
            for i in range(n - 1):
                nextx = d[i] - x[i]
                if nextx not in (0, 1):
                    valid = False
                    break
                x[i + 1] = nextx
            if valid:
                sumx = sum(x)
                comp_a1 = n - sumx + x[0]
                if comp_a1 == p[0]:
                    ans += 1
        out_lines.append(str(ans % MOD))
    sys.stdout.write("\n".join(out_lines) + "\n")

if __name__ == "__main__":
    solve()