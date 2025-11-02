import sys

def solve():
    data = list(map(int, sys.stdin.read().strip().split()))
    it = iter(data)
    t = next(it)
    out = []

    for _ in range(t):
        n = next(it)
        k = next(it)

        max_val = 0
        for i in range(1, n):
            for j in range(i + 1, n + 1):
                max_val += i * (n - j + 1)

        if k > max_val:
            out.append("0")
            continue

        if k == 0:
            out.append(" ".join(map(str, range(1, n + 1))))
            continue

        p = list(range(1, n + 1))
        cur_val = 0

        for i in range(n - 1, -1, -1):
            added = 0
            for j in range(i, n):
                p[i:j+1] = reversed(p[i:j+1])
                new_val = 0
                inv_pairs = [(x, y) for x in range(n) for y in range(x + 1, n) if p[x] > p[y]]
                for (x, y) in inv_pairs:
                    new_val += (x + 1) * (n - y)
                if new_val == k:
                    added = 1
                    break
                if new_val < k:
                    cur_val = new_val
                else:
                    p[i:j+1] = reversed(p[i:j+1])
                    break
            if added:
                break

        out.append(" ".join(map(str, p)))

    print("\n".join(out))

if __name__ == "__main__":
    solve()
