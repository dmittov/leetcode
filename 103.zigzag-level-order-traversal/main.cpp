#include <vector>
#include <deque>
#include <utility>
#include <map>
#include <algorithm>

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};
 
class Solution {

private:

    using TreeNodePtrWithLevel = std::pair<TreeNode*, int>;

    void zigzagTreeStorage(std::vector<std::vector<int>>* const treeStoragePtr) {
        for (int level = 0; level < treeStoragePtr->size(); ++level) {
            if (level % 2 == 0) {
                continue;
            }
            auto& levelStorage = treeStoragePtr->at(level);
            std::reverse(levelStorage.begin(), levelStorage.end());
        }
    }

public:

    std::vector<std::vector<int>> zigzagLevelOrder(TreeNode* root) {
        std::vector<std::vector<int>> treeStorage;
        std::deque<TreeNodePtrWithLevel> nodeBFSQueue;
        nodeBFSQueue.push_back(std::make_pair(root, 0));
        while (!nodeBFSQueue.empty()) {
            auto current = nodeBFSQueue.front();
            nodeBFSQueue.pop_front();
            auto treeNodePtr = current.first;
            if (treeNodePtr == nullptr) {
                continue;
            }
            auto level = current.second;
            if (treeStorage.size() < level + 1) {
                treeStorage.push_back({});
            }
            treeStorage[level].push_back(treeNodePtr->val);
            nodeBFSQueue.push_back(std::make_pair(treeNodePtr->left, level + 1));
            nodeBFSQueue.push_back(std::make_pair(treeNodePtr->right, level + 1));
        }
        zigzagTreeStorage(&treeStorage);
        return treeStorage;
    }
};

int main(int argc, char** argv) {
}
