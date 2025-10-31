#include <bits/stdc++.h>
using namespace std;

vector<int> parse_list(const string& s) {
    vector<int> nums;
    string num;
    for (char c : s) {
        if (isdigit(c) || c == '-') {
            num += c;
        } else if (!num.empty()) {
            nums.push_back(stoi(num));
            num.clear();
        }
    }
    if (!num.empty()) nums.push_back(stoi(num));
    return nums;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int t;
    cin >> t;
    cin.ignore(numeric_limits<streamsize>::max(), '\n'); 
    
    for (int i = 0; i < t; ++i) {
        string line;
        getline(cin, line);
        vector<int> nums = parse_list(line);

        unordered_map<int, int> freq;
        for (int num : nums) freq[num]++;

        vector<int> ans;
        for (auto& [k, v] : freq)
            if (v == 2) ans.push_back(k);

        sort(ans.begin(), ans.end());

        cout << "[";
        for (size_t j = 0; j < ans.size(); ++j) {
            cout << ans[j];
            if (j + 1 < ans.size()) cout << ", ";
        }
        cout << "]\n";
    }
    
    return 0;
}

// g++ -std=c++17 -O2 -Wall solution.cpp -o solution
// ./solution < input.txt
