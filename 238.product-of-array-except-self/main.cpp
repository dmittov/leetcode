#include <vector>

class Solution {

private:

    void backwardPass(std::vector<int>* const result, const std::vector<int>& nums) {
        int current = 1;
        for (int idx = nums.size() - 1; idx >= 0; --idx) {
            result->at(idx) = current;
            current = current * nums[idx];
        }
    }

    void forwardPass(std::vector<int>* const result, const std::vector<int>& nums) {
        int current = 1;
        for (int idx = 0; idx < nums.size(); ++idx) {
            result->at(idx) = current * result->at(idx);
            current *= nums[idx];
        }
    }

public:

    std::vector<int> productExceptSelf(std::vector<int>& nums) {
        std::vector<int> result(nums.size());
        backwardPass(&result, nums);
        forwardPass(&result, nums);
        return result;
    }
};

int main(int argc, char** argv) {
}
