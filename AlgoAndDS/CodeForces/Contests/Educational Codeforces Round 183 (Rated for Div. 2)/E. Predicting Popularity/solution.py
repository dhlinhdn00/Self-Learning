import sys

class Fenwick:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (size + 1)

    def update(self, idx, val):
        while idx <= self.size:
            self.tree[idx] += val
            idx += idx & -idx

    def query(self, idx):
        res = 0
        while idx > 0:
            res += self.tree[idx]
            idx -= idx & -idx
        return res

def solve():
    data = list(map(int, sys.stdin.read().strip().split()))
    it = iter(data)
    ac = next(it)
    dr = next(it)
    n = next(it)
    a = [next(it) for _ in range(n)]
    d = [next(it) for _ in range(n)]
    m = next(it)
    queries = []
    for _ in range(m):
        k = next(it) - 1
        na = next(it)
        nd = next(it)
        queries.append((k, na, nd))

    MAX = 2000010
    ft = Fenwick(MAX)

    def get_diff(ai, di):
        return max(ai - ac, 0) + max(di - dr, 0)

    for i in range(n):
        df = get_diff(a[i], d[i])
        ft.update(df + 1, 1)

    def get_p():
        low = 0
        high = n
        while low < high:
            mid = (low + high + 1) // 2
            cnt = ft.query(mid + 1)
            if cnt >= mid:
                low = mid
            else:
                high = mid - 1
        return low

    out_lines = []
    for k, na, nd in queries:
        old_df = get_diff(a[k], d[k])
        new_df = get_diff(na, nd)
        a[k] = na
        d[k] = nd
        if old_df != new_df:
            ft.update(old_df + 1, -1)
            ft.update(new_df + 1, 1)
        out_lines.append(str(get_p()))
    sys.stdout.write("\n".join(out_lines) + "\n")

if __name__ == "__main__":
    solve()