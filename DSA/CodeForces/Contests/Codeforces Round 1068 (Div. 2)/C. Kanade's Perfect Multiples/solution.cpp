#include <bits/stdc++.h>
using namespace std;

static vector<int> primes;

static void sieve_primes(int n = 31623) {
    vector<bool> isPrime(n + 1, true);
    isPrime[0] = isPrime[1] = false;
    for (int i = 2; i * 1LL * i <= n; i++) if (isPrime[i]) {
        for (int j = i * i; j <= n; j += i) isPrime[j] = false;
    }
    for (int i = 2; i <= n; i++) if (isPrime[i]) primes.push_back(i);
}

static vector<pair<int,int>> factorize_int(int x) {
    vector<pair<int,int>> f;
    int tmp = x;
    for (int p : primes) {
        if (1LL * p * p > tmp) break;
        if (tmp % p == 0) {
            int e = 0;
            while (tmp % p == 0) tmp /= p, e++;
            f.push_back({p, e});
        }
    }
    if (tmp > 1) f.push_back({tmp, 1});
    return f;
}

static void gen_divisors(const vector<pair<int,int>>& f, vector<int>& divs) {
    divs.clear();
    divs.push_back(1);
    for (auto [p, e] : f) {
        int sz = (int)divs.size();
        long long mul = 1;
        for (int i = 1; i <= e; i++) {
            mul *= p;
            for (int j = 0; j < sz; j++) {
                divs.push_back((int)(divs[j] * mul));
            }
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    sieve_primes();

    int t;
    cin >> t;

    while (t--) {
        int n;
        long long k;
        cin >> n >> k;

        vector<int> a(n);
        for (int i = 0; i < n; i++) cin >> a[i];

        vector<int> vals = a;
        sort(vals.begin(), vals.end());
        vals.erase(unique(vals.begin(), vals.end()), vals.end());
        int m = (int)vals.size();

        unordered_map<int,int> id;
        id.reserve(m * 2);
        id.max_load_factor(0.7f);
        for (int i = 0; i < m; i++) id[vals[i]] = i;

        vector<vector<pair<int,int>>> facts(m);
        for (int i = 0; i < m; i++) facts[i] = factorize_int(vals[i]);

        vector<int> cnt(m, 0);
        vector<int> divs;

        for (int i = 0; i < m; i++) {
            gen_divisors(facts[i], divs);
            for (int d : divs) {
                auto it = id.find(d);
                if (it != id.end()) cnt[it->second]++;
            }
        }

        vector<char> good(m, 0);
        for (int i = 0; i < m; i++) {
            long long need = k / vals[i];
            if (need <= m && cnt[i] == need) good[i] = 1;
        }

        vector<int> Bidx;
        for (int i = 0; i < m; i++) if (good[i]) {
            bool dominated = false;
            gen_divisors(facts[i], divs);
            for (int d : divs) {
                if (d == vals[i]) continue;
                auto it = id.find(d);
                if (it != id.end() && good[it->second]) {
                    dominated = true;
                    break;
                }
            }
            if (!dominated) Bidx.push_back(i);
        }

        if (Bidx.empty()) {
            cout << -1 << "\n";
            continue;
        }

        vector<char> inB(m, 0);
        for (int idx : Bidx) inB[idx] = 1;

        bool okAll = true;
        for (int i = 0; i < m; i++) {
            bool ok = false;
            gen_divisors(facts[i], divs);
            for (int d : divs) {
                auto it = id.find(d);
                if (it != id.end() && inB[it->second]) {
                    ok = true;
                    break;
                }
            }
            if (!ok) { okAll = false; break; }
        }

        if (!okAll) {
            cout << -1 << "\n";
            continue;
        }

        cout << (int)Bidx.size() << "\n";
        for (int idx : Bidx) cout << vals[idx] << " ";
        cout << "\n";
    }

    return 0;
}
// g++ -std=c++17 -O2 -Wall solution.cpp -o solution
// ./solution < input.txt
