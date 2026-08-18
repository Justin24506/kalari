# LeetCode 0001: Two Sum

## Problem
Find the indices of two numbers in an array (`nums`) that add up to a specific value (`target`).

## Notes
The hashmap keeps a log of past numbers. 
For each number, check if `(target - num)` is already in the log:
- **No:** Insert `num` and its index into the hashmap.
- **Yes:** You found the pair! Return `[index of (target - num), index of num]`.
