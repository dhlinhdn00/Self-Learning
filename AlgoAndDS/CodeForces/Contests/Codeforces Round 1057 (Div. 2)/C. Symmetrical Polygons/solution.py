import sys
from collections import defaultdict
import heapq

def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    it = iter(data)
    t = next(it)
    out = []
    for _ in range(t):
        n = next(it)
        a = [next(it) for _ in range(n)]
        a.sort(reverse=True)

        s = 0                  
        odd = defaultdict(int)   
        odd_cnt = 0
        odd_sum = 0
        heap = []              

        ans = 0
        for i in range(n - 1, -1, -1):
            v = a[i]
            s += v
            if odd[v] == 0:
                odd[v] = 1
                odd_cnt += 1
                odd_sum += v
                heapq.heappush(heap, -v)
            else:
                odd[v] = 0
                odd_cnt -= 1
                odd_sum -= v

            L = n - i
            if L < 3 or s <= 2 * a[i]:
                continue

            top = []
            while heap and odd[-heap[0]] == 0:
                heapq.heappop(heap)
            if heap:
                top1 = -heap[0]
                top.append(top1)
                heapq.heappop(heap)
                while heap and odd[-heap[0]] == 0:
                    heapq.heappop(heap)
                if heap:
                    top2 = -heap[0]
                    top.append(top2)
                heapq.heappush(heap, -top1)

            odd_max1 = top[0] if len(top) >= 1 else 0
            odd_max2 = top[1] if len(top) >= 2 else 0

            candidates = []

            # u = 0
            if odd_cnt >= 0:
                r0 = odd_cnt
                if L - r0 >= 3:
                    cost0 = odd_sum
                    if s - cost0 > 2 * a[i]:
                        candidates.append(s - cost0)

            # u = 1
            if odd_cnt >= 1:
                r1 = odd_cnt - 1
                if L - r1 >= 3:
                    cost1 = odd_sum - odd_max1
                    if s - cost1 > 2 * a[i]:
                        candidates.append(s - cost1)

            # u = 2
            if odd_cnt >= 2:
                r2 = odd_cnt - 2
                if L - r2 >= 3:
                    cost2 = odd_sum - odd_max1 - odd_max2
                    if s - cost2 > 2 * a[i]:
                        candidates.append(s - cost2)

            if candidates:
                best = max(candidates)
                if best > ans:
                    ans = best

        out.append(str(ans))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()
