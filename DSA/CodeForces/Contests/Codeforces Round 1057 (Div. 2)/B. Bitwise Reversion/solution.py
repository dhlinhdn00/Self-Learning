import sys

def solve():
    data = sys.stdin.read().strip().split()
    it = iter(data)
    t = int(next(it))
    out_lines = []
    for _ in range(t):
        x = int(next(it))
        y = int(next(it))
        z = int(next(it))

        valid = True
        for bit in range(31):  
            xi = (x >> bit) & 1
            yi = (y >> bit) & 1
            zi = (z >> bit) & 1
            if (xi, yi, zi) not in {(0,0,0), (0,1,0), (0,0,1), (1,0,0), (1,1,1)}:
                valid = False
                break

        out_lines.append("YES" if valid else "NO")
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    solve()
