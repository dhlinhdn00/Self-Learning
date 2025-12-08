#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int countTriples(int n) {
        int count = 0;

        for (int a = 1; a <= n; ++a) {
            for (int b = 1; b <= n; ++b) {
                int c2 = a * a + b * b;
                int c = (int)std::sqrt(c2);

                if (c <= n && c * c == c2) {
                    count ++;
                }
            }
        }
        return count;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    if (!(cin >> t)) return 0;
    
    Solution solver;

    while (t--) {

        long long n;
        cin >> n;

        long long ans = solver.countTriples(n);

        cout << ans << '\n';
    }

    return 0;
}
// g++ -std=c++17 -O2 -Wall solution.cpp -o solution
// ./solution < input.txt