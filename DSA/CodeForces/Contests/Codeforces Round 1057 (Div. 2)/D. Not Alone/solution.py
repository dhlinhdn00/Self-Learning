import sys

INF = 10**18 + 5

def solve():
    data = sys.stdin.read().strip().split()
    it = iter(data)
    t = int(next(it))
    out_lines = []
    for _ in range(t):
        n = int(next(it))
        a = [int(next(it)) for _ in range(n)]
        if n == 0:
            out_lines.append('0')
            continue
        # compute runs
        runs = []
        i = 0
        while i < n:
            val = a[i]
            cnt = 0
            while i < n and a[i] == val:
                i += 1
                cnt += 1
            runs.append((cnt, val))
        if n > 0 and a[0] == a[n - 1] and len(runs) > 1:
            runs[0] = (runs[0][0] + runs[-1][0], runs[0][1])
            runs = runs[:-1]
        m_len = len(runs)
        has_good = any(l >= 2 for l, v in runs)
        ans = 0
        if not has_good:
            # all singletons, circular
            d = [abs(a[i] - a[(i + 1) % n]) for i in range(n)]
            total_d = sum(d)
            triples = [0] * n
            for i in range(n):
                vals = [a[(i + j) % n] for j in range(3)]
                triples[i] = max(vals) - min(vals)
            if n % 2 == 0:
                s_odd = sum(d[i] for i in range(0, n, 2))
                s_even = sum(d[i] for i in range(1, n, 2))
                ans = min(s_odd, s_even)
            else:
                minc = INF
                for i in range(n):
                    skip_sum = d[(i - 1) % n] + d[i] + d[(i + 1) % n] + d[(i + 2) % n]
                    paid = total_d - skip_sum
                    cc = paid + triples[i]
                    if n == 3:
                        cc = triples[i]
                    minc = min(minc, cc)
                ans = minc
        else:
            # has good runs
            ii = 0
            while ii < m_len:
                cl, cv = runs[ii]
                if cl >= 2:
                    ii += 1
                    continue
                # start chain
                chain_s = []
                start_ii = ii
                while ii < m_len and runs[ii][0] == 1:
                    chain_s.append(runs[ii][1])
                    ii += 1
                k = len(chain_s)
                if k == 0:
                    continue
                # L and R
                prev_ii = (start_ii - 1) % m_len
                L = runs[prev_ii][1]
                next_ii = ii % m_len
                R = runs[next_ii][1]
                # cum_left
                cum_left = [0] * (k + 1)
                for j in range(1, k + 1):
                    cum_left[j] = cum_left[j - 1] + abs(chain_s[j - 1] - L)
                # cum_right
                cum_right = [0] * (k + 1)
                for j in range(1, k + 1):
                    cum_right[j] = cum_right[j - 1] + abs(chain_s[k - j] - R)
                # forward dp with left special
                fdp = [INF] * (k + 1)
                fdp[0] = 0
                for pos in range(1, k + 1):
                    # special left
                    fdp[pos] = cum_left[pos]
                    # normal 2
                    if pos >= 2:
                        c2 = abs(chain_s[pos - 2] - chain_s[pos - 1])
                        fdp[pos] = min(fdp[pos], fdp[pos - 2] + c2)
                    # normal 3
                    if pos >= 3:
                        mx = max(chain_s[pos - 3], chain_s[pos - 2], chain_s[pos - 1])
                        mn = min(chain_s[pos - 3], chain_s[pos - 2], chain_s[pos - 1])
                        c3 = mx - mn
                        fdp[pos] = min(fdp[pos], fdp[pos - 3] + c3)
                # now min with right
                minc = INF
                for ii in range(k + 1):
                    qq = k - ii
                    minc = min(minc, fdp[ii] + cum_right[qq])
                ans += minc
        out_lines.append(str(ans))
    sys.stdout.write("\n".join(out_lines) + "\n")

if __name__ == "__main__":
    solve()