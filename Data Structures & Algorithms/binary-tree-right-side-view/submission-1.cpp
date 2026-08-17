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
    vector<int> rightSideView(TreeNode* root) {
        vector<int> res;
        dfs(root, res, 0);
        return res;
    }
private:
    void dfs(TreeNode* node, vector<int>& nums, int depth) {
        if (!node) {
            return;
        }
        if (nums.size() == depth) {
            nums.push_back(node->val);
        }
        nums[depth] = node->val;
        dfs(node->left, nums, depth + 1);
        dfs(node->right, nums, depth + 1);
    }
};
