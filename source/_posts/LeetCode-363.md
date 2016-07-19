---
title: LeetCode 363
date: 2016-07-15 17:10:27
tags:
- 动态规划
- 扫描线
- STL
- LeetCode
- Hard
- 二分查找
- 算法

categories:
- 算法
---

## 题目及分析

给一个非空r*c的矩阵（r>>c），找一个子矩阵使得该矩阵的和不超过给定的k（难度：hard）

暴力方法： 枚举两个子矩阵的两个端点，复杂度`O(rrcc)`
这个问题是另外几个问题的叠加

<!-- more -->

## 问题1
题意： 给定一个一维数组A，求解A中和最大的子序列

思路： 动态规划，`d[i]`表示以`A[i]`为结尾的和最大序列的和，那么以`A[i+1]`结尾和最大序列则为：如果`d[i]>0`,则序列接上`A[i]`,否则`A[i+1]`自己为和最大序列。转移公式为：`d[i+1] = d[i] > 0 ? d[i] + A[i+1], A[i+1]`。时间复杂度为`O(n)`。

## 问题2
题意： 求一个二维矩阵A的子矩阵，使得子矩阵的所有元素的和最大

思路： 扫描线，每次固定两列L、R，表示子矩阵的左右两端，对于每一行求出L~R列的和(使用累积和相减)，即可得到一个一维数组`A[row]`,问题转换为即可转换为问题1。固定。时间复杂度为`O(min(ccr,rrc))`。

## 问题3
题意： 给定一个一维数组A，求解A中和不超过k的最大子序列

思路： 预处理一个累加和数组C，`C[i]`表示从`sum(A[0~i])`，则`sum(A[i~j]) = C[j] - C[i-1]`，问题可表述为：找到一对i，j使得`T = C[j] - C[i-1] <= k`并且使T最大。 通过移项有： `C[j] - k <= C[i-1]`, 问题转换为： 对与每个j，在集合`S = {0, C[1], C[2], ... C[j-1]}`中求一个小于 `C[j] - K`的最大值，如果使用二叉搜索树维护S，则该问题的复杂度为`O(lgj)`。总体复杂度`O(nlgn)`。

## 本题
明白了以上问题的解法，本题将迎刃而解。

首先，使用扫描线法每次固定两列（r>>c）L、R，求出每一行L～R列的和得到一个一维数组A，使用问题3中的方法找出A中和小于但最接近k的子序列，总体时间复杂度为：`O(ccrlgr)`

代码如下：

```C++
class Solution {
public:
    int maxSumSubmatrix(vector< vector<int> >& matrix, int k) {
        int row = matrix.size(), col = matrix[0].size();
        int cum_matrix[row][col];
        //预处理，对每行累积求和
        for(int i = 0; i < row; i++){
            for(int j = 0; j < col; j++){
                if(j == 0)cum_matrix[i][j] = matrix[i][j];
                else cum_matrix[i][j] = cum_matrix[i][j - 1] + matrix[i][j];
            }
        }
        int max_sum = -0x7fffffff;
        set<int> cum_sum;
        //扫描线，固定两列，变成一个在以为数组中寻找最大不超过k的子序列
        for(int i = 0; i < col; i++){
            for(int j = i; j < col; j++){
                int f, tmp = 0;
                cum_sum.clear();
                // 二分
                for(int s = 0; s < row; s++){
                    cum_sum.insert(tmp);
                    if(i == 0) f = cum_matrix[s][j];
                    else f = cum_matrix[s][j] - cum_matrix[s][i - 1];
                    tmp += f;
                    //set本身有序，可使用STL中upper_bound函数
                    set<int>::iterator iter = cum_sum.upper_bound(tmp-k-1);
                    if(iter != cum_sum.end()){
                        max_sum = max(max_sum, tmp - *iter);
                    }
                }
            }
        }
        return max_sum;
    }
};
```


