class Solution {
public:
    int minDistance(string word1, string word2) {
        string n = word1;
        string m = word2;
        vector< vector<int> > dp(n.length()+1, vector<int>(m.length()+1, 0));
          for (int i = 0; i < n.length()+1; i++) {
            dp[i][0] = i;
          }
          for (int i = 0; i < m.length()+1; i++) {
            dp[0][i] = i;
          }
          for (int i = 1; i < n.length()+1; i++) {
            for (int j = 1; j < m.length()+1; j++) {
              int cost = 1;
              if (n[i-1] == m[j-1]) {
                cost = 0;
              }
              int vals[3] = {dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1]+cost};
              dp[i][j] = *min_element(vals, vals+3);
            }
          }
          return dp[n.length()][m.length()];
    }
};