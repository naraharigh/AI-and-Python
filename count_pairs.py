def countPairs(arr, target):
    n = len(arr)
    cnt = 0

    # Iterate through each element in the array
    for i in range(n):
      
        # For each element arr[i], check every
        # other element arr[j] that comes after it
        for j in range(i + 1, n):
          
            # Check if the sum of the current pair
            # equals the target
            if arr[i] + arr[j] == target:
                cnt += 1
    return cnt

if __name__ == "__main__":
    arr = [1, 5, 7, -1, 5]
    target = 6
    print(countPairs(arr, target))