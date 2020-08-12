#include <deque>
#include <utility>
#include <algorithm>


/**
 * Definition for a binary tree node.
 */
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

public:
    
    int maxDepth(TreeNode* root) {
        if (root == nullptr) {
            return 0;
        }
        int currentDepthEst = 0;
        std::deque<TreeNodePtrWithLevel> nodeQueue;
        nodeQueue.push_back(std::make_pair(root, 1));
        while (!nodeQueue.empty()) {
            TreeNodePtrWithLevel nodePtrWithLevel = nodeQueue.front();
            nodeQueue.pop_front();
            auto currentLevel = nodePtrWithLevel.second;
            auto currentNodePtr = nodePtrWithLevel.first;
            if (currentNodePtr == nullptr) {
                continue;
            }
            currentDepthEst = std::max(currentDepthEst, currentLevel);
            nodeQueue.push_back(std::make_pair(currentNodePtr->left, currentLevel + 1));
            nodeQueue.push_back(std::make_pair(currentNodePtr->right, currentLevel + 1));
        }
        return currentDepthEst;
    }
};

int main(int argc, char** argv) {
}
