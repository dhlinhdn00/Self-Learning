import sys

def is_critical(x):
    if x < 2:
        return False
    y = x - 1
    return y > 1 and (y & (y - 1)) == 0

def compute_c(x):
    count = 0
    while x > 1:
        x //= 2
        count += 1
        if x > 1:
            x += 1
    return count

def solve():
    data = sys.stdin.read().strip().split()
    it = iter(data)
    t = int(next(it))
    out_lines = []
    for _ in range(t):
        n = int(next(it))
        q = int(next(it))
        a = [int(next(it)) for _ in range(n)]
        prefix_c = [0] * (n + 1)
        prefix_cnt = [0] * (n + 1)
        for i in range(1, n + 1):
            prefix_c[i] = prefix_c[i - 1] + compute_c(a[i - 1])
            prefix_cnt[i] = prefix_cnt[i - 1] + (1 if is_critical(a[i - 1]) else 0)
        for __ in range(q):
            l = int(next(it))
            r = int(next(it))
            sumc = prefix_c[r] - prefix_c[l - 1]
            cnt = prefix_cnt[r] - prefix_cnt[l - 1]
            ans = sumc + (cnt // 2)
            out_lines.append(str(ans))
    sys.stdout.write("\n".join(out_lines) + "\n")

if __name__ == "__main__":
    solve()