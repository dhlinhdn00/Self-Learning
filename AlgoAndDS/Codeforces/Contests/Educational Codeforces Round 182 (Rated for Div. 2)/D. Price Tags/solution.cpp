#include <bits/stdc++.h>

using namespace std;

using int64 = long long;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T; 
    if (!(cin >> T)) return 0;
    while (T--) {
        int n; long long y;
        cin >> n >> y;
        vector<int> c(n);
        int Cmax = 0;
        for (int i = 0; i < n; ++i) {
            cin >> c[i];
            if (c[i] > Cmax) Cmax = c[i];
        }

        vector<int> freq(Cmax + 1, 0);
        for (int v : c) ++freq[v];

        vector<int> pre(Cmax + 1, 0);
        for (int v = 1; v <= Cmax; ++v) pre[v] = pre[v-1] + freq[v];

        long long best = LLONG_MIN;

        {
            long long sum_new = n; 
            long long overlap  = (Cmax >= 1 ? freq[1] : 0);
            long long income = - y * n + sum_new + y * overlap;
            best = max(best, income);
        }

        for (int x = 2; x <= Cmax; ++x) {
            int K = (Cmax + x - 1) / x; 
            long long sum_new = 0;
            long long overlap = 0;

            for (int k = 1; k <= K; ++k) {
                int L = (k - 1) * x + 1;
                if (L > Cmax) break;
                int R = k * x;
                if (R > Cmax) R = Cmax;

                int cnt_new_k = pre[R] - pre[L - 1];
                if (!cnt_new_k) continue;

                sum_new += 1LL * k * cnt_new_k;

                if (k <= Cmax) {
                    int f_old_k = freq[k];
                    if (f_old_k) overlap += min<long long>(cnt_new_k, f_old_k);
                }
            }
            long long income = - y * n + sum_new + y * overlap;
            if (income > best) best = income;
        }

        cout << best << "\n";
    }
    return 0;
}
