<!-- vim-markdown-toc GFM -->

  * [backtracking](#backtracking)
  * [deque 要点](#deque-要点)
  * [枚举](#枚举)
  * [矩阵](#矩阵)
* [技巧](#技巧)
  * [反向思考](#反向思考)
  * [思考数字的存储的位的结构](#思考数字的存储的位的结构)

<!-- vim-markdown-toc -->

## backtracking

要点是：

1. 在当前这个点做一个尝试，如果尝试[满足条件],就继续进行下一个点的尝试
2. 如果[不满足条件]就 revert 这个点回去（否则数据就乱了）
3. 如果没有点需要继续尝试，那么我们得到了一个解。

## deque 要点

[239. Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/)

[1425. Constrained Subsequence Sum](https://leetcode.com/problems/constrained-subsequence-sum/)

维护一个双端队列,存放的是下标（因为下标信息，和数字都会用于淘汰。通过下标可以获
得数字，通过数字无法获得下标）：

- 最开头的，如果 index = deque[0]不满足要求（index<=i-k，在窗口之外) 则淘汰；(其
  实从开头开始淘汰，最多只会淘汰一次）;
- 最末尾的，如果 deque[-1] < nums[index]，则没有存在的必要，因为现在的数字比它大
  并且比它年轻，之后的滑动窗口不再需要，从后往前 pop 出来所有的这样的数字。

这样 deque[0] 保存的永远是我们想要的数字。

## 枚举

可以用一个 `list(range(1, 1+n))` 来表示下标和值都相等的列表，每用掉一个，就从列
表中 `pop(index)` 去掉一个。

## 矩阵

沿着斜线对称翻转其实就是 row col 对调，对于矩阵转换，可以试着写出来几个转换前后
的坐标，看其中有什么规律。
[48. Rotate Image](https://leetcode.com/problems/rotate-image/)

# 技巧

## 反向思考

比如给你一段 string，将它由心向外螺旋打印，比如:

```
oll.
whe.
orld
```

正向打印是比较烦的，因为要找起始点，所以可以将 string reverse，然后从尾部开始打
印。

## 思考数字的存储的位的结构

很多要求 O(1)空间的可以思考是否利用数字空闲的位，比如用 -x 来表示 x 之前出现过没
有。
