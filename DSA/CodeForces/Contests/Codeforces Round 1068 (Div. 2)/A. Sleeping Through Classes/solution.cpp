#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int t;
    cin >> t;
    
    while (t--) {  
        int n, k;
        cin >> n >> k;
        
        string s;
        cin >> s;
        
        long long ans = 0;      
        int awake_limit = -1;   
        
        for (int i = 0; i < n; ++i) {
            if (s[i] == '1') {
                awake_limit = max(awake_limit, i + k);
            } else {
                if (i > awake_limit) {
                    ans++;
                }
            }
        }
        
        cout << ans << '\n';
    }
    
    return 0;
}
// g++ -std=c++17 -O2 -Wall solution.cpp -o solution
// ./solution < input.txt
