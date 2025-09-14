import sys

def solve():
    it = iter(sys.stdin.read().strip().split())
    t = int(next(it))
    out_lines = []
    for _ in range(t):
        n = int(next(it)); m = int(next(it)); x = int(next(it)); y = int(next(it))
        for _ in range(n):
            _ = next(it)
        for _ in range(m):
            _ = next(it)
        out_lines.append(str(n + m))
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    solve()
