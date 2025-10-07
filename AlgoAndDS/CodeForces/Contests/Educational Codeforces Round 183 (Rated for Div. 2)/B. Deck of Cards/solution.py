import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    out_lines = []
    for _ in range(t):
        n = int(data[idx])
        k = int(data[idx + 1])
        idx += 2
        s = data[idx]
        idx += 1
        z = s.count('0')
        o = s.count('1')
        tt = k - z - o
        min_a = z
        max_a = z + tt
        m = n - k
        if m == 0:
            ans = '-' * n
        else:
            min_l = min_a + 1
            max_l = max_a + 1
            union_left = min_l
            union_right = max_l + m - 1
            inter_left = max_l
            inter_right = min_l + m - 1
            ans_list = [''] * n
            for i in range(1, n + 1):
                if i < union_left or i > union_right:
                    ans_list[i - 1] = '-'
                elif inter_left <= i <= inter_right:
                    ans_list[i - 1] = '+'
                else:
                    ans_list[i - 1] = '?'
            ans = ''.join(ans_list)
        out_lines.append(ans)
    sys.stdout.write("\n".join(out_lines) + "\n")

if __name__ == "__main__":
    solve()