import sys

def solve():
    data = list(map(int, sys.stdin.read().strip().split()))
    if not data:
        return
    t = data[0]
    out = []
    i = 1
    for _ in range(t):
        x = data[i]; n = data[i + 1]; i += 2
        out.append(str(x if (n & 1) else 0))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()
