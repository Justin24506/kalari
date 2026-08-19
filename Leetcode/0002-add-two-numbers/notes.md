# LeetCode 0002: Add Two Numbers

## Problem

Add two numbers represented by two linked lists.

## Notes

Traverse both linked lists together using a loop condition: `while l1 or l2 or carry`.  
If any of them exist, add their values to get the total.  
Floor dividing this total by 10 (`total // 10`) gives the new carry, and the digit to enter into the result linked list is `total % 10`.  
Always check if each linked list node exists separately. Only if it exists, should you advance to `.next`.

**Loop Condition:** `while l1 or l2 or carry`  
**Sum Values:** `total = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry`  
**Split Total:** `carry = total // 10` (the tens place), `node_val = total % 10` (the ones place)  
**Advance Pointers:** `l1 = l1.next if l1 else None` (same for `l2`)
