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
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> res;
        dfs(root, res, 0);
        return res;
    }
private:
    void dfs(TreeNode* node, vector<vector<int>>& l, int depth) {
        if (!node) {
            return;
        }
        if (depth == l.size()) {
            l.push_back(vector<int>());
        }
        l[depth].push_back(node->val);
        dfs(node->left, l, depth + 1);
        dfs(node->right, l, depth + 1);
        return;
    }
};
