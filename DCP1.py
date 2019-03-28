# Good morning! Here's your coding interview problem for today.

# This problem was recently asked by Google.

# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

# Bonus: Can you do this in one pass?

def solution(nums, target):
    seen = []
    for num in nums:
        if  target - num in seen:
            return True
        else:
            seen.append(num)
    return False

if __name__=="__main__":
    nums = [10, 15, 3, 7]
    target = 1
    print(solution(nums, target))
