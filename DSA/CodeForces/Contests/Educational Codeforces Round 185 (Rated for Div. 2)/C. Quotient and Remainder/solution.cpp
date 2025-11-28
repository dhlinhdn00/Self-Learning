#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int T;
    cin >> T;
    
    while (T--) {
        int n;
        long long k;
        cin >> n >> k;
        
        vector<long long> q(n), r(n);
        for (int i = 0; i < n; ++i) {
            cin >> q[i];
        }
        for (int i = 0; i < n; ++i) {
            cin >> r[i];
        }
        
        vector<long long> caps;
        caps.reserve(n);
        
        for (int i = 0; i < n; ++i) {
            long long t = q[i];
            if (t > k) continue; 
            
            long long cap = (k - t) / (t + 1); // cap = floor((k - t)/(t+1))
            if (cap >= 1) {
                caps.push_back(cap);
            }
        }
        
        vector<long long> rems;
        rems.reserve(n);
        for (int i = 0; i < n; ++i) {
            long long x = r[i];
            if (x < k) { // remainder < x <= k => r < k
                rems.push_back(x);
            }
        }
        
        sort(caps.begin(), caps.end());
        sort(rems.begin(), rems.end());
        
        long long ans = 0;
        int j = 0; 
        
        for (long long cap : caps) {
            if (j >= (int)rems.size()) break;
            
            if (rems[j] <= cap) {
                ++ans;
                ++j;
            } 
        }
        
        cout << ans << '\n';
    }
    
    return 0;
}
// g++ -std=c++17 -O2 -Wall solution.cpp -o solution
// ./solution < input.txt
