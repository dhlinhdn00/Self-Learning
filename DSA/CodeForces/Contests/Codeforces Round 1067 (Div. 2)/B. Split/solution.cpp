#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int t;
    cin >> t;
    
    while (t--) {  
        int n;
        cin >> n;
        
        int len = 2 * n;
        vector<int> cnt(len + 1, 0);
        for (int i = 0; i < len; ++i) {
            int x;
            cin >> x;
            cnt[x]++;
        }
        
        int s = 0;
        int g = 0;
        for (int i = 1; i <= len; ++i) {
            if (cnt[i] == 0) continue;
            if (cnt[i] & 1) s++;
            else g++;
        }
        
        int best_b = 0;
        for (int s_p = 0; s_p <= s; ++s_p) {
            int lim = min(g, min(n - s_p, n - s + s_p));
            if (lim < 0) continue;
            
            int parity = (n - s_p) & 1; 
            int b = lim;
            if ((b & 1) != parity) --b; 
            
            if (b >= 0) best_b = max(best_b, b);
        }
        
        int ans = s + 2 * best_b;
        cout << ans << '\n';
    }
    
    return 0;
}
// g++ -std=c++17 -O2 -Wall solution.cpp -o solution
// ./solution < input.txt
