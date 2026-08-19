# LeetCode 0009: Palindrome Number

## Problem

Given an integer `x`, return `true` if `x` is a palindrome, and `false` otherwise.

## Key intuition

Reversing only the back half of the integer cuts processing iterations in half and avoids integer overflow in fixed-width languages.

- **Negative numbers:** A minus sign breaks symmetry (`-121` reversed is `121-`).
- **Trailing zeros:** Numbers ending in zero (like `120`) are never palindromes because positive integers never start with zero. Only `0` itself is valid.

## Algorithm

1. Return `false` immediately if `x < 0` or if `x > 0` and `x % 10 == 0`.
2. Move digits from the end of `workx` into `rev` using `rev = rev * 10 + (workx % 10)`.
3. Shrink `workx` with floor division (`workx //= 10`).
4. Stop looping when `rev >= workx`. At this point, half the digits are processed.
5. Check equality:
   - Even digit count (`1221` leaves `workx = 12` and `rev = 12`): check `workx == rev`
   - Odd digit count (`12321` leaves `workx = 12` and `rev = 123`): check `workx == rev // 10` to drop the middle digit

## Complexity

- Time: `O(log10 N)`
- Space: `O(1)`
