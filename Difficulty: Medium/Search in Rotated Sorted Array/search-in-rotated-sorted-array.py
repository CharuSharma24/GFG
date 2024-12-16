#User function Template for python3
class Solution:
    def search(self,arr,key):
        flag = -1
        if arr[0]>key:
            for i in range(0, len(arr)):
                n = len(arr) - i - 1
                if arr[n] == key:
                    flag = n
                if arr[n-1] > arr[n]:
                    break
        else:
            for i in range(0, len(arr)):
                if arr[i] == key:
                    flag = i
                
        
        return flag
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        A = list(map(int, input().strip().split()))
        k = int(input())
        ob = Solution()
        print(ob.search(A, k))
        print("~")

# } Driver Code Ends