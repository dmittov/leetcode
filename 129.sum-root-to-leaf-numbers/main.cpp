#include <stack>
#include <utility>

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

    using PathPtr = std::pair<TreeNode*, int>;

    bool isLeaf(const TreeNode* node) {
        if ((node->left == nullptr) && (node->right == nullptr)) {
            return true;
        }
        return false;
    }

public:

    int sumNumbers(TreeNode* root) {
        if (root == nullptr) {
            return 0;
        }
        int result = 0;
        std::stack<PathPtr> dfsStack;
        dfsStack.push(std::make_pair(root, 0));
        int stackNumber = root->val;
        while(!dfsStack.empty()) {
            auto currentPath = dfsStack.top();
            dfsStack.pop();
            TreeNode* currentNode = currentPath.first;
            if (currentNode == nullptr) {
                continue;
            }
            int number = currentPath.second * 10 + currentNode->val;
            if (isLeaf(currentNode)) {
                result += number;
            } else {
                dfsStack.push(std::make_pair(currentNode->left, number));
                dfsStack.push(std::make_pair(currentNode->right, number));
            }
        }
        return result;
    }
};

int main(int argc, char** argv) {
}
