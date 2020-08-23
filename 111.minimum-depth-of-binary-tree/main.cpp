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
    bool isLeaf(TreeNode* node) {
        if (node == nullptr) {
            return false;
        }
        if (node->left == nullptr && node->right == nullptr) {
            return true;
        }
        return false;
    }

public:
    
    int minDepth(TreeNode* root) {
        if (root == nullptr) {
            return 0;
        }
        int currentMinDepthEst = std::numeric_limits<int>::max();
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
            if (isLeaf(currentNodePtr)) {
                currentMinDepthEst = std::min(currentMinDepthEst, currentLevel);
            }
            nodeQueue.push_back(std::make_pair(currentNodePtr->left, currentLevel + 1));
            nodeQueue.push_back(std::make_pair(currentNodePtr->right, currentLevel + 1));
        }
        return currentMinDepthEst;
    }
};

int main(int argc, char** argv) {
}
