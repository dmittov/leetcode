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
    
    bool isLeaf(TreeNode* node) {
        if ((node->left == nullptr) && (node->right == nullptr)) {
            return true;
        }
        return false;
    }

public:

    bool hasPathSum(TreeNode* root, int sum) {
        if (root == nullptr) {
            return false;
        }
        if (isLeaf(root)) {
            if (sum == root->val) {
                return true;
            }
            return false;
        }
        int rest = sum - root->val;
        if (hasPathSum(root->left, rest) || hasPathSum(root->right, rest)) {
            return true;
        }
        return false;
    }
};

int main(int argc, char** argv) {
}
