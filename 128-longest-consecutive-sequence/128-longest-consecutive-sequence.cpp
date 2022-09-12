class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_map<int,int> m;
        int ret = 0;
        for (auto i : nums) {
            m[i] = 1;
        }
        for (auto i : nums) {
            if (m[i-1] != 1) {
                ret = max(1,ret);
                int p = i+1;
                while (m[p] == 1) {
                    ret = max(ret, p-i+1);
                    p++;
                }
                
            }
        }
        return ret;
    }
};