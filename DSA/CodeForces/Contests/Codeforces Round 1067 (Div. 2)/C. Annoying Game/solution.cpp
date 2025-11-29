#include <bits/stdc++.h>
using namespace std;

long long kadane(const vector<long long>& a) {
    long long best = a[0], cur = a[0];
    for (int i = 1; i < (int)a.size(); ++i) {
        cur = max(a[i], cur + a[i]);
        best = max(best, cur);
    }
    return best;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t; 
    cin >> t;
    while (t--) {
        int n;
        long long k;
        cin >> n >> k;

        vector<long long> a(n), b(n);
        for (auto &x : a) cin >> x;
        for (auto &x : b) cin >> x;

        long long base = kadane(a);
        if (k % 2 == 0) {
            cout << base << '\n';
            continue;
        }

        vector<long long> end(n), start(n);

        end[0] = a[0];
        for (int i = 1; i < n; ++i) end[i] = max(a[i], end[i - 1] + a[i]);

        start[n - 1] = a[n - 1];
        for (int i = n - 2; i >= 0; --i) start[i] = max(a[i], start[i + 1] + a[i]);

        long long ans = base;
        for (int i = 0; i < n; ++i) {
            long long left = (i > 0 ? max(0LL, end[i - 1]) : 0LL);
            long long right = (i + 1 < n ? max(0LL, start[i + 1]) : 0LL);
            ans = max(ans, left + (a[i] + b[i]) + right);
        }

        cout << ans << '\n';
    }
}

// g++ -std=c++17 -O2 -Wall solution.cpp -o solution
// ./solution < input.txt