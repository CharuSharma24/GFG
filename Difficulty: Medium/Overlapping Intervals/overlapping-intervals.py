class Solution:
    def mergeOverlap(self, arr):
        #Code here
        arr.sort(key=lambda x:x[0])
        
        stack = [arr[0]]
        for i in range(1,len(arr)):
            if stack[-1][1]>=arr[i][0]:
                stack[-1][1]=max(stack[-1][1],arr[i][1])
            else:
                stack.append(arr[i])
        return stack

#{ 
 # Driver Code Starts
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n = int(input())
        # a = list(map(int, input().strip().split()))
        arr = []
        # j = 0
        for i in range(n):
            a = list(map(int, input().strip().split()))
            x = a[0]
            # j += 1
            y = a[1]
            # j += 1
            arr.append([x, y])
        obj = Solution()
        ans = obj.mergeOverlap(arr)
        for i in ans:
            for j in i:
                print(j, end=" ")
        print()

# } Driver Code Ends