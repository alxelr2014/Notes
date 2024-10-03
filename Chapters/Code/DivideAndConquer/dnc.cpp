#include "dnc.h"

// sort arr from arr[low] to arr[high - 1]
void mergesort(vector<int> & arr){
    if(arr.size() == 1 || arr.size() == 0) return;
    int mid = arr.size()/2; 
    vector<int> left(arr.begin(), arr.begin() + mid);
    vector<int> right(arr.begin() + mid, arr.end());
    mergesort(left);
    mergesort(right);
    int left_ind = 0, right_ind =0;
    int left_size = left.size(), right_size = right.size();
    int curr_ind = 0;
    while(left_ind < left_size || right_ind < right_size){
        if(left_ind < left_size && right_ind < right_size){
            if(left[left_ind] <= right[right_ind]){
                arr[curr_ind++] = left[left_ind++];
            }
            else{
                arr[curr_ind++] = right[right_ind++];
            }
        }
        else if(left_ind < left_size){
                arr[curr_ind++] = left[left_ind++];
        }
        else {
                arr[curr_ind++] = right[right_ind++];
        }
    }
}

int countInversion(vector<int> & arr){
    if(arr.size() == 1 || arr.size() == 0) return 0;
    int mid = arr.size()/2; 
    vector<int> left(arr.begin(), arr.begin() + mid);
    vector<int> right(arr.begin() + mid, arr.end());
    int ans = 0;
    ans += countInversion(left);
    ans += countInversion(right);
    int left_ind = 0, right_ind =0;
    int left_size = left.size(), right_size = right.size();
    int curr_ind = 0;
    while(left_ind < left_size || right_ind < right_size){
        if(left_ind < left_size && right_ind < right_size){
            if(left[left_ind] <= right[right_ind]){
                arr[curr_ind++] = left[left_ind++];
            }
            else{
                arr[curr_ind++] = right[right_ind++];
                ans+= left_size - left_ind;
            }
        }
        else if(left_ind < left_size){
                arr[curr_ind++] = left[left_ind++];
        }
        else {
                arr[curr_ind++] = right[right_ind++];
        }
    }
    return ans; 
}

void removeRepeatedElement(vector<int> & arr){
    if(arr.size() == 1 || arr.size() == 0) return;
    int mid = arr.size()/2; 
    vector<int> left(arr.begin(), arr.begin() + mid);
    vector<int> right(arr.begin() + mid, arr.end());
    removeRepeatedElement(left);
    removeRepeatedElement(right);
    int left_ind = 0, right_ind =0;
    int left_size = left.size(), right_size = right.size();
    int curr_ind = 0;
    while(left_ind < left_size || right_ind < right_size){
        if(left_ind < left_size && right_ind < right_size){
            if(left[left_ind] < right[right_ind]){
                arr[curr_ind++] = left[left_ind++];
            }
            else if(left[left_ind] == right[right_ind]){
                right_ind++;
            }
            else{
                arr[curr_ind++] = right[right_ind++];
            }
        }
        else if(left_ind < left_size){
                arr[curr_ind++] = left[left_ind++];
        }
        else {
                arr[curr_ind++] = right[right_ind++];
        }
    }
    while(curr_ind <= arr.size() - 1)
        arr.pop_back();
}


int integerMultiply(int x , int y, int n){
    if(n <= 3) return x*y;
    int mid = n/2;
    int high = n - mid;
    int power = 1 << mid;
    int x0 = x & (power - 1), y0 = y & (power - 1);
    int x1 = x >> mid,  y1 = y >> mid;
    int s = integerMultiply(x0 + x1, y0 + y1, high + 1);
    int p1 = integerMultiply(x0,y0,mid);
    int p3= integerMultiply(x1,y1,high);
    int p2 = s - p1 - p3;
    return p1 + (p2 << mid) + (p3 << (2 * mid));
}

typedef pair<point,pair<int,int>> pind;
typedef pair<point,int> ppoint;

bool comparex(const ppoint & a, const ppoint &b)
{
    return a.first.first < b.first.first;
}
bool comparey(const ppoint & a, const ppoint &b)
{
    return a.first.second < b.first.second;
}
double integerNorm(const point &a , const point& b){
    int diffx = a.first-b.first;
    int diffy = a.second - b.second;
    return sqrt(diffx* diffx + diffy*diffy);
}

pair<point,point> closestPairSolve(int low, int high, const vector<ppoint> &px, const vector<ppoint> &py){
    if(low +2 == high){
        return pair<point,point> (px[low].first, px[low + 1].first);
    }
    if(low + 3== high){
        double norm12 = integerNorm(px[low].first, px[low+1].first),
            norm13 = integerNorm(px[low].first, px[low + 2].first),
            norm23 = integerNorm(px[low +1].first, px[low + 2].first);
        if(norm12 <= norm13 && norm12 <= norm23){
            return pair<point,point> (px[low].first, px[low + 1].first);
        }
        if(norm13 <= norm12 && norm13 && norm23){
            return pair<point,point> (px[low].first, px[low + 2].first);
        }
        return pair<point,point> (px[low + 1].first, px[low + 2].first);
    }

    int mid = low + (high - low)/2;
    pair<point,point> left_result = closestPairSolve(low,mid,px,py);
    pair<point,point> right_result = closestPairSolve(mid,high,px,py);
    int norm_left = integerNorm(left_result.first,left_result.second),
        norm_right = integerNorm(right_result.first,right_result.second);
    double min_norm = (norm_left <= norm_right) ? norm_left : norm_right;
    pair<point,point> min_points = (norm_left <= norm_right) ? left_result : right_result;

    vector<point> boundary;
    double lowx = px[mid].first.first - min_norm/2.0;
    double highx = px[mid].first.first + min_norm/2.0;
    for(int i = high - 1; i >= low ; i--)
    {
        if((py[i].first.first >= lowx && py[i].first.first <= highx)){
            boundary.emplace_back(py[i].first);
        }
    }
    for(int i = 0 ; i < boundary.size(); i++){
        for(int j = 1; (j +i )< boundary.size() && j <= 10; j++){
            if(integerNorm(boundary[i], boundary[j+i]) < min_norm){
                min_norm = integerNorm(boundary[i],boundary[i + j]);
                min_points = pair<point,point>(boundary[i],boundary[j]);
            }
        }
    }
    return min_points;
}

pair<point,point> closestPair(const vector<point> & points){
    int psize = points.size();
    vector<pind> pinds (psize);
    vector<ppoint> px (psize);
    vector<ppoint> py (psize);
    for(int i = 0 ; i < psize; i++){
        pinds[i].first =points[i];
        px[i]= ppoint(points[i],i);
        py[i]= ppoint(points[i],i);
    }
    sort(px.begin(), px.end(), comparex);
    sort(py.begin(), py.end(), comparey);

    for(int i = 0 ; i < psize; i++){
        pinds[i].second.first = px[i].second;
        pinds[i].second.second = py[i].second;
    }
    return closestPairSolve(0,psize,px,py);
}