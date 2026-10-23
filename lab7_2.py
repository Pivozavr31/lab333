def find_error_nums_easy(nums):
    n = len(nums)
    ideal_sum = n * (n+1) // 2
    unique_sum = sum(set(nums))
    actual_sum = sum(nums)
    rep = actual_sum - unique_sum
    miss = ideal_sum - unique_sum
    return[rep,miss]
print([1,2,2,4], "->", find_error_nums_easy([1,2,2,4]))
print([1,1], "->", find_error_nums_easy([1,1]))
print([2,2], "->", find_error_nums_easy([2,2]))
print([3,2,3,4,6,5], "->", find_error_nums_easy([3,2,3,4,654,]))





