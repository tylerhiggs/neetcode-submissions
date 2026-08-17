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
 */

class Solution {
public:
    int goodNodes(TreeNode* root) {
        return dfs(root, root->val);
    }
private:
    int dfs(TreeNode* node, int val) {
        if (!node) {
            return 0;
        }
        bool is_bad = node->val < val;
        int new_val = is_bad ? val : node->val;
        int c = is_bad ? 0 : 1;
        return dfs(node->left, new_val) + dfs(node->right, new_val) + c;
    }
};
