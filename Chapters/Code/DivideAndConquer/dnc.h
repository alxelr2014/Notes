#pragma once
#include <cstdlib>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;
typedef pair<int,int> point;


void mergesort(vector<int> & arr);

int countInversion(vector<int> & arr);

void removeRepeatedElement(vector<int> & arr);

int integerMultiply(int x , int y, int n);

pair<point,point> closestPair(const vector<point> & points);

