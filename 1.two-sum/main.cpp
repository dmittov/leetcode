# include <vector>
# include <map>

using std::vector;
using std::map;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int, int> viewed;
        vector<int> result;
        for (int i = 0; i < nums.size(); ++i) {
            auto odd = target - nums[i];
            auto found_it = viewed.find(odd);
            if (found_it != viewed.end()) {
                result.push_back(found_it->second);
                result.push_back(i);
                return result;
            }
            viewed[nums[i]] = i;
        }
        return result;
    }
};
