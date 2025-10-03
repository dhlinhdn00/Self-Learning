import sys

def solve():
    data = sys.stdin.read().strip().split()
    it = iter(data)
    t = int(next(it))
    out_lines = []
    for _ in range(t):
        n = int(next(it))
        rk = int(next(it))
        ck = int(next(it))
        rd = int(next(it))
        cd = int(next(it))
        dr = abs(rk - rd)
        dc = abs(ck - cd)
        # escape row (vertical)
        if dr > 0:
            room_r = n - rk if rk > rd else rk
            load_r = dr + room_r
            time_r = max(load_r, dc)
        else:
            time_r = dc
        # escape col (horizontal)
        if dc > 0:
            room_c = n - ck if ck > cd else ck
            load_c = dc + room_c
            time_c = max(load_c, dr)
        else:
            time_c = dr
        ans = max(time_r, time_c)
        out_lines.append(str(ans))
    sys.stdout.write("\n".join(out_lines) + "\n")

if __name__ == "__main__":
    solve()