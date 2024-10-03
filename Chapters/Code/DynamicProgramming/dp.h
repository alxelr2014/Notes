#pragma once
#include <cstdlib>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;

typedef pair<pair<int,int>, int> request;
vector<request> weightedIntervalScheduling(vector<request>& intervals);
