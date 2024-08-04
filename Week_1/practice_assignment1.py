'''
You begin with a stack of n boxes.

Then you make a sequence of moves. In each move, you divide one stack of boxes into two 
nonempty stacks. The game ends when you have n stacks, each containing a single box. 
You earn points for each move; in particular, if you divide one stack of height a + b into 
two stacks with heights a and b, then you score ab points for that move. Your overall score 
is the sum of the points that you earn for each move.

What strategy should you use to maximize your total score?
'''
def maximize_score(n):
    score = 0
    while n > 1:
        # Divide the stack into two parts: 1 and (n-1)
        part1 = 1
        part2 = n - 1
        score += part1 * part2
        # Update n to the new largest stack
        n = part2
    return score

# Example usage
no_of_tc = int(input())
for _ in range(no_of_tc):
    n = int(input())
    print(maximize_score(n))
