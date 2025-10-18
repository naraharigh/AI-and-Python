def subset_sum(arr, target_sum):
    n = len(arr)
    dp = [[False for _ in range(target_sum + 1)] for  _ in range(n + 1)]

    print(dp)

    # If sum is 0, the answer is True (empty set)
    for i in range(n + 1):
        dp[i][0] = True

    # Fill dp[][] in bottom-up manner
    for i in range(1, n + 1):
        for j in range(1, target_sum + 1):
            if arr[i-1] > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] or dp[i-1][j-arr[i-1]]

    return dp[n][target_sum]

arr = [3, 34, 4, 12, 5, 2]
target_sum = 9
# print(subset_sum(arr, target_sum))  # Output: True



def unbounded_knapsack(weights, values, capacity):
    dp = [0] * (capacity + 1)

    # Fill dp[] using the concept of unbounded knapsack
    for i in range(capacity + 1):
        for j in range(len(values)):
            if weights[j] <= i:
                dp[i] = max(dp[i], dp[i - weights[j]] + values[j])

    return dp[capacity]

weights = [1, 3, 4]
values = [15, 50, 60]
capacity = 8
print(unbounded_knapsack(weights, values, capacity))  # Output: 120

