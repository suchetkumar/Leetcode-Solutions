class Solution {
public:
    vector<string> findItinerary(vector<vector<string>>& tickets) {
        vector<string>ans;
		// create an adjacency list: unordered_ map is been used for easy random access of the using strings, multiset: automatically stores the elements in alphabetical order.
        unordered_map<string, multiset<string>>adj;
        for(int i=0;i<tickets.size();i++)
        {
            adj[tickets[i][0]]. insert(tickets[i][1]);

        }
		
        stack<string>s;
        s.push("JFK");
		
        while(s.empty()==false)
        {
            string curr= s.top();
            if(adj[curr].size()==0)
            {
                ans.push_back(curr);
                s.pop();
            }
            else
            {
                auto it= adj[curr].begin();
                s.push(*it);
                adj[curr].erase(it);
            }
        }
        reverse(ans.begin(), ans.end());
        return ans;
    }
};