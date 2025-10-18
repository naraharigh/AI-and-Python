class Solution:
    def __init__(self):
        pass
    def maxSum(self, arr): 
        # Code here
        return self.sort_elements(arr)
    def sort_elements(self, arr):
        i = 0
        j =  1
        
        while i < len(arr) - 1:
            print(i)
            if arr[i] <  arr[j]:
                arr[i],arr[j] = arr[j],arr[i]
            i = i+1
            j = j+1
            
        print(arr)
        sum = 0
        for index,elm in enumerate(arr):
            print (index-1,elm)
            if index == 0:
                print('coming')
                sum = sum + (len(arr)-1)*elm
            else:
               sum = sum + elm*(index-1)
        return sum 

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

   ans = Solution()
   arr = [8, 3, 1, 2]
   print(ans.maxSum(arr))