#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int t;
    cin >> t;
    
    while (t--) {  
        long long n;
        cin >> n;
        
        long long y, r;
        cin >> y >> r;
        
        long long redSusp = min(r, n);
        
        long long remainingPlayers = n - redSusp;
        
        long long yellowSusp = min(y / 2, remainingPlayers);
        
        long long ans = redSusp + yellowSusp;
        
        cout << ans << '\n';
    }
    
    return 0;
}
// g++ -std=c++17 -O2 -Wall solution.cpp -o solution
// ./solution < input.txt
