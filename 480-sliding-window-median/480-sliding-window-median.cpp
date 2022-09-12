class Solution {
public:
    double med(multiset<int>& m, int k) {
        // for (auto i : m) {
        //     cout << i << ' ';
        // }
        // cout << endl;
        if (k==1) {
            return *m.begin();
        }
        auto it = m.begin();
        for (int i=0; i < (k/2 - 1); i++) {
            it++;
        }
        if (k%2 == 0) {
            double a = *(it);
            ++it;
            double b = *(it);
            return (a+b)/2;
        }
        ++it;
        return *(it);
    }
    
    vector<double> medianSlidingWindow(vector<int>& nums, int k) {
        multiset<int> window(nums.begin(), nums.begin()+k);
        vector<double> meds;
        meds.push_back(med(window, k));
        for (int i = k; i < nums.size(); i++) {
            window.erase(window.lower_bound(nums[i-k]));
            window.insert(nums[i]);
            meds.push_back(med(window, k));
        }
        return meds;
    }
};