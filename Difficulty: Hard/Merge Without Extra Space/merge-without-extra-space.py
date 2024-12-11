from typing import List

class Solution:
    def mergeArrays(self, a: List[int], b: List[int]) -> None:
        if a and b and b[0] < a[-1]:
            na, nb = len(a), len(b)
            ma = mb = 0
            while (ma + mb) < na:
                if mb < nb and b[mb] < a[ma]:
                    mb += 1
                else:
                    ma += 1
            a[ma:na], b[0:mb] = b[0:mb], a[ma:na]
            a.sort()
            b.sort()
#{ 
 # Driver Code Starts
# Input handling and main function
if __name__ == "__main__":
    # Number of test cases
    t = int(input().strip())

    for _ in range(t):
        # Input first array
        a = list(map(int, input().strip().split()))
        # Input second array
        b = list(map(int, input().strip().split()))

        # Create solution object and merge the arrays
        solution = Solution()
        solution.mergeArrays(a, b)

        # Output both arrays in the same line space-separated
        print(" ".join(map(str, a)))
        print(" ".join(map(str, b)))

# } Driver Code Ends