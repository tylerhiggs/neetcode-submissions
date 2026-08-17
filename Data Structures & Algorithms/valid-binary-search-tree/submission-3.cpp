/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 *          0
 *         / \
 *     -1000  1000
 */

class Solution {
public:
    bool isValidBST(TreeNode* root) {
        return valid(root, nullopt, nullopt);
    }
private:
    bool valid(TreeNode* node, optional<int> low, optional<int> high) {
        if (!node) {
            return true;
        }
        return (!low.has_value() || node->val > low) && (!high.has_value() || node->val < high) && valid(node->left, low, node->val) && valid(node->right, node->val, high);
    }
};
