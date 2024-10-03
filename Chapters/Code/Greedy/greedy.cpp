#include "greedy.h"

bool sortSecond(const pair<int,int> &a , const pair<int,int> &b){
    return a.second < b.second;
}

vector<pair<int,int>> intervalScheduling(vector<pair<int,int>>& intervals){
    sort(intervals.begin(), intervals.end(),sortSecond);
    vector<pair<int,int>> ans; 
    ans.push_back(intervals[0]);
    for(int i = 1; i < intervals.size() ; i++){
        if(intervals[i].first >= ans[ans.size() - 1].second){
            ans.push_back(intervals[i]);
        }
    }
    return ans;
}