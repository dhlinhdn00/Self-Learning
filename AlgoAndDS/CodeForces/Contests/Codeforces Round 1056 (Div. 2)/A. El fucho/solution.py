import sys

def solve():
    data = sys.stdin.read().strip().split()
    it = iter(data)
    t = int(next(it))
    out_lines = []
    for _ in range(t):
        num = int(next(it))

        ans = (num - 1) * 2 

        out_lines.append(str(ans))
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    solve()
