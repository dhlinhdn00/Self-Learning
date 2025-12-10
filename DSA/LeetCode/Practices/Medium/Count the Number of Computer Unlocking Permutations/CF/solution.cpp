#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    static const long long MOD = 1000000007;
    
    long long factorial(int n) {
        long long result = 1;
        for (int i = 2; i <= n; i++) {
            result = (result * i) % MOD;
        };
        return result;
    }

    int countPermutations(vector<int>& complexity) {
        int n = complexity.size();
        if (n == 0) return 0;
        int root = complexity[0];
        for (int i = 1; i < n; i++) {
            if(complexity[i] <= root) {
                return 0;
            }
        }
        return factorial(n - 1);
    }

};

vector<int> parseVector(const string& s) {
    vector<int> v;
    int num = 0;
    bool in_number = false;

    for (char c : s) {
        if (isdigit(c)) {
            num = num * 10 + (c - '0');
            in_number = true;
        } else {
            if (in_number) {
                v.push_back(num);
                num = 0;
                in_number = false;
            }
        }
    }
    if (in_number) v.push_back(num);
    return v;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    if (!(cin >> t)) return 0;

    Solution sol;

    while (t--) {

        string raw_complexity;
        cin >> raw_complexity;

        vector<int> complexity = parseVector(raw_complexity);



        long long ans = sol.countPermutations(complexity);

        cout << ans << '\n';
    }

    return 0;
}
// g++ -std=c++17 -O2 -Wall solution.cpp -o solution
// ./solution < input.txt