'''
At a party, there are n cups of gulab jamun arranged in a circle. A fly is sitting in one of the cups at the moment.

After minute number k, the fly jumps over k - 1 cups (clockwise) and lands and the next one. For example, after the first minute the fly ends up at the neighboring cup, and after that at the third cup from the start.

You should answer: will the fly visit all the cups or not?

We assume that fly is jumping forever.

Input. The only line contains single integer: 1 ≤ n ≤ 1000 — number of cups.

Output. Output "YES" if all the cups will be visited and "NO" otherwise
'''
import math

def will_fly_visit_all_cups(n):
    # The fly will visit all cups if and only if the step size and n are coprime.
    # This is true if and only if GCD(n, k) is 1 for all k.
    # However, we just need to check if GCD(n, k) == 1 for any k in the sequence.
    visited = [False] * n
    position = 0
    for k in range(1, n + 1):
        position = (position + k) % n
        if visited[position]:
            return "NO"
        visited[position] = True
    return "YES"

# Input handling
n = int(input())

# Check if the fly will visit all cups and print the result
print(will_fly_visit_all_cups(n))
