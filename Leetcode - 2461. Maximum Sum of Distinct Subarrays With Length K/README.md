# Name 2461. Maximum Sum of Distinct Subarrays With Length K

**Link** to the problem -> https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/description/?envType=daily-question&envId=2024-11-19

# Solution

```
We are given an array and we have to find a maximum sum in a subarray where all values are distinct and subarray is equal to **k**
Visualizing the problem, we can see that subarrays overlap, except for the start value.
For example in array [1,5,4,2,9,9,9] and k = 3 we can get
[1, 5, 4] | [5, 4 2] | [4, 2, 9]

We can see the sums overlapping. Therefore, save value of sum and subtract a start value as it slides. Use a hashmap to keep track of duplicates.

Solution is O(n), 
Runtime 43 ms
Beats 58.06%
------------
Memory 58.18 MB
Beats 70.25%

```


