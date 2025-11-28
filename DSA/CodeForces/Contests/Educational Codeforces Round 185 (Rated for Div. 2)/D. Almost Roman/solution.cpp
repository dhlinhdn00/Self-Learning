#include <bits/stdc++.h>
using namespace std;

static inline long long seg_cost(int L, int leftBit, int rightBit, int k) {
    if (k == 0) return 0;
    int z = L - k;
    const long long INF = (long long)4e18;
    long long res = INF;

    // start=1 end=1
    res = min(res, max(0LL, 2LL * k - L - 1LL) + leftBit + rightBit);

    // start=1 end=0
    if (z >= 1) res = min(res, max(0LL, 2LL * k - L) + leftBit);

    // start=0 end=1
    if (z >= 1) res = min(res, max(0LL, 2LL * k - L) + rightBit);

    // start=0 end=0
    if (z >= 2) res = min(res, max(0LL, 2LL * k - L + 1LL));

    return res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;

    while (t--) {
        int n, q;
        cin >> n >> q;
        string s;
        cin >> s;

        long long fixedX = 0, fixedV = 0, fixedI = 0;
        int m = 0;

        // bit: 1 = (X/V), 0 = I, -1 = '?'
        vector<int> bit(n + 2);
        bit[0] = 1;       
        bit[n + 1] = 0; 

        for (int i = 1; i <= n; i++) {
            char c = s[i - 1];
            if (c == '?') {
                bit[i] = -1;
                m++;
            } else if (c == 'I') {
                bit[i] = 0;
                fixedI++;
            } else if (c == 'V') {
                bit[i] = 1;
                fixedV++;
            } else { // 'X'
                bit[i] = 1;
                fixedX++;
            }
        }

        long long fixedB = fixedX + fixedV;
        long long base_fixed = 10LL * fixedX + 5LL * fixedV + 1LL * fixedI;

        long long base_const = 0;
        for (int i = 0; i <= n - 1; i++) {
            if (bit[i] != -1 && bit[i + 1] != -1 && bit[i] == 1 && bit[i + 1] == 1) {
                base_const++;
            }
        }

        vector<int> deltas;
        deltas.reserve(m);

        for (int i = 1; i <= n; ) {
            if (bit[i] != -1) { i++; continue; }
            int l = i;
            while (i <= n && bit[i] == -1) i++;
            int r = i - 1;
            int L = r - l + 1;

            int leftBit = bit[l - 1];
            int rightBit = bit[r + 1];

            long long prev = 0;
            for (int k = 1; k <= L; k++) {
                long long cur = seg_cost(L, leftBit, rightBit, k);
                deltas.push_back((int)(cur - prev));
                prev = cur;
            }
        }

        sort(deltas.begin(), deltas.end());
        vector<long long> prefDelta(m + 1, 0);
        for (int i = 1; i <= m; i++) prefDelta[i] = prefDelta[i - 1] + deltas[i - 1];

        vector<long long> bonus(m + 1, 0);
        for (int b = 0; b <= m; b++) {
            long long minCost = base_const + prefDelta[b]; 
            long long onesTotal = fixedB + b;
            bonus[b] = onesTotal - minCost;
            if (bonus[b] < 0) bonus[b] = 0;
        }

        while (q--) {
            long long cX, cV, cI;
            cin >> cX >> cV >> cI;

            if (cX < 0 || cV < 0 || cI < 0 || cX + cV + cI < m) {
                cout << -1 << '\n';
                continue;
            }

            long long useI = min<long long>(m, cI);
            int b = (int)(m - useI);

            if (b > cX + cV) {
                cout << -1 << '\n';
                continue;
            }

            long long useV = min<long long>(b, cV);
            long long useX = b - useV;
            if (useX > cX) {
                cout << -1 << '\n';
                continue;
            }

            long long base = base_fixed + useI * 1LL + useV * 5LL + useX * 10LL;
            long long ans = base - 2LL * bonus[b];
            cout << ans << '\n';
        }
    }

    return 0;
}

// g++ -std=c++17 -O2 -Wall solution.cpp -o solution
// ./solution < input.txt
