#include <iostream>
#include <vector>
#include <numeric>

class Solution {
public:
    int waysToSplitArray(std::vector<int>& nums) {
        return solverReversedLoop(nums);
    }

private:
    int solverReversedLoop(std::vector<int>& nums) {
        int count = 0;
        long long total = std::accumulate(nums.begin(), nums.end(), 0LL);

        long long reversedNumsStack = 0;
        for (int i = nums.size() - 1; i > 0; --i) {
            reversedNumsStack += nums[i];
            if (reversedNumsStack <= total - reversedNumsStack) {
                ++count;
            }
        }
        return count;
    }
};

void runTestCase(int caseNumber, std::vector<int> inputNums, int expected) {
    Solution solution;
    int result = solution.waysToSplitArray(inputNums);
    std::string status = (result == expected) ? "PASSED" : "FAILED";
    std::cout << "Case " << caseNumber
              << " - Input: { ";
    for (int num : inputNums) std::cout << num << " ";
    std::cout << "}, Output: " << result
              << ", Expected: " << expected
              << ", Status: " << status << std::endl;
}

int main() {
    std::vector<std::pair<std::vector<int>, int>> testCases = {
        {{10, 4, -8, 7}, 2},
        {{2, 3, 1, 0}, 2}
    };

    for (size_t i = 0; i < testCases.size(); ++i) {
        runTestCase(i + 1, testCases[i].first, testCases[i].second);
    }

    return 0;
}
