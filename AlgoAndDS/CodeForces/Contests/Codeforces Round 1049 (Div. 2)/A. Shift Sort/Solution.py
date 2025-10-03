import sys

it = iter(sys.stdin.read().strip().split())
t = int(next(it))
out_lines = []
for _ in range(t):
    n = int(next(it))         
    s = list(next(it).strip())
    z = s.count('0')
    m = sum(1 for ch in s[:z] if ch == '1')
    out_lines.append(str(m))
sys.stdout.write("\n".join(out_lines))