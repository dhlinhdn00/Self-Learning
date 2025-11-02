import sys

def fillIfOneZero(arr, n):
    seen = [False] * (n + 1)

    for x in arr:
        if 1 <= x <= n:
            seen[x] = True

    missing = [v for v in range(1, n + 1) if not seen[v]]

    mi = 0
    for i in range(n):
        if arr[i] == 0:
            arr[i] = missing[mi]
            mi += 1
    return arr


def solve():
    data = sys.stdin.read().strip().split()
    it = iter(data)
    t = int(next(it))
    out_lines = []
    for _ in range(t):
        n = int(next(it))
        arr = [int(next(it)) for _ in range(n)]
        zeros = arr.count(0)
        if zeros == 1:
            fillIfOneZero(arr, n)
        first = None
        last = None
        for i, v in enumerate(arr):
            if v != i + 1:
                if first is None:
                    first = i
                last = i
                
        ans = 0 if first is None else last - first + 1
        out_lines.append(str(ans))
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    solve()
