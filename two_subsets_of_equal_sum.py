def equalPartition(arr):
    # Calculate sum of the elements in array
    arrSum = sum(arr)

    # If sum is odd, there cannot be two 
    # subsets with equal sum
    if arrSum % 2 != 0:
        return False

    # Find if there is subset with sum equal 
    # to half of total sum
    return isSubsetSum(len(arr), arr, arrSum // 2)

def isSubsetSum(n, arr, sum):
  
    # base cases
    if sum == 0:
        return True
    if n == 0:
        return False

    # If element is greater than sum, then ignore it
    if arr[n-1] > sum:
        return isSubsetSum(n-1, arr, sum)

    # Check if sum can be obtained by any of the following
    # (a) including the current element
    # (b) excluding the current element
    return isSubsetSum(n-1, arr, sum) or \
  		   isSubsetSum(n-1, arr, sum - arr[n-1])

if __name__ == "__main__":
    arr = [1, 5, 11, 5]
    if equalPartition(arr):
        print("True")
    else:
        print("False")
          