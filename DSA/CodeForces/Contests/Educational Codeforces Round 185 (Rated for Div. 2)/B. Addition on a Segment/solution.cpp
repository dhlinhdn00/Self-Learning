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
        
        long long S = 0;
        long long cnt_pos = 0;
        for (int i = 0; i < n; ++i) {
            long long x;
            cin >> x;
            S += x;
            if (x > 0) ++cnt_pos;
        }
        
        long long ans = min({ (long long)n, S - n + 1, cnt_pos });
        
        cout << ans << '\n';
    }
    
    return 0;
}
// g++ -std=c++17 -O2 -Wall solution.cpp -o solution
// ./solution < input.txt
