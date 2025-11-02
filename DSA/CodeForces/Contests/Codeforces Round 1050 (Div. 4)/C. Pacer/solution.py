import sys

def solve():
    it = iter(sys.stdin.read().strip().split())
    t = int(next(it))
    out = []
    for _ in range(t):
        n = int(next(it)); m = int(next(it))
        reqs = [ (int(next(it)), int(next(it))) for __ in range(n) ]

        cur_t, cur_side = 0, 0   
        total = 0
        ok = True

        for a, b in reqs:
            L = a - cur_t               
            if L < 0:
                ok = False; break
            dist = cur_side ^ b         
            if L < dist:
                ok = False; break
            total += L - ((L - dist) & 1)
            cur_t, cur_side = a, b

        if not ok:
            out.append("0")
            continue

        total += m - cur_t
        out.append(str(total))

    print("\n".join(out))

if __name__ == "__main__":
    solve()
