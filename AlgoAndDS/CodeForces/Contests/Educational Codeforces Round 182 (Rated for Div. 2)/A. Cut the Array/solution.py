import sys

def solve():
    it = iter(sys.stdin.read().strip().split())
    t = int(next(it))
    out = []
    for _ in range(t):
        n = int(next(it))
        a = [int(next(it)) for _ in range(n)]
        pre = [0]*(n+1)
        for i in range(1, n+1):
            pre[i] = (pre[i-1] + a[i-1]) % 3

        if pre[n] != 0:
            out.append("0 0")
            continue

        first_pos = [-1, -1, -1]

        ans_l = ans_r = 0

        pos_of = {0: [], 1: [], 2: []}
        for i in range(1, n):  
            pos_of[pre[i]].append(i)

        found = False
        for k in (0, 1, 2):
            two_k = (2*k) % 3
            if pos_of[k] and pos_of[two_k]:
                for l in pos_of[k]:
                    import bisect
                    arr = pos_of[two_k]
                    j = bisect.bisect_right(arr, l)
                    if j < len(arr):
                        r = arr[j]
                        if r < n:
                            ans_l, ans_r = l, r
                            found = True
                            break
                if found:
                    break

        if not found:
            first_pos = [-1, -1, -1]
            for i in range(1, n):  
                p = pre[i]
                if p == 0:
                    cand = [1, 2]
                elif p == 1:
                    cand = [0, 1]
                else:
                    cand = [0, 2]

                l = -1
                for c in cand:
                    if first_pos[c] != -1 and first_pos[c] < i:
                        l = first_pos[c]
                        break
                if l != -1:
                    ans_l, ans_r = l, i
                    found = True
                    break

                if first_pos[pre[i]] == -1:
                    first_pos[pre[i]] = i

        out.append(f"{ans_l} {ans_r}" if found else "0 0")

    print("\n".join(out))

if __name__ == "__main__":
    solve()
