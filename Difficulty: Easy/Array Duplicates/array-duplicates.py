class Solution:
    def findDuplicates(self, arr):
        dup={}
        n=len(arr)
        for num in arr:
            if num in dup:
                dup[num]+=1
            else:
                dup[num]=1
        result=[]
        for key,value in dup.items():
            if value>1:
                result.append(key)
        result.sort()
        return result
        # code here

#{ 
 # Driver Code Starts
# Initial Template for Python 3

t = int(input())  # number of test cases
for _ in range(t):
    arr = list(map(int, input().split()))  # input array
    s = Solution().findDuplicates(arr)  # find the duplicates

    # Output formatting
    if s:
        print(" ".join(map(str, s)))  # Print duplicates in ascending order
    else:
        print("[]")  # Print empty list if no duplicates are found
    print("~")

# } Driver Code Ends