import sys

def build_spf(limit):
    spf = list(range(limit + 1))
    for i in range(2, int(limit ** 0.5) + 1):
        if spf[i] == i:
            step = i
            start = i * i
            for j in range(start, limit + 1, step):
                if spf[j] == j:
                    spf[j] = i
    return spf

def factorize_spf(x, spf):
    fac = []
    while x > 1:
        p = spf[x]
        cnt = 0
        while x % p == 0:
            x //= p
            cnt += 1
        fac.append((p, cnt))
    return fac

def gen_divisors_from_factorization(factors):
    divs = [1]
    for p, e in factors:
        cur = []
        mul = 1
        for _ in range(e + 1):
            for d in divs:
                cur.append(d * mul)
            mul *= p
        divs = cur
    return divs


class SegTree:
    def __init__(self, nmax):
        self.N = 1
        while self.N < nmax + 2:
            self.N <<= 1
        self.seg = [0] * (2 * self.N)

    def set_pos(self, pos, present):
        i = pos + self.N
        self.seg[i] = 1 if present else 0
        i //= 2
        while i:
            self.seg[i] = max(self.seg[i * 2], self.seg[i * 2 + 1])
            i //= 2

    def max_leq(self, R):
        if R <= 0:
            return 0
        res = 0
        l = self.N + 1
        r = self.N + R
        def query(node, nl, nr):
            nonlocal res
            if self.seg[node] == 0 or nr < 1 or nl > R:
                return
            if nl == nr:
                res = nl
                return
            mid = (nl + nr) // 2
            right = node * 2 + 1
            left = node * 2
            if mid + 1 <= R and self.seg[right]:
                query(right, mid + 1, nr)
                if res:
                    return
            query(left, nl, mid)
        query(1, 0, self.N - 1)
        return res


def solve():
    data = sys.stdin.read().strip().split()
    it = iter(data)
    t = int(next(it))
    tests = []
    maxA = 1
    total_n = 0
    for _ in range(t):
        n = int(next(it))
        arr = [int(next(it)) for _ in range(n)]
        tests.append(arr)
        total_n += n
        ma = max(arr) if arr else 1
        if ma > maxA:
            maxA = ma

    # SPF up to maxA
    spf = build_spf(maxA)

    out_lines = []
    for a in tests:
        n = len(a)
        cnt = {}  
        bucket_size = [0] * (n + 1)  
        seg = SegTree(n + 1)

        ans = []
        for i, x in enumerate(a, 1):
            if x == 0:
                divs = [0]
            else:
                facs = factorize_spf(x, spf)
                divs = gen_divisors_from_factorization(facs)

            for d in divs:
                old = cnt.get(d, 0)
                new = old + 1
                cnt[d] = new
                if old <= n:
                    if old >= 1:
                        bucket_size[old] -= 1
                        if bucket_size[old] == 0:
                            seg.set_pos(old, 0)
                if new <= n:
                    if new >= 1:
                        bucket_size[new] += 1
                        if bucket_size[new] == 1:
                            seg.set_pos(new, 1)

            res = seg.max_leq(i - 1)
            ans.append(str(res if res is not None else 0))

        out_lines.append(" ".join(ans))

    print("\n".join(out_lines))

if __name__ == "__main__":
    solve()
