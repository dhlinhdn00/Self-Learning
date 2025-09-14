import sys

def solve():
    it = iter(sys.stdin.read().strip().split())
    t = int(next(it))
    out = []
    for _ in range(t):
        n = int(next(it))
        a = [int(next(it)) for _ in range(n)]
        evens_sum = sum(x for x in a if x % 2 == 0)
        odds = [x for x in a if x % 2 == 1]
        if not odds:
            out.append("0")
            continue
        odds.sort(reverse=True)
        take = (len(odds) + 1) // 2
        ans = evens_sum + sum(odds[:take])
        out.append(str(ans))
    print("\n".join(out))

if __name__ == "__main__":
    solve()
