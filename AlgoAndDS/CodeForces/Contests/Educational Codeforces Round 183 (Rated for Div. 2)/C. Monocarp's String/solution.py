import sys

def solve():
    data = sys.stdin.read().strip().split()
    it = iter(data)
    t = int(next(it))
    out_lines = []
    for _ in range(t):
        n = int(next(it))
        s = next(it)
        total_a = s.count('a')
        total_b = n - total_a
        diff = total_b - total_a
        if diff == 0:
            ans = 0
        else:
            min_len = n
            prefix = 0
            seen = {0: 0}
            for i in range(1, n + 1):
                prefix += 1 if s[i - 1] == 'b' else -1
                needed = prefix - diff
                if needed in seen:
                    length = i - seen[needed]
                    if length < min_len:
                        min_len = length
                if prefix not in seen or i > seen[prefix]:
                    seen[prefix] = i
            ans = -1 if min_len == n else min_len
        out_lines.append(str(ans))
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    solve()