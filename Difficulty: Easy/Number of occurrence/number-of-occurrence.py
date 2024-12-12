class Solution:
    def countFreq(self, arr, target):
        #code here
        count = [0]
        def recursion(low, high):
            if low<=high:
                mid = (low+high)//2
                
                if arr[mid]==target:
                    count[0] = count[0] + 1
                    recursion(mid+1, high)
                    recursion(low,mid-1)
                
                elif arr[mid]<target:
                    recursion(mid+1,high)
                
                else:
                    recursion(low,mid-1)
        
        recursion(0, len(arr)-1)
        return count[0]
#{ 
 # Driver Code Starts
#Initial Template for Python 3
import bisect
#Main
if __name__ == '__main__':
    t = int(input())
    while t:
        t -= 1
        A = [int(x) for x in input().strip().split()]
        nd = [int(x) for x in input().strip().split()]
        D = nd[0]
        ob = Solution()
        ans = ob.countFreq(A, D)
        print(ans)
        print("~")

# } Driver Code Ends