import sys
import ast  

def solve():
    data = sys.stdin.read().strip().splitlines()
    t = int(data[0])  
    out_lines = []

    for i in range(1, t + 1):
        nums = ast.literal_eval(data[i])

        dic = {}
        for num in nums:
            dic[num] = dic.get(num, 0) + 1

        ans = [k for k, v in dic.items() if v == 2]
        out_lines.append(str(ans))

    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    solve()