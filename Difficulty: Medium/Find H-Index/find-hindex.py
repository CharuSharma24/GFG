#User function Template for python3
class Solution:
    def hIndex(self, citations):
        n = len(citations)
        c = [0] * (n + 1)
        for i in citations:
            if i >= n:
                c[n] += 1
            else:
                c[i] += 1
        tot_papers = 0
        for i in range(n, -1, -1):
            tot_papers += c[i]
            if tot_papers >= i:
                return i
        return 0


#{ 
 # Driver Code Starts
# Initial Template for Python 3

# Main
if __name__ == '__main__':
    t = int(input())
    while t > 0:
        t -= 1
        arr = [int(x) for x in input().strip().split()]

        ob = Solution()
        result = ob.hIndex(arr)

        print(result)
        print("~")

# } Driver Code Ends