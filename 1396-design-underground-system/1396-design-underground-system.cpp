class UndergroundSystem {
public:
    unordered_map<int, pair<string, int>> enterr;
    unordered_map<string, pair<int,int>> times;
    UndergroundSystem() {

    }
    
    void checkIn(int id, string stationName, int t) {
        enterr[id] = make_pair(stationName, t);
    }
    
    void checkOut(int id, string stationName, int t) {
        int elapsed = t - enterr[id].second;
        string idx = enterr[id].first+";"+stationName;
        enterr.erase(id);
        if (times.count(idx)) {
            times[idx].first += elapsed;
            times[idx].second += 1;
        } else {
            times[idx] = make_pair(elapsed, 1);
        }
        // for (auto i : times) {
        //     printf("%s %d %d\n", i.first.c_str(), i.second.first, i.second.second);
        // }
    }
    
    double getAverageTime(string startStation, string endStation) {
        return (float)times[startStation+";"+endStation].first / (double)times[startStation+";"+endStation].second;
    }
};

/**
 * Your UndergroundSystem object will be instantiated and called as such:
 * UndergroundSystem* obj = new UndergroundSystem();
 * obj->checkIn(id,stationName,t);
 * obj->checkOut(id,stationName,t);
 * double param_3 = obj->getAverageTime(startStation,endStation);
 */