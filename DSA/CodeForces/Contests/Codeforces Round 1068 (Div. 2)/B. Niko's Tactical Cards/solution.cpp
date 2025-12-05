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
        vector<long long> a(n), b(n);
        for (int i = 0; i < n; ++i) cin >> a[i];
        for (int i = 0; i < n; ++i) cin >> b[i];
        
        long long L = 0, R = 0;
        for (int i = 0; i < n; ++i) {
            long long nL = min(L - a[i], b[i] - R);
            long long nR = max(R - a[i], b[i] - L);
            L = nL;
            R = nR;
        }
        
        long long ans = R;
        cout << ans << '\n';
    }
    
    return 0;
}
// g++ -std=c++17 -O2 -Wall solution.cpp -o solution
// ./solution < input.txt
