backtracking

要点是：
1. 在当前这个点做一个尝试，如果尝试[满足条件],就继续进行下一个点的尝试
2. 如果[不满足条件]就revert 这个点回去（否则数据就乱了）
3. 如果没有点需要继续尝试，那么我们得到了一个解。
