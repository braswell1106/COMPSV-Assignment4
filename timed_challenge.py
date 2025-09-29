# Pick one question from timed_challenge.txt
# Paste the question as a comment below
# Set a timer for 30 minutes and complete the question!
#Running Total with Reset
#Track a running total of values. If a negative number is added, reset the total to 0.
#Input: [5, 7, -1, 3, 2]
#Output: [5, 12, 0, 3, 5]
def running_total_with_reset(nums):
    total = 0
    result = []
    for n in nums:
        if n < 0:
            total = 0
        else:
            total += n
        result.append(total)
    return result

print(running_total_with_reset([5, 7, -1, 3, 2]))
