#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int t;
    cin >> t;
    
    for (int i = 0; i < t; ++i) {
        long long n;
        cin >> n;
        
        int bit_len = (n == 0) ? 1 : 64 - __builtin_clzll(n);
        long long ans = (1LL << bit_len) - 1;
        
        cout << ans << '\n';  
    }
    
    return 0;
}

// g++ -std=c++17 -O2 -Wall solution.cpp -o solution