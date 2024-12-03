class Solution:
    def minChar(self, s):
        #Write your code here
         # Create the reversed string
        s_rev = s[::-1]
        # Concatenate the string with its reverse with a special character
        temp = s + '#' + s_rev
        # Compute the LPS array
        lps = [0] * len(temp)
        j = 0  # Length of the previous longest prefix suffix
        for i in range(1, len(temp)):
            while j > 0 and temp[i] != temp[j]:
                j = lps[j - 1]
            if temp[i] == temp[j]:
                j += 1
            lps[i] = j
        # Result is the difference between string length and longest palindromic suffix
        return len(s) - lps[-1]
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    for _ in range(int(input())):
        s = input()
        obj = Solution()
        ans = obj.minChar(s)
        print(ans)
        print("~")

# } Driver Code Ends