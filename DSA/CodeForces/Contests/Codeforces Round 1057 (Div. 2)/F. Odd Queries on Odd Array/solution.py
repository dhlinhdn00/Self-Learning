import sys

class State:
    def __init__(self, n):
        self.L = 1
        self.R = 0
        self.beauty = 0
        self.bits = [0] * ((n // 64) + 2)

    def add(self, pos, a):
        x = a[pos - 1]
        idx = x // 64
        bit = x % 64
        int_val = self.bits[idx]
        is_odd = (int_val & (1 << bit)) != 0
        if is_odd:
            self.beauty -= x
        else:
            self.beauty += x
        self.bits[idx] ^= (1 << bit)

    def del_(self, pos, a):
        self.add(pos, a)

def move_to(s, tl, tr, a):
    while s.L > tl:
        s.L -= 1
        s.add(s.L, a)
    while s.R < tr:
        s.R += 1
        s.add(s.R, a)
    while s.L < tl:
        s.del_(s.L, a)
        s.L += 1
    while s.R > tr:
        s.del_(s.R, a)
        s.R -= 1

def get_block(l, r, B, n):
    num = (n + B - 1) // B
    lb = (l - 1) // B
    rb = (r - 1) // B
    return lb * num + rb

def solve():
    data = sys.stdin.read().strip().split()
    it = iter(data)
    t = int(next(it))
    out_lines = []
    for _ in range(t):
        n = int(next(it))
        q = int(next(it))
        a = [int(next(it)) for _ in range(n)]
        B = max(1, int(n ** (2 / 3)))
        num_blocks = (n + B - 1) // B
        total_blocks = num_blocks * num_blocks
        states = [None] * total_blocks
        initialized = [False] * total_blocks
        prev = 0
        test_out = []
        for __ in range(q):
            xp = int(next(it))
            yp = int(next(it))
            x = ((xp - 1 + prev) % n) + 1
            y = ((yp - 1 + prev) % n) + 1
            l = min(x, y)
            r = max(x, y)
            block_id = get_block(l, r, B, n)
            if not initialized[block_id]:
                states[block_id] = State(n)
                move_to(states[block_id], l, r, a)
                initialized[block_id] = True
            else:
                move_to(states[block_id], l, r, a)
            ans = states[block_id].beauty
            test_out.append(str(ans))
            prev = ans
        out_lines.append(' '.join(test_out))
    sys.stdout.write('\n'.join(out_lines) + '\n')

if __name__ == "__main__":
    solve()