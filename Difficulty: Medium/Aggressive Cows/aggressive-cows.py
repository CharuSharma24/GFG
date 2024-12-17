#User function Template for python3

class Solution:

    def aggressiveCows(self, stalls, k):
        stalls.sort()
        left, right = 1, stalls[-1] - stalls[0]
        while left <= right:
            mid = left + (right - left) // 2
            prev, count = -10**8, 0
            for s in stalls:
                if s - prev >= mid:
                    count += 1
                    prev = s
            if count >= k:
                left = mid + 1
            else:
                right = mid - 1
        return right


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
        ans = ob.aggressiveCows(A, D)
        print(ans)
        print("~")
# } Driver Code Ends