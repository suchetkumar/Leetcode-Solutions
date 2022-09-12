class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> ret(nums.size(), 1);
        int p = 1;
        int s = 1;
        for (int i=0; i < nums.size()-1; i++) {
            p *= nums[i];
            s *= nums[nums.size()-1-i];
            ret[i+1] *= p;
            ret[ret.size()-2-i] *= s;
        }
        return ret;
    }
};