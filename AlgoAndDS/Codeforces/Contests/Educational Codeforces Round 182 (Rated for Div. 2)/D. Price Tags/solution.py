import sys

def solve():
    data = sys.stdin.read().strip().split()
    it = iter(data)
    t = int(next(it))
    out = []

    for _ in range(t):
        n = int(next(it)); y = int(next(it))
        c = [int(next(it)) for _ in range(n)]
        Cmax = max(c)

        freq = [0] * (Cmax + 1)
        for v in c:
            freq[v] += 1

        pre = [0] * (Cmax + 1)
        for v in range(1, Cmax + 1):
            pre[v] = pre[v-1] + freq[v]

        best = -10**30 

        for x in range(2, Cmax + 2):
            K = (Cmax + x - 1) // x  
            sum_new = 0
            overlap = 0
            for k in range(1, K + 1):
                L = (k - 1) * x + 1
                R = k * x
                if L > Cmax:
                    break
                if R > Cmax:
                    R = Cmax
                cnt_new_k = pre[R] - pre[L - 1]
                if cnt_new_k == 0:
                    continue
                sum_new += k * cnt_new_k
                if k <= Cmax:
                    f_old_k = freq[k]
                    if f_old_k:
                        overlap += min(cnt_new_k, f_old_k)

            income = - y * n + sum_new + y * overlap
            if income > best:
                best = income

        out.append(str(best))

    print("\n".join(out))

if __name__ == "__main__":
    solve()
