#include "dp.h"

bool sortS(const request &a, const request &b)
{
    return a.first.first < b.first.first;
}

int findIndexS(const int s, const vector<request> &intervals, int low, int high)
{
    if (low == high - 1)
    {
        if(intervals[low] >= s)
            return low;
        else
            return high;
    }
    int mid = (low + high) / 2;
    if (intervals[mid].first.first > s)
    {
        return findIndexS(s, intervals, low, mid);
    }
    return findIndexS(s, intervals, mid, high);
}

vector<request> weightedIntervalScheduling(vector<request> &intervals)
{
    int n = intervals.size();
    vector<int> dp(n + 1, 0);
    sort(intervals.begin(), intervals.end(), sortS);
    for (int i = n - 1; i >= 0; i--)
    {
        int j = findIndexS(intervals[i].first.second,intervals,i,n);
        int first_op = dp[j] + intervals[i].second;
        int second_op = dp[i+1];
        dp[i] = (first_op > second_op) ? first_op : second_op;
    }
    return dp[0];
}
