#include <bits/stdc++.h>
using namespace std;

static inline bool isPal(const string &s, int l, int r) {
    while (l < r) if (s[l++] != s[r--]) return false;
    return true;
}

static inline void flipRange(string &s, int l, int r) {
    for (int i = l; i <= r; ++i) s[i] = (s[i] == '0' ? '1' : '0');
}

// Return ops (0-indexed) to transform s -> all '0' in <= n ops (n>=4).
vector<pair<int,int>> toZero(string s) {
    int n = (int)s.size();
    vector<pair<int,int>> ops;

    // Greedy clean positions [0 .. n-5]
    for (int i = 0; i <= n - 5; ++i) {
        if (s[i] == '0') continue;

        if (s[i+1] == '1') {                 // "11"
            // flip [i, i+1]
            ops.push_back({i, i+1});
            flipRange(s, i, i+1);
        } else if (s[i+2] == '1') {          // "101"
            // flip [i, i+2]
            ops.push_back({i, i+2});
            flipRange(s, i, i+2);
        } else {                              // "100"
            // flip "00" at [i+1, i+2] -> "11"
            ops.push_back({i+1, i+2});
            flipRange(s, i+1, i+2);
            // now [i, i+1] is "11", flip it -> "00"
            ops.push_back({i, i+1});
            flipRange(s, i, i+1);
        }
        // now s[i] is guaranteed '0'
    }

    // Solve last 4 bits with BFS on 16 states
    int base = n - 4;
    string start = s.substr(base, 4);
    const string goal = "0000";

    auto encode = [&](const string &x) {
        int m = 0;
        for (int i = 0; i < 4; ++i) m = (m << 1) | (x[i] - '0');
        return m;
    };
    auto decode = [&](int m) {
        string x(4, '0');
        for (int i = 3; i >= 0; --i) { x[i] = char('0' + (m & 1)); m >>= 1; }
        return x;
    };

    vector<int> pre(16, -1);
    vector<pair<int,int>> preOp(16, {-1,-1});
    queue<int> q;

    int st = encode(start), gl = encode(goal);
    pre[st] = st;
    q.push(st);

    while (!q.empty() && pre[gl] == -1) {
        int cur = q.front(); q.pop();
        string x = decode(cur);

        for (int l = 0; l < 4; ++l) for (int r = l + 1; r < 4; ++r) {
            if (!isPal(x, l, r)) continue;
            string y = x;
            for (int i = l; i <= r; ++i) y[i] = (y[i] == '0' ? '1' : '0');
            int nxt = encode(y);
            if (pre[nxt] == -1) {
                pre[nxt] = cur;
                preOp[nxt] = {l, r};
                q.push(nxt);
            }
        }
    }

    // Should always be reachable for n>=4 (but keep safe)
    if (pre[gl] == -1) return {}; // indicates failure (won't happen)

    vector<pair<int,int>> tail;
    for (int cur = gl; cur != st; cur = pre[cur]) tail.push_back(preOp[cur]);
    reverse(tail.begin(), tail.end());

    for (auto [l, r] : tail) {
        ops.push_back({base + l, base + r});
        flipRange(s, base + l, base + r);
    }

    return ops;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T; cin >> T;
    while (T--) {
        int n; cin >> n;
        string s, t;
        cin >> s >> t;

        // Always solvable for n>=4 with this operation set.
        auto opsS = toZero(s);
        auto opsT = toZero(t);

        vector<pair<int,int>> ans = opsS;
        for (int i = (int)opsT.size() - 1; i >= 0; --i)
            ans.push_back(opsT[i]);

        if ((int)ans.size() > 2 * n) {
            cout << -1 << "\n"; // safety (shouldn't happen)
            continue;
        }

        cout << ans.size() << "\n";
        for (auto [l, r] : ans) cout << (l + 1) << " " << (r + 1) << "\n";
    }
}

// g++ -std=c++17 -O2 -Wall solution.cpp -o solution
// ./solution < input.txt