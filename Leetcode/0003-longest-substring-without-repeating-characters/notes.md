# LeetCode 0003: Longest substring without repeating characters

## Problem

Given a string `s`, find the length of the longest substring without duplicate characters.

## Notes

Think of a ruler stretched over a string of letters. The left edge (`left`) and right edge (`right`) mark your active window.
Your dictionary (`seen`) acts as a logbook recording every character's latest index. You never delete old entries from this logbook.
When `right` encounters a letter already in the logbook, check if its last position sits inside your current ruler. If it does, snap `left` directly past that old position (`seen[char] + 1`).

### Algorithm

Initialize a dict (`seen`) to store the last seen index of each character, alongside `left = 0` and `max_len = 0`.
Iterate through `s` with index `right` and character `char`:

1. **Check:** If `char in seen` and `seen[char] >= left`, set `left = seen[char] + 1`.
2. **Record:** Set `seen[char] = right`.
3. **Measure:** Update max length using `right - left + 1`.

### Why `seen[char] >= left` is required

Old entries stay in the logbook even after your ruler slides past them.

Trace `a b b a` with indices 0, 1, 2, 3:

1. At index 2 (the second `b`), `left` moves to index 2. Window is `"b"`.
2. At index 3 (the second `a`), you look up `a` in the logbook. The logbook returns index 0.
3. Index 0 is behind your current `left` boundary of 2. That old `a` fell off the ruler earlier.
4. Without checking `seen['a'] >= left`, `left` would jump backward from 2 to 1. That turns your window into `"bba"`, which contains duplicates.

Checking if `seen[char] >= left` stops `left` from ever jumping backward into old history.
