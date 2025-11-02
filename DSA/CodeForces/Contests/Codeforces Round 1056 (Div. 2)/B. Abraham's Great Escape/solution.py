import sys

def solve():
    data = sys.stdin.read().strip().split()
    it = iter(data)
    t = int(next(it))
    out_lines = []
    for _ in range(t):
        n = int(next(it))
        k = int(next(it))
        m = n * n - k
        if m == 1:
            out_lines.append("NO")
            continue
        out_lines.append("YES")
        full_rows = m // n
        extra = m % n
        t_cells = set()
        if extra > 0:
            partial_r = n - full_rows - 1
            for c in range(n - extra, n):
                t_cells.add((partial_r, c))
            for r in range(partial_r + 1, n):
                for c in range(n):
                    t_cells.add((r, c))
        else:
            start_r = n - full_rows
            for r in range(start_r, n):
                for c in range(n):
                    t_cells.add((r, c))
        grid = [['' for _ in range(n)] for _ in range(n)]
        for r in range(n):
            for c in range(n):
                if (r, c) not in t_cells:
                    grid[r][c] = 'U'
        dirs = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
        prefer = ['R', 'D', 'L', 'U']
        for r in range(n):
            for c in range(n):
                if (r, c) in t_cells:
                    for d in prefer:
                        dr, dc = dirs[d]
                        nr = r + dr
                        nc = c + dc
                        if 0 <= nr < n and 0 <= nc < n and (nr, nc) in t_cells:
                            grid[r][c] = d
                            break
        for row in grid:
            out_lines.append(''.join(row))
    sys.stdout.write("\n".join(out_lines) + "\n")

if __name__ == "__main__":
    solve()