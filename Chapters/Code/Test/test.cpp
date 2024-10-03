#include "test.h"

void mergesortTest()
{
    vector<int> arr = {15, 7, 1, 4, 2, 6, 8, 12, 5};
    printf("Unsorted: ");
    for (int i : arr)
        printf("%d ", i);
    printf("\n");
    auto start = high_resolution_clock::now();
    mergesort(arr);
    auto stop = high_resolution_clock::now();
    auto duration = duration_cast<milliseconds>(stop - start);
    printf("Sorted: ");
    for (int i : arr)
        printf("%d ", i);
    printf("\n");
    printf("solved in %llu milliseconds\n", duration.count());
}

void countInversionTest()
{
    vector<int> arr = {15, 7, 1, 4, 2, 6, 8, 12, 5};
    printf("Array: ");
    for (int i : arr)
        printf("%d ", i);
    printf("\n");
    auto start = high_resolution_clock::now();
    int ans = countInversion(arr);
    auto stop = high_resolution_clock::now();
    auto duration = duration_cast<milliseconds>(stop - start);
    printf("Number of Inversions: %d\n", ans);
    printf("solved in %llu milliseconds\n", duration.count());
}

void removeRepeatedElementTest()
{
    vector<int> arr = {15, 7, 5, 6, 12, 15, 1, 4, 5, 3, 1, 2, 4, 2, 6, 8, 12, 5};
    printf("Array: ");
    for (int i : arr)
        printf("%d ", i);
    printf("\n");
    auto start = high_resolution_clock::now();
    removeRepeatedElement(arr);
    auto stop = high_resolution_clock::now();
    auto duration = duration_cast<milliseconds>(stop - start);
    printf("Repeated elements removed: ");
    for (int i : arr)
        printf("%d ", i);
    printf("\n");
    printf("solved in %llu milliseconds\n", duration.count());
}

void integerMultTest()
{
    int x = 12;
    int y = 32;
    auto start = high_resolution_clock::now();
    int ans = integerMultiply(x, y, 9);
    auto stop = high_resolution_clock::now();
    auto duration = duration_cast<milliseconds>(stop - start);
    printf("%d * %d = %d\n", x, y, ans);
    printf("solved in %llu milliseconds\n", duration.count());
}

void closestPairTest()
{
    vector<point> points = {point(3, 4), point(1, 0), point(-4, 1), point(5, 9), point(10, 2), point(2, 1)};
    auto start = high_resolution_clock::now();
    pair<point, point> ans = closestPair(points);
    auto stop = high_resolution_clock::now();
    auto duration = duration_cast<milliseconds>(stop - start);
    printf("[(%d,%d) - (%d,%d)]\n", ans.first.first, ans.first.second, ans.second.first, ans.second.second);
    printf("solved in %llu milliseconds\n", duration.count());
}

void intervalSchedulingTest()
{
    vector<pair<int, int>> intervals = {pair<int, int>(1, 3), pair<int, int>(2, 3), pair<int, int>(2, 4), pair<int, int>(1, 2), pair<int, int>(3, 4)};
    auto start = high_resolution_clock::now();
    vector<pair<int, int>> ans = intervalScheduling(intervals);
    auto stop = high_resolution_clock::now();
    auto duration = duration_cast<milliseconds>(stop - start);
    for (int i = 0; i < ans.size(); i++)
        printf("(%d,%d) ", ans[i].first, ans[i].second);
    printf("\n");
    printf("solved in %llu milliseconds\n", duration.count());
}