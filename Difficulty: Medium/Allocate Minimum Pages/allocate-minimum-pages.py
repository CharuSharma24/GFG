class Solution:
    
    def countStudents(self, nums, pages):
        # Size of array
        n = len(nums)
        
        students = 1
        pagesStudent = 0
        
        for i in range(n):
            if pagesStudent + nums[i] <= pages:
                # Add pages to current student
                pagesStudent += nums[i]
            else:
                # Add pages to next student
                students += 1
                pagesStudent = nums[i]
        
        return students
    
    """Function to allocate the book to ‘m’ 
    students such that the maximum number 
    of pages assigned to a student is minimum"""
    def findPages(self, nums, m):
        n = len(nums)
        
        # Book allocation impossible
        if m > n:
            return -1
        
        # Calculate the range for binary search
        low = max(nums)
        high = sum(nums)
        
        # Binary search for minimum maximum pages
        while low <= high:
            mid = (low + high) // 2
            students = self.countStudents(nums, mid)
            if students > m:
                low = mid + 1
            else:
                high = mid - 1
                
        return low
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
        ans = ob.findPages(A, D)
        print(ans)
        print("~")

# } Driver Code Ends