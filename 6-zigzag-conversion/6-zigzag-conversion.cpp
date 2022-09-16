class Solution {
public:
    string convert(string s, int numRows) {
        if (numRows == 1) return s;
        vector<char> z[numRows];
        int i = 0;
        int row = 0;
        bool down = true;
        while (i < s.length()) {
            z[row].push_back(s[i]);
            i++;
            if ((row == 0 && !down) || (row == numRows-1 && down)) {
                down = !down;
            }
            if (down) {
                row++;
            } else {
                row--;
            }
        }
        string ret = "";
        for (int i=0; i < numRows; i++) {
            for (auto c:z[i]) {
                ret += c;
            }
        }
        return ret;
    }
};