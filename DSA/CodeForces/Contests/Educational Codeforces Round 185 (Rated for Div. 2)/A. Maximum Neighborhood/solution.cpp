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
        
        long long ans;
        if (n == 1)      ans = 1;
        else if (n == 2) ans = 9;
        else if (n == 3) ans = 29;
        else if (n == 4) ans = 56;
        else             ans = 5 * (n * n - n - 1);
        
        cout << ans << '\n';
    }
    
    return 0;
}
// g++ -std=c++17 -O2 -Wall solution.cpp -o solution
// ./solution < input.txt
