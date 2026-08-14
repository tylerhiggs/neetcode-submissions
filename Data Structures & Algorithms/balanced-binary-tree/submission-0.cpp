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
    bool isBalanced(TreeNode* root) {
        return help(root) != -1;
    }
private:
    int help(TreeNode* root) {
        if (root == nullptr) {
            return 0;
        }
        int right = help(root->right);
        int left = help(root->left);
        
        if (right == -1 || left == -1) {
            return -1;
        }
        if (right - left > 1 || left - right > 1) {
            return -1;
        }
        return 1 + max(left, right);
    }
};
