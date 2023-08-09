# 1822. Sign of the Product of an Array

There is a function signFunc(x) that returns: </br>

1 if x is positive. </br>
-1 if x is negative. </br>
0 if x is equal to 0. </br>
You are given an integer array nums. Let product be the product of all values in the array nums. </br>

Return signFunc(product). </br>

## Example 1:

Input: nums = [-1,-2,-3,-4,3,2,1] </br>
Output: 1 </br>
Explanation: The product of all values in the array is 144, and signFunc(144) = 1 </br>

## Example 2:

Input: nums = [1,5,0,2,-3] </br>
Output: 0 </br>
Explanation: The product of all values in the array is 0, and signFunc(0) = 0 </br>

## Example 3:

Input: nums = [-1,1,-1,1,-1] </br>
Output: -1 </br>
Explanation: The product of all values in the array is -1, and signFunc(-1) = -1 </br>

## Constraints:

1 <= nums.length <= 1000 </br>
-100 <= nums[i] <= 100 </br>
